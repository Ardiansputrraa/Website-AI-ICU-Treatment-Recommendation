from flask import Flask, request, render_template, current_app, Blueprint, jsonify, redirect, url_for
import pandas as pd
from flask_socketio import SocketIO, emit
from app.data_global import icu_beds_values
import jwt

prediction_ = Blueprint('prediction', __name__)
predictionSocketio = SocketIO()

@prediction_.route('/prediction/<bed_id>')
def prediction(bed_id):
    myToken = request.cookies.get("mytoken")
    SECRET_KEY = current_app.config['SECRET_KEY']
    try:
        payload = jwt.decode(myToken, SECRET_KEY, algorithms=["HS256"])
        user_info = current_app.db.users.find_one({"email": payload["id"]})
        return render_template('dashboard/vital-prediction.html', user_info=user_info, bed_id=bed_id)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("auth.sign_in", msg="Login time has expired!"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("auth.sign_in", msg="Please login first!"))

@predictionSocketio.on('get_prediction_data')
def handle_prediction_data_request(data):
    bed_id = data.get('bed_id')
    prediction_data = icu_beds_values[bed_id]["prediction"]
    emit('prediction_data', prediction_data)
    