from flask import Flask, request, render_template, current_app, Blueprint, jsonify, redirect, url_for
import pandas as pd
import random
from datetime import datetime
import jwt

vital_ = Blueprint('vital', __name__)

def get_current_datetime():
    return datetime.now().strftime('%Y-%m-%d')

# Fungsi untuk menghasilkan data medis secara dinamis
def generate_dynamic_data():
    return {
        "heart_rate": random.randint(60, 100),
        "oxygen_saturation": random.randint(90, 100),  # Range: 90-100
        "respiratory_rate": random.randint(15, 25),   # Range: 15-25
        "blood_pressure_mm": random.randint(110, 130),  # Systolic: 110-130
        "blood_pressure_hg": random.randint(70, 90),    # Diastolic: 70-90
        "temperature": round(random.uniform(36.5, 38.5), 1)  # Range: 36.5-38.5
    }

# Data global untuk bed ICU dan pasien
icu_beds = {
    "5010001": {
        "patient_details": {
            "nama": "Ardian",
            "alamat": "Jakarta",
            "date_now": get_current_datetime()
        },
        "data": generate_dynamic_data()
    },
    "5010002": {
        "patient_details": {
            "nama": "Dewi",
            "alamat": "Bandung",
            "date_now": get_current_datetime()
        },
        "data": generate_dynamic_data()
    },
    "5010003": {
        "patient_details": {
            "nama": "Rizal",
            "alamat": "Surabaya",
            "date_now": get_current_datetime()
        },
        "data": generate_dynamic_data()
    },
    "5010004": {
        "patient_details": {
            "nama": "Lia",
            "alamat": "Medan",
            "date_now": get_current_datetime()
        },
        "data": generate_dynamic_data()
    },
    "5010005": {
        "patient_details": {
            "nama": "Budi",
            "alamat": "Semarang",
            "date_now": get_current_datetime()
        },
        "data": generate_dynamic_data()
    },
    "5010006": {
        "patient_details": {
            "nama": "Siti",
            "alamat": "Makassar",
            "date_now": get_current_datetime()
        },
        "data": generate_dynamic_data()
    },
    "5010007": {
        "patient_details": {
            "nama": "Adi",
            "alamat": "Palembang",
            "date_now": get_current_datetime()
        },
        "data": generate_dynamic_data()
    },
    "5010008": {
        "patient_details": {
            "nama": "Rina",
            "alamat": "Yogyakarta",
            "date_now": get_current_datetime()
        },
        "data": generate_dynamic_data()
    }
}

@vital_.route('/get-data-vital/<bed_id>', methods=['POST'])
def update_data(bed_id):
    try:
        if bed_id in icu_beds:
            # Generate new data for the specified bed
            icu_beds[bed_id]["data"] = generate_dynamic_data()
            icu_beds[bed_id]["patient_details"]["date_now"] = get_current_datetime()
            return jsonify(icu_beds[bed_id]["data"])  # Only return the data part for that bed
        return jsonify({"error": "Bed ID tidak ditemukan"}), 404
    except jwt.ExpiredSignatureError:
        return redirect(url_for("auth.sign_in", msg="Login time has expired!"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("auth.sign_in", msg="Please login first!"))

 