from flask import Flask, jsonify, request, Blueprint
import numpy as np
import pickle
import pandas as pd
from pydantic import BaseModel, Field
import numpy as np
import copy
import random
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import torch
from flask_cors import CORS
from app.data.deepQnet_v2 import Dist_DQN
from app.services.treatment_recommendation_service import physicianAction, aiRecommendation 
import numpy as np
from joblib import load
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

predict_ = Blueprint('predict', __name__)


# with open('app/./data/Qon.pkl', 'rb') as file:
#     Qon = pickle.load(file)

# with open('app/./data/C.pkl', 'rb') as file:
#     C = pickle.load(file)

# with open('app/./data/physpol.pkl', 'rb') as file:
#     physpol = pickle.load(file)


# patients_kmeans_model = load('app/data/patients_kmeans_model.pkl')
# pca_model = load('app/data/pca_model.pkl')
# state_kmeans_model = load('app/data/state_kmeans_model.pkl')
# transition_prob = load('app/data/transition_prob.pkl')

# @predict_.route("/predict", methods=["POST"])
# def predict():
#     try:
#         input_data = request.json
#         phys_OptimalAction = np.argmax(physpol, axis=1).reshape(-1, 1)
#         OptimalAction = np.argmax(Qon, axis=1).reshape(-1, 1)
#         user_input = pd.DataFrame([input_data])
#         current_state = C.predict(user_input)
#         physician_action = phys_OptimalAction[current_state][0]
#         rec_action = OptimalAction[current_state][0]

#         return jsonify({
#             "Physician_Action": physicianAction(int(physician_action)),
#             "Recommended_Action": aiRecommendation(int(rec_action))
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400
    
# def load_model(model_path, cluster):
#     model = Dist_DQN()  
#     checkpoint = torch.load(model_path)
#     model.Q.load_state_dict(checkpoint['Q_state_dict'])
#     model.Q_target.load_state_dict(checkpoint['Q_target_state_dict'])
#     model.Q.eval() 
#     model.Q_target.eval()
#     return model

# def randomAction():
#     return np.random.choice(25)

# def patient_clustering_single(X):
#     # Extract single action
#     action = randomAction()
#     print('action', action)
#     # State Clustering
#     state = state_kmeans_model.predict(X.reshape(1, -1))[0]  # Extract single value
#     print('State', state)

#     # Predict Next State using Transition Probability
#     # next_state = transition_prob[state][action].argmax()  # Based on previous state & action

#     ncl = 200
#     # Action-State Representation
#     nact = 5 * 5
#     SA = np.zeros((ncl, nact))

#     for s in range(ncl):
#         for a in range(nact):
#             SA[s, a] = transition_prob[s][a].argmax()

#     scaler = MinMaxScaler()
#     SA_norm = scaler.fit_transform(SA)
#     temp_testCount = copy.deepcopy(SA_norm)
#     counter = copy.deepcopy(SA)
    
#     # counter[state, action] = next_state
    
#     sum_counter = counter[state, action].sum()
#     print('sum_counter:', sum_counter)
#     temp_testCount[state, action] = counter[state, action] / sum_counter
            
#     # temp_testCount[state, action] = counter[state, action] / counter[state, action].sum()

#     #if batch_cls['bloc'].iloc[i + 1] == 1:
#     temp_testCount = np.nan_to_num(temp_testCount, nan=0)  # Ganti NaN dengan 0
#     x_new_pca = pca_model.transform(temp_testCount.flatten().reshape(1, -1))
    
#     return patients_kmeans_model.predict(x_new_pca)[0]


# @predict_.route("/predict-personalize", methods=["POST"])
# def predict_personalize():
#     try:
#         input_data = request.json
#         user_input = pd.DataFrame([input_data])
#         user_input = user_input.apply(pd.to_numeric, errors='coerce') 
#         model_path_1 = 'app/data/model_0100.pt'
#         loaded_model_1 = load_model(model_path_1, 2)
#         model_path_2 = 'app/data/model_0100.pt'
#         loaded_model_2 = load_model(model_path_2, 2)
#         model_path_3 = 'app/data/model_0100.pt'
#         loaded_model_3 = load_model(model_path_3, 2)
#         model_path_4 = 'app/data/model_0100.pt'
#         loaded_model_4 = load_model(model_path_4, 2)
#         reformat2 = user_input.values.copy()
#         colnorm = ['SOFA', 'age', 'Weight_kg', 'GCS', 'HR', 'SysBP', 'MeanBP', 'DiaBP', 'RR', 'Temp_C',
#                    'Sodium', 'Chloride', 'Glucose', 'Calcium', 'Hb', 'WBC_count', 'Platelets_count',
#                    'PTT', 'PT', 'Arterial_pH', 'paO2', 'paCO2', 'HCO3', 'Arterial_lactate', 'Shock_Index',
#                    'PaO2_FiO2', 'cumulated_balance', 'CO2_mEqL', 'Ionised_Ca']
#         collog = ['SpO2', 'BUN', 'Creatinine', 'SGOT', 'Total_bili', 'INR', 'input_total', 'output_total']
#         collog_indices = np.where(np.isin(user_input.columns, collog))[0]
#         colnorm_indices = np.where(np.isin(user_input.columns, colnorm))[0]

