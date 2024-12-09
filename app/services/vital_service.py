import random
import math
from app.data_global import icu_beds_values

def generate_heart_rate():
    return random.randint(60, 100)


def generate_oxygen_saturation():
    return random.randint(90, 100)


def generate_respiratory_rate():
    return random.randint(15, 25)


def generate_blood_pressure(global_time):
    systolic_base = 120
    diastolic_base = 80
    fluctuation = math.sin(global_time * 0.1) * 10
    return {
        "systolic": systolic_base + fluctuation,
        "diastolic": diastolic_base + fluctuation / 2
    }

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
