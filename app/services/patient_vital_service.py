import random
import math
import csv
from app.data_global import icu_beds_values


def generate_heart_rate(global_time):
    baseline = 75
    amplitude = 5
    frequency = 0.1
    noise = random.uniform(-0.25, 0.25)
    return max(min(baseline + amplitude * math.sin(frequency * global_time) + noise, 120), 50)
     

def generate_oxygen_saturation(global_time):
    amplitude = 2
    baseline = 98
    frequency = 0.2
    noise = random.uniform(-0.25, 0.25)
    return baseline + amplitude * math.sin(frequency * global_time + math.pi / 2) + noise
    

def generate_respiratory_rate(global_time):
    amplitude = 2
    baseline = 20
    frequency = 0.1
    noise = random.uniform(-0.5, 0.5)
    return baseline + amplitude * math.sin(frequency * global_time) + noise
    

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

