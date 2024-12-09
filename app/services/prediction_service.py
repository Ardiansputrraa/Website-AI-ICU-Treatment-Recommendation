import random
import math
from app.data_global import icu_beds_values

def generate_heart_rate_predict(global_time):
    # baseline = 75
    # amplitude = 5
    # frequency = 0.1
    # noise = random.uniform(-0.25, 0.25)
    # return max(min(baseline + amplitude * math.sin(frequency * global_time) + noise, 120), 50)
    return random.randint(60, 100)

def generate_oxygen_saturation_predict(global_time):
    # amplitude = 2
    # baseline = 98
    # frequency = 0.2
    # noise = random.uniform(-0.25, 0.25)
    # return baseline + amplitude * math.sin(frequency * global_time + math.pi / 2) + noise
    return random.randint(90, 100)

def generate_respiratory_rate_predict(global_time):
    # amplitude = 2
    # baseline = 20
    # frequency = 0.1
    # noise = random.uniform(-0.5, 0.5)
    # return baseline + amplitude * math.sin(frequency * global_time) + noise
    return random.randint(15, 25)


def get_prediction_data(bed_id):
    global icu_beds_values
    if bed_id in icu_beds_values:
        return icu_beds_values[bed_id]["prediction"]
    return {"error": "Bed ID tidak ditemukan"}

