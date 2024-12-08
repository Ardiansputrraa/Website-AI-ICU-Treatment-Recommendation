from flask import jsonify, Blueprint
from app.services.vital_service import get_patient_detail, get_vital_data, get_blood_data
from app.services.sofa_service import get_sofa_data
from app.services.treatment_service import get_treatment_recommendation

patient_ = Blueprint('patient', __name__)

@patient_.route('/get-patient-detail/<bed_id>', methods=['GET'])
def get_patient_detail_by_bed(bed_id):
    result = get_patient_detail(bed_id)
    return jsonify(result)

@patient_.route('/get-vital-data/<bed_id>', methods=['GET'])
def get_vital_data_by_bed(bed_id):
    result = get_vital_data(bed_id)
    return jsonify(result)

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
