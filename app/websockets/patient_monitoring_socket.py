from app.extensions import socketio
from flask import Blueprint
import csv
from flask_socketio import emit
from app.services.monitoring_patient_service import read_data_vital_patient, read_detail_patient
from app.middleware.authenticate import token_required

patientMonitoringSocketio = Blueprint('patient_monitoring', __name__)

file_path_dataset_vital_patient = 'app/data/selected_data.csv'
file_path_dataset_sofal_patient = 'app/data/sofa_indicators.csv'

data_vital_patient = {}
data_sofa_patient = {}

@socketio.on('connect', namespace='/detail_patient')
def handle_connect():
    emit('message', {'status': 'Connected to patient detail'})


@socketio.on('get_detail_patient', namespace='/detail_patient')
def handle_get_data(data):
    icustayid = data.get('icustayid')
    detail_patient = read_detail_patient(float(icustayid))
    emit('detail_patient_data', detail_patient)
    
@socketio.on('connect', namespace='/vital_patient')
def handle_connect():
    emit('message', {'status': 'Connected to data vital patient'})

@socketio.on('get_data_vital_patient', namespace='/vital_patient')
def handle_get_data(data):
    global data_vital_patient
    icustayid = data.get('icustayid')

    if icustayid not in data_vital_patient:
        data_vital_patient[icustayid] = 0

    vital_data = read_data_vital_patient(file_path_dataset_vital_patient, icustayid)

    while True:
        index = data_vital_patient[icustayid]

        if len(vital_data) == 0:
            emit('data_vital_patient', {'error': 'No data available for this patient'})
            break

        row = vital_data[index]

        emit('data_vital_patient', row)

        socketio.sleep(10) 

        data_vital_patient[icustayid] = (index + 1) % len(vital_data)
        
@socketio.on('connect', namespace='/sofa_patient')
def handle_connect():
    emit('message', {'status': 'Connected to data sofa score patient'})

@socketio.on('get_data_sofa_patient', namespace='/sofa_patient')
def handle_get_data(data):
    global data_sofa_patient
    icustayid = data.get('icustayid')

    if icustayid not in data_sofa_patient:
        data_sofa_patient[icustayid] = 0

    sofa_data = read_data_vital_patient(file_path_dataset_sofal_patient, icustayid)

    while True:
        index = data_sofa_patient[icustayid]

        if len(sofa_data) == 0:
            emit('data_sofa_patient', {'error': 'No data available for this patient'})
            break

        row = sofa_data[index]

        emit('data_sofa_patient', row)

        socketio.sleep(10) 

        data_sofa_patient[icustayid] = (index + 1) % len(sofa_data)