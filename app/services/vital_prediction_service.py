import csv
from app.data_global import icu_beds_values, hr_data, rr_data, oxygen_data

def load_hr_data_predict(csv_file):
    global hr_data
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        hr_data = [float(row['HR']) for row in reader] 
        
def load_oxygen_data_predict(csv_file):
    global oxygen_data
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        oxygen_data = [float(row['SpO2']) for row in reader] 
        
def load_rr_data_predict(csv_file):
    global rr_data
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        rr_data = [float(row['RR']) for row in reader] 
        
def generate_heart_rate_predict(global_time):
    if not hr_data:
        raise ValueError("HR data is not loaded. Please call load_hr_data first.")
    index = global_time % len(hr_data)  
    return round(hr_data[index]) 

def generate_oxygen_saturation_predict(global_time):
    if not oxygen_data:
        raise ValueError("SpO2 data is not loaded. Please call load_oxygen_data first.")
    index = global_time % len(oxygen_data)  
    return round(oxygen_data[index]) 

def generate_respiratory_rate_predict(global_time):
    if not rr_data:
        raise ValueError("RR data is not loaded. Please call load_rr_data first.")
    index = global_time % len(rr_data)  
    return round(rr_data[index])


def get_prediction_data(bed_id):
    global icu_beds_values
    if bed_id in icu_beds_values:
        return icu_beds_values[bed_id]["prediction"]
    return {"error": "Bed ID tidak ditemukan"}

