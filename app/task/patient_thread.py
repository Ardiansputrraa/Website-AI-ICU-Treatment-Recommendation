import threading
import time
from app.services.vital_service import generate_heart_rate, generate_oxygen_saturation, generate_respiratory_rate, dateNow, \
    generate_blood_pressure, generate_temperature, icu_beds_values
from app.services.sofa_service import calculate_sofa_score, renal, nervous, cardiovascular, liver, respiration, coagulation
from app.services.treatment_service import random_physician_action, random_ai_recommendation

patients = [
    {"name": "Abdul Kirom", "address": "Jakarta"},
    {"name": "Dewi Rahmawati", "address": "Bandung"},
    {"name": "Rizal Abdi", "address": "Surabaya"},
    {"name": "Lia Rahma", "address": "Medan"},
    {"name": "Prasetyo Putra", "address": "Bali"},
    {"name": "Aldo Akfar Rahma", "address": "Padang"},
    {"name": "Kusmita Suryah", "address": "Balikpapan"},
    {"name": "Aldy Hamzah", "address": "Pontianak"},
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
                    "address": patient["address"],
                    "date": dateNow(),
                },
                "vital": {
                    "heart_rate": generate_heart_rate(global_time),
                    "oxygen_saturation": generate_oxygen_saturation(global_time),
                    "respiratory_rate": generate_respiratory_rate(global_time),
                    "blood_pressure": generate_blood_pressure(global_time),
                    "temperature": generate_temperature(global_time),
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