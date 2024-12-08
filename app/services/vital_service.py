import random
import math
from datetime import datetime
from app.data_global import icu_beds_values


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


def get_patient_detail(bed_id):
    global icu_beds_values
    if bed_id in icu_beds_values:
        return icu_beds_values[bed_id]["patient_details"]
    return {"error": "Bed ID tidak ditemukan"}

def get_vital_data(bed_id):
    global icu_beds_values
    if bed_id in icu_beds_values:
        return icu_beds_values[bed_id]["vital"]
    return {"error": "Bed ID tidak ditemukan"}

def get_blood_data(bed_id):
    global icu_beds_values
    if bed_id in icu_beds_values:
        return icu_beds_values[bed_id]["blood"]
    return {"error": "Bed ID tidak ditemukan"}
