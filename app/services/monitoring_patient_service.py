import random
import math
import csv

patients = {
    11.0: {"name": "Abdul Kirom", "age": "60 years old", "body_period": "169 cm 73 kg"},
    12.0: {"name": "Dewi Rahmawati", "age": "45 years old", "body_period": "172 cm 68 kg"},
    13.0: {"name": "Rizal Abdi", "age": "30 years old", "body_period": "160 cm 55 kg"},
    14.0: {"name": "Lia Rahma", "age": "39 years old", "body_period": "180 cm 80 kg"},
    15.0: {"name": "Prasetyo Putra", "age": "55 years old", "body_period": "176 cm 65 kg"},
    16.0: {"name": "Aldo Akfar Rahma", "age": "49 years old", "body_period": "174 cm 73 kg"},
    17.0: {"name": "Kusmita Suryah", "age": "48 years old", "body_period": "166 cm 63 kg"},
    18.0: {"name": "Aldy Hamzah", "age": "68 years old", "body_period": "175 cm 80 kg"},
}

def read_detail_patient(icustayid):
    patient_detail = patients.get(icustayid)
    if patient_detail:
        return patient_detail
    else:
        return {"error": "Patient not found"}

def read_data_vital_patient(file_path, icustayid):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if float(row['icustayid']) == float(icustayid):
                data.append(row)
    return data