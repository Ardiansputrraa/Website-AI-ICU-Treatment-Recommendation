from app.data_global import icu_beds_values
import random


def random_physician_action():
    physician_action = [
        ["0 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
    ]
    return random.choice(physician_action)

def random_ai_recommendation():
    ai_recommendations = [
        ["0 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
    ]
    return random.choice(ai_recommendations)

def get_treatment_recommendation(bed_id):
    global icu_beds_values
    if bed_id in icu_beds_values:
        return icu_beds_values[bed_id]["treatment"]
    return {"error": "Bed ID tidak ditemukan"}