from flask_socketio import SocketIO, emit
from app.data_global import icu_beds_values
from app.middleware.authenticate import token_required

patientMonitoringSocketio = SocketIO()

@patientMonitoringSocketio.on('get_patient_data')
@token_required
def handle_patient_data_request(data):
    bed_id = data.get('bed_id')
    patient_data = icu_beds_values[bed_id]["patient_details"]
    emit('patient_data', patient_data)
    
@patientMonitoringSocketio.on('get_vital_data')
@token_required
def handle_vital_data_request(data):
    bed_id = data.get('bed_id')
    vital_data = icu_beds_values[bed_id]["vital"]
    emit('vital_data', vital_data)

@patientMonitoringSocketio.on('get_blood_data')
@token_required
def handle_blood_data_request(data):
    bed_id = data.get('bed_id')
    blood_data = icu_beds_values[bed_id]["blood"]
    emit('blood_data', blood_data)
    
@patientMonitoringSocketio.on('get_sofa_data')
@token_required
def handle_sofa_data_request(data):
    bed_id = data.get('bed_id')
    sofa_data = icu_beds_values[bed_id]["sofa"]
    emit('sofa_data', sofa_data)
    
@patientMonitoringSocketio.on('get_treatment_recommendation_data')
@token_required
def handle_treatment_recommendation_data_request(data):
    bed_id = data.get('bed_id')
    treatment_recommendation_data = icu_beds_values[bed_id]["treatment_recommendation"]
    emit('treatment_recommendation_data', treatment_recommendation_data)
