from app.data_global import icu_beds_values
import random

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

def calculate_sofa_score():

    score_renal = renal()
    score_nervous = nervous()
    score_cardiovascular = cardiovascular()
    score_liver = liver()
    score_respiration = respiration()
    score_coagulation = coagulation()

    total_score = (score_renal + score_nervous + score_cardiovascular +
                   score_liver + score_respiration + score_coagulation)

    return total_score

def get_sofa_data(bed_id):
    global icu_beds_values
    if bed_id in icu_beds_values:
        return icu_beds_values[bed_id]["sofa"]
    return {"error": "Bed ID tidak ditemukan"}