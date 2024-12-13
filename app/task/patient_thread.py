import threading
import time
from datetime import datetime
from app.services.vital_service import generate_heart_rate, generate_oxygen_saturation, generate_respiratory_rate, \
    generate_blood_pressure, generate_temperature, icu_beds_values
from app.services.prediction_service import generate_heart_rate_predict, generate_oxygen_saturation_predict, generate_respiratory_rate_predict
from app.services.sofa_service import calculate_sofa_score, renal, nervous, cardiovascular, liver, respiration, coagulation
from app.services.treatment_service import random_physician_action, random_ai_recommendation

def dateNow():
    current_date = datetime.now()
    formatted_date = current_date.strftime('%a, %d %b %Y')
    return formatted_date

patients = [
    {"name": "Abdul Kirom", "age": "60 years old", "body_period": "169 cm 73 kg"},
    {"name": "Dewi Rahmawati", "age": "45 years old", "body_period": "172 cm 68 kg"},
    {"name": "Rizal Abdi", "age": "30 years old", "body_period": "160 cm 55 kg"},
    {"name": "Lia Rahma", "age": "39 years old", "body_period": "180 cm 80 kg"},
    {"name": "Prasetyo Putra", "age": "55 years old", "body_period": "176 cm 65 kg"},
    {"name": "Aldo Akfar Rahma", "age": "49 years old", "body_period": "174 cm 73 kg"},
    {"name": "Kusmita Suryah", "age": "48 years old", "body_period": "166 cm 63 kg"},
    {"name": "Aldy Hamzah", "age": "68 years old", "body_period": "175 cm 80 kg"},
]


def update_patient_data():
    
    global_time = 0

    while True:
        global_time += 1
        for i in range(1, 9):
            bed_id = f"5010000{i}"
            patient = patients[i - 1]
            icu_beds_values[bed_id] = {
                "patient_details": {
                    "name": patient["name"],
                    "age": patient["age"],
                    "body_period": patient["body_period"],
                },
                "vital": {
                    "heart_rate": generate_heart_rate(),
                    "oxygen_saturation": generate_oxygen_saturation(),
                    "respiratory_rate": generate_respiratory_rate(),
                    "blood_pressure": generate_blood_pressure(global_time),
                    "temperature": generate_temperature(global_time),
                },
                "prediction": {
                    "heart_rate_predict": generate_heart_rate_predict(global_time),
                    "oxygen_saturation_predict": generate_oxygen_saturation_predict(global_time),
                    "respiratory_rate_predict": generate_respiratory_rate_predict(global_time),
                },
                "blood": {
                    "blood_pressure": generate_blood_pressure(global_time),
                    "temperature": generate_temperature(global_time),
                },
                "sofa": {
                    "sofa_score": calculate_sofa_score(),
                    "renal": renal(),
                    "nervous": nervous(),
                    "cardiovascular": cardiovascular(),
                    "liver": liver(),
                    "respiration": respiration(),
                    "coagulation": coagulation(),
                },
                "treatment": {
                    "physician_action": random_physician_action(),
                    "ai_recommendations": random_ai_recommendation(),
                },
            }
        time.sleep(1)
        
def start_patient_thread():
    thread = threading.Thread(target=update_patient_data, daemon=True)
    thread.start()