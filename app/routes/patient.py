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

# Fungsi untuk menghitung SOFA score masing-masing organ
def renal():
    creatinine = random.uniform(0.5, 6.0)
    urine_output = random.randint(0, 1000)
    if creatinine >= 5.0 or urine_output < 200:
        return 4
    elif creatinine >= 3.5 or urine_output < 500:
        return 3
    elif creatinine >= 2.0:
        return 2
    elif creatinine >= 1.2:
        return 1
    else:
        return 0

def nervous():
    gcs = random.randint(3, 15)
    if gcs < 6:
        return 4
    elif gcs <= 9:
        return 3
    elif gcs <= 12:
        return 2
    elif gcs <= 14:
        return 1
    else:
        return 0

def cardiovascular():
    map_value = random.randint(50, 100)
    vasopressors = random.choice(["none", "low", "medium", "high"])
    if map_value < 70 and vasopressors == "high":
        return 4
    elif vasopressors == "medium":
        return 3
    elif vasopressors == "low":
        return 2
    elif map_value < 70:
        return 1
    else:
        return 0

def liver():
    bilirubin = random.uniform(0.5, 15.0)
    if bilirubin >= 12.0:
        return 4
    elif bilirubin >= 6.0:
        return 3
    elif bilirubin >= 2.0:
        return 2
    elif bilirubin >= 1.2:
        return 1
    else:
        return 0

def respiration():
    pao2_fio2_ratio = random.randint(50, 500)
    if pao2_fio2_ratio < 100:
        return 4
    elif pao2_fio2_ratio < 200:
        return 3
    elif pao2_fio2_ratio < 300:
        return 2
    elif pao2_fio2_ratio < 400:
        return 1
    else:
        return 0

def coagulation():
    platelet_count = random.randint(10, 200)
    if platelet_count < 20:
        return 4
    elif platelet_count < 50:
        return 3
    elif platelet_count < 100:
        return 2
    elif platelet_count < 150:
        return 1
    else:
        return 0

# Fungsi untuk menghitung total SOFA score
def calculate_sofa_score():

    score_renal = renal()
    score_nervous = nervous()
    score_cardiovascular = cardiovascular()
    score_liver = liver()
    score_respiration = respiration()
    score_coagulation = coagulation()

    # Total SOFA score
    total_score = (score_renal + score_nervous + score_cardiovascular +
                   score_liver + score_respiration + score_coagulation)

    return total_score

def update_patient_data():
    global icu_beds_values
    global_time = 0

    while True:
        with lock:
            global_time += 1
            icu_beds_values = {
                "50100001": {"patient_details": {"name": "Abdul Kirom", "address": "Jakarta", "date": dateNow()}},
                "50100002": {"patient_details": {"name": "Dewi Rahmawati", "address": "Bandung", "date": dateNow()}},
                "50100003": {"patient_details": {"name": "Rizal Abdi", "address": "Surabaya", "date": dateNow()}},
                "50100004": {"patient_details": {"name": "Lia Rahma", "address": "Medan", "date": dateNow()}},
                "50100005": {"patient_details": {"name": "Prasetyo Putra", "address": "Bali", "date": dateNow()}},
                "50100006": {"patient_details": {"name": "Aldo Akfar Rahma", "address": "Padang", "date": dateNow()}},
                "50100007": {"patient_details": {"name": "Kusmita Suryah", "address": "Balikpapan", "date": dateNow()}},
                "50100008": {"patient_details": {"name": "Aldy Hamzah", "address": "Pontianak", "date": dateNow()}}
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
                icu_beds_values[bed_id]["sofa"] = {
                    "sofa_score": calculate_sofa_score(),
                    "renal": renal(),
                    "nervous": nervous(),
                    "cardiovascular": cardiovascular(),
                    "liver": liver(),
                    "respiration": respiration(),
                    "coagulation": coagulation(),
                }
        time.sleep(1) 

def initialize_icu_beds():
    global icu_beds_values
    with lock:
        icu_beds_values = {
            "50100001": {"patient_details": {"name": "Abdul Kirom", "address": "Jakarta", "date": dateNow()}},
            "50100002": {"patient_details": {"name": "Dewi Rahmawati", "address": "Bandung", "date": dateNow()}},
            "50100003": {"patient_details": {"name": "Rizal Abdi", "address": "Surabaya", "date": dateNow()}},
            "50100004": {"patient_details": {"name": "Lia Rahma", "address": "Medan", "date": dateNow()}},
            "50100005": {"patient_details": {"name": "Prasetyo Putra", "address": "Bali", "date": dateNow()}},
            "50100006": {"patient_details": {"name": "Aldo Akfar Rahma", "address": "Padang", "date": dateNow()}},
            "50100007": {"patient_details": {"name": "Kusmita Suryah", "address": "Balikpapan", "date": dateNow()}},
            "50100008": {"patient_details": {"name": "Aldy Hamzah", "address": "Pontianak", "date": dateNow()}}
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
            icu_beds_values[bed_id]["sofa"] = {
                    "sofa_score": calculate_sofa_score(),
                    "renal": renal(),
                    "nervous": nervous(),
                    "cardiovascular": cardiovascular(),
                    "liver": liver(),
                    "respiration": respiration(),
                    "coagulation": coagulation(),
            }

@patient_.route('/get-patient-detail/<bed_id>', methods=['GET'])
def get_patient_detail_by_bed(bed_id):
    global icu_beds_values

    with lock:
        if bed_id not in icu_beds_values:
            return jsonify({"error": "Bed ID tidak ditemukan"}), 404

        bed_data = icu_beds_values[bed_id]
        patient_details = bed_data["patient_details"]
        return jsonify(patient_details)

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
    
@patient_.route('/get-sofa-data/<bed_id>', methods=['GET'])
def get_sofa_data_by_bed(bed_id):
    global icu_beds_values

    with lock:
        if bed_id not in icu_beds_values:
            return jsonify({"error": "Bed ID tidak ditemukan"}), 404

        bed_data = icu_beds_values[bed_id]
        data_sofa = bed_data["sofa"]
        return jsonify(data_sofa)

initialize_icu_beds()
threading.Thread(target=update_patient_data, daemon=True).start()
