from flask import Flask, jsonify, request, Blueprint
import numpy as np
import pickle
import pandas as pd
from pydantic import BaseModel, Field
import torch
from flask_cors import CORS
from app.data.deepQnet_v2 import Dist_DQN
from app.services.treatment_recommendation_service import physicianAction, aiRecommendation 

predict_ = Blueprint('predict', __name__)


with open('app/./data/Qon.pkl', 'rb') as file:
    Qon = pickle.load(file)

with open('app/./data/C.pkl', 'rb') as file:
    C = pickle.load(file)

with open('app/./data/physpol.pkl', 'rb') as file:
    physpol = pickle.load(file)

phys_OptimalAction = np.argmax(physpol, axis=1).reshape(-1, 1)

OptimalAction = np.argmax(Qon, axis=1).reshape(-1, 1)

@predict_.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.json
        
        user_input = pd.DataFrame([input_data])

        current_state = C.predict(user_input)

        physician_action = phys_OptimalAction[current_state][0]

        rec_action = OptimalAction[current_state][0]

        return jsonify({
            "Physician_Action": physicianAction(int(physician_action)),
            "Recommended_Action": aiRecommendation(int(rec_action))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
def load_model(model_path, cluster):
    model = Dist_DQN()  
    checkpoint = torch.load(model_path)
    model.Q.load_state_dict(checkpoint['Q_state_dict'])
    model.Q_target.load_state_dict(checkpoint['Q_target_state_dict'])
    model.Q.eval() 
    model.Q_target.eval()
    return model


@predict_.route("/predict-qnet", methods=["POST"])
def predict_qnet():
    try:
        input_data = request.json
        user_input = pd.DataFrame([input_data])
        user_input = user_input.apply(pd.to_numeric, errors='coerce') 
        model_path = 'app/data/model_0100.pt'
        loaded_model = load_model(model_path, 2)
        reformat2 = user_input.values.copy()
        colnorm = ['SOFA', 'age', 'Weight_kg', 'GCS', 'HR', 'SysBP', 'MeanBP', 'DiaBP', 'RR', 'Temp_C',
                   'Sodium', 'Chloride', 'Glucose', 'Calcium', 'Hb', 'WBC_count', 'Platelets_count',
                   'PTT', 'PT', 'Arterial_pH', 'paO2', 'paCO2', 'HCO3', 'Arterial_lactate', 'Shock_Index',
                   'PaO2_FiO2', 'cumulated_balance', 'CO2_mEqL', 'Ionised_Ca']
        collog = ['SpO2', 'BUN', 'Creatinine', 'SGOT', 'Total_bili', 'INR', 'input_total', 'output_total']
        collog_indices = np.where(np.isin(user_input.columns, collog))[0]
        colnorm_indices = np.where(np.isin(user_input.columns, colnorm))[0]

        if colnorm_indices.size > 0:
            reformat2_colnorm = reformat2[:, colnorm_indices]
            mean = 1016.931959759328
            std_dev = 3590.0479651268106
            reformat2_colnorm = (reformat2_colnorm - mean) / std_dev
        else:
            reformat2_colnorm = np.zeros((reformat2.shape[0], len(colnorm)))

        if collog_indices.size > 0:
            reformat2_collog = reformat2[:, collog_indices]
            reformat2_collog = np.log(0.1 + reformat2_collog)
        else:
            reformat2_collog = np.zeros((reformat2.shape[0], len(collog)))

        reformat2 = np.hstack((reformat2_colnorm, reformat2_collog))
        
        single_state = torch.tensor(reformat2, dtype=torch.float32).unsqueeze(0)
        
        with torch.no_grad():
            q_values = loaded_model.Q(single_state)
            predicted_action = torch.argmax(q_values).item()

        return jsonify({
            "recommended_action_model_qnet": aiRecommendation(int(predicted_action))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
