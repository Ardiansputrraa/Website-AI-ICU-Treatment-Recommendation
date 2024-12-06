from flask import jsonify, Blueprint
import threading
import time
import random
import math
from datetime import datetime

patient_ = Blueprint('patient', __name__)

icu_beds_values = {}
lock = threading.Lock() 

def dateNow():
    current_date = datetime.now()
    formatted_date = current_date.strftime('%a, %d %b %Y')
    return formatted_date


# Fungsi untuk menghasilkan data vital secara dinamis
def generate_heart_rate(global_time):
    baseline = 75
    amplitude = 5
    frequency = 0.1
    noise = random.uniform(-0.25, 0.25)
    # return max(min(baseline + amplitude * math.sin(frequency * global_time) + noise, 120), 50)
    return random.randint(60, 100)


def generate_oxygen_saturation(global_time):
    amplitude = 2
    baseline = 98
    frequency = 0.2
    noise = random.uniform(-0.25, 0.25)
    # return baseline + amplitude * math.sin(frequency * global_time + math.pi / 2) + noise
    return random.randint(90, 100)


def generate_respiratory_rate(global_time):
    amplitude = 2
    baseline = 20
    frequency = 0.1
    noise = random.uniform(-0.5, 0.5)
    # return baseline + amplitude * math.sin(frequency * global_time) + noise
    return random.randint(15, 25)


def generate_blood_pressure(global_time):
    systolic_base = 120
    diastolic_base = 80
    fluctuation = math.sin(global_time * 0.1) * 10
    return {
        "systolic": systolic_base + fluctuation,
        "diastolic": diastolic_base + fluctuation / 2
    }
    # return {
    #      "systolic": random.randint(110, 130),
    #      "diastolic": random.randint(70, 90)
    #  }
    


def generate_temperature(global_time):
    base_temp = 36.5
    fluctuation = math.sin(global_time * 0.05) * 0.5
    return round(base_temp + fluctuation, 1)


def update_patient_data():
    global icu_beds_values
    global_time = 0

    while True:
        with lock:
            global_time += 1
            icu_beds_values = {
                "50100001": {"patient_details": {"name": "Ardian", "address": "Jakarta", "date": dateNow()}},
                "50100002": {"patient_details": {"name": "Dewi", "address": "Bandung", "date": dateNow()}},
                "50100003": {"patient_details": {"name": "Rizal", "address": "Surabaya", "date": dateNow()}},
                "50100004": {"patient_details": {"name": "Lia", "address": "Medan", "date": dateNow()}}
            }
            for bed_id in icu_beds_values:
                icu_beds_values[bed_id]["vital"] = {
                    "heart_rate": generate_heart_rate(global_time),
                    "oxygen_saturation": generate_oxygen_saturation(global_time),
                    "respiratory_rate": generate_respiratory_rate(global_time),
                    "blood_pressure": generate_blood_pressure(global_time),
                    "temperature": generate_temperature(global_time),
                }
                icu_beds_values[bed_id]["blood"] = {
                    "blood_pressure": generate_blood_pressure(global_time),
                    "temperature": generate_temperature(global_time),
                }
        time.sleep(1) 

def initialize_icu_beds():
    global icu_beds_values
    with lock:
        icu_beds_values = {
            "50100001": {"patient_details": {"name": "Ardian", "address": "Jakarta", "date": dateNow()}},
            "50100002": {"patient_details": {"name": "Dewi", "address": "Bandung", "date": dateNow()}},
            "50100003": {"patient_details": {"name": "Rizal", "address": "Surabaya", "date": dateNow()}},
            "50100004": {"patient_details": {"name": "Lia", "address": "Medan", "date": dateNow()}}
        }
        for bed_id in icu_beds_values:
            icu_beds_values[bed_id]["vital"] = {
                "heart_rate": 75,
                "oxygen_saturation": 98,
                "respiratory_rate": 20,
                "blood_pressure": {"systolic": 120, "diastolic": 80},
                "temperature": 36.5
            }
            icu_beds_values[bed_id]["blood"] = {
                "blood_pressure": {"systolic": 120, "diastolic": 80},
                "temperature": 36.5
            }


@patient_.route('/get-vital-data/<bed_id>', methods=['GET'])
def get_vital_data_by_bed(bed_id):
    global icu_beds_values

    with lock:
        if bed_id not in icu_beds_values:
            return jsonify({"error": "Bed ID tidak ditemukan"}), 404

        bed_data = icu_beds_values[bed_id]
        data_vital = bed_data["vital"]
        return jsonify(data_vital)
    
@patient_.route('/get-blood-data/<bed_id>', methods=['GET'])
def get_blood_data_by_bed(bed_id):
    global icu_beds_values

    with lock:
        if bed_id not in icu_beds_values:
            return jsonify({"error": "Bed ID tidak ditemukan"}), 404

        bed_data = icu_beds_values[bed_id]
        data_blood = bed_data["blood"]
        return jsonify(data_blood)
    
@patient_.route('/get-patient-detail/<bed_id>', methods=['GET'])
def get_patient_detail_by_bed(bed_id):
    global icu_beds_values

    with lock:
        if bed_id not in icu_beds_values:
            return jsonify({"error": "Bed ID tidak ditemukan"}), 404

        bed_data = icu_beds_values[bed_id]
        patient_details = bed_data["patient_details"]
        return jsonify(patient_details)

initialize_icu_beds()
threading.Thread(target=update_patient_data, daemon=True).start()