#         if colnorm_indices.size > 0:
#             reformat2_colnorm = reformat2[:, colnorm_indices]
#             mean = 1016.931959759328
#             std_dev = 3590.0479651268106
#             reformat2_colnorm = (reformat2_colnorm - mean) / std_dev
#         else:
#             reformat2_colnorm = np.zeros((reformat2.shape[0], len(colnorm)))

#         if collog_indices.size > 0:
#             reformat2_collog = reformat2[:, collog_indices]
#             reformat2_collog = np.log(0.1 + reformat2_collog)
#         else:
#             reformat2_collog = np.zeros((reformat2.shape[0], len(collog)))

#         reformat2 = np.hstack((reformat2_colnorm, reformat2_collog))
        
#         single_state = torch.tensor(reformat2, dtype=torch.float32).unsqueeze(0)
#         cluster = patient_clustering_single(single_state)
#         print('Cluster:', cluster)
        
#         if cluster == 0:
#             loaded_model = loaded_model_1
#         elif cluster == 1:
#             loaded_model = loaded_model_2
#         elif cluster == 2:
#             loaded_model = loaded_model_3
#         else:
#             loaded_model = loaded_model_4
            
#         with torch.no_grad():
#             q_values = loaded_model.Q(single_state)
#             predicted_action = torch.argmax(q_values).item()

#         return jsonify({
#             "recommended_action_model_personalize": aiRecommendation(int(predicted_action))
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400
    
# @predict_.route("/predict-generalize", methods=["POST"])
# def predict_generalize():
#     try:
#         input_data = request.json
#         user_input = pd.DataFrame([input_data])
#         user_input = user_input.apply(pd.to_numeric, errors='coerce') 
#         model_path = 'app/data/model_0100.pt'
#         loaded_model = load_model(model_path, 2)
#         reformat2 = user_input.values.copy()
#         colnorm = ['SOFA', 'age', 'Weight_kg', 'GCS', 'HR', 'SysBP', 'MeanBP', 'DiaBP', 'RR', 'Temp_C',
#                    'Sodium', 'Chloride', 'Glucose', 'Calcium', 'Hb', 'WBC_count', 'Platelets_count',
#                    'PTT', 'PT', 'Arterial_pH', 'paO2', 'paCO2', 'HCO3', 'Arterial_lactate', 'Shock_Index',
#                    'PaO2_FiO2', 'cumulated_balance', 'CO2_mEqL', 'Ionised_Ca']
#         collog = ['SpO2', 'BUN', 'Creatinine', 'SGOT', 'Total_bili', 'INR', 'input_total', 'output_total']
#         collog_indices = np.where(np.isin(user_input.columns, collog))[0]
#         colnorm_indices = np.where(np.isin(user_input.columns, colnorm))[0]

#         if colnorm_indices.size > 0:
#             reformat2_colnorm = reformat2[:, colnorm_indices]
#             mean = 1016.931959759328
#             std_dev = 3590.0479651268106
#             reformat2_colnorm = (reformat2_colnorm - mean) / std_dev
#         else:
#             reformat2_colnorm = np.zeros((reformat2.shape[0], len(colnorm)))

#         if collog_indices.size > 0:
#             reformat2_collog = reformat2[:, collog_indices]
#             reformat2_collog = np.log(0.1 + reformat2_collog)
#         else:
#             reformat2_collog = np.zeros((reformat2.shape[0], len(collog)))

#         reformat2 = np.hstack((reformat2_colnorm, reformat2_collog))
        
#         single_state = torch.tensor(reformat2, dtype=torch.float32).unsqueeze(0)

#         with torch.no_grad():
#             q_values = loaded_model.Q(single_state)
#             predicted_action = torch.argmax(q_values).item()

#         return jsonify({
#             "recommended_action_model_generalize": aiRecommendation(int(predicted_action))
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400
