import threading
import time
from app.websockets.patient_monitoring_socket import patientMonitoringSocketio
from app.websockets.vital_prediction_socket import vitalPredictionSocketio
from app.services.patient_vital_service import generate_heart_rate, generate_oxygen_saturation, generate_respiratory_rate, \
    generate_blood_pressure, generate_temperature, icu_beds_values
from app.services.vital_prediction_service import generate_heart_rate_predict, generate_oxygen_saturation_predict, generate_respiratory_rate_predict
from app.services.patient_sofa_service import calculate_sofa_score, renal, nervous, cardiovascular, liver, respiration, coagulation
from app.services.treatment_recommendation_service import random_physician_action, random_ai_recommendation

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
                "patient_detail": {
                    "name": patient["name"],
                    "age": patient["age"],
                    "body_period": patient["body_period"],
                },
                "vital": {
                    "heart_rate": generate_heart_rate(global_time),
                    "oxygen_saturation": generate_oxygen_saturation(global_time),
                    "respiratory_rate": generate_respiratory_rate(global_time),
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
            patientMonitoringSocketio.emit('patient_data', {"bed_id": bed_id, "patient_detail": icu_beds_values[bed_id]["patient_detail"]})
            patientMonitoringSocketio.emit('vital_data', {"bed_id": bed_id, "vital": icu_beds_values[bed_id]["vital"]})
            patientMonitoringSocketio.emit('blood_data', {"bed_id": bed_id, "blood": icu_beds_values[bed_id]["blood"]})
            patientMonitoringSocketio.emit('sofa_data', {"bed_id": bed_id, "sofa": icu_beds_values[bed_id]["sofa"]})
            patientMonitoringSocketio.emit('treatment_recommendation_data', {"bed_id": bed_id, "treatment": icu_beds_values[bed_id]["treatment"]})
            patientMonitoringSocketio.emit('prediction_data', {"bed_id": bed_id, "prediction": icu_beds_values[bed_id]["prediction"]})
        time.sleep(1)
        
def start_patient_thread():
    thread = threading.Thread(target=update_patient_data, daemon=True)
    thread.start()