from flask import jsonify, Blueprint
from flask_socketio import SocketIO, emit
from app.data_global import icu_beds_values
from app.services.vital_service import get_patient_detail, get_vital_data, get_blood_data
from app.services.sofa_service import get_sofa_data
from app.services.treatment_service import get_treatment_recommendation

patient_ = Blueprint('patient', __name__)
patientSocketio = SocketIO()

@patientSocketio.on('connect')
def handle_connect():
    emit('connected', {'message': 'WebSocket connected successfully!'})

@patientSocketio.on('get_patient_data')
def handle_patient_data_request(data):
    bed_id = data.get('bed_id')
    result = icu_beds_values[bed_id]["patient_details"]
    emit('patient_data', result)
    
@patientSocketio.on('get_vital_data')
def handle_vital_data_request(data):
    bed_id = data.get('bed_id')
    result = get_vital_data(bed_id)
    emit('vital_data', result)

@patient_.route('/get-blood-data/<bed_id>', methods=['GET'])
def get_blood_data_by_bed(bed_id):
    result = get_blood_data(bed_id)
    return jsonify(result)

@patient_.route('/get-sofa-data/<bed_id>', methods=['GET'])
def get_sofa_data_by_bed(bed_id):
    result = get_sofa_data(bed_id)
    return jsonify(result)

@patient_.route('/get-treatment-data/<bed_id>', methods=['GET'])
def get_treatment_data_by_bed(bed_id):
    result = get_treatment_recommendation(bed_id)
    return jsonify(result)
