from flask import Flask, jsonify, request, Blueprint
import numpy as np
import pickle
import pandas as pd
from pydantic import BaseModel, Field
from flask_cors import CORS

predict_ = Blueprint('predict', __name__)

@predict_.route('/get-data-vital-four-hour/<bed_id>', methods=['GET'])
def get_treatment_recommendation_data(bed_id):
    data = pd.read_csv('app/./data/df_with_readable_charttime.csv')
    filtered_data = data[data['icustayid'] == float(bed_id)]
    data_vital = filtered_data.to_dict(orient='records')
    return jsonify(data_vital)

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
            "Physician_Action": int(physician_action),
            "Recommended_Action": int(rec_action)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


