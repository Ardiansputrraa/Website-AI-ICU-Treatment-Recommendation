from flask import Flask, request, render_template, current_app, Blueprint, jsonify, redirect, url_for
import pandas as pd
import jwt
from app.services.vital_prediction_service import get_prediction_data

prediction_ = Blueprint('prediction', __name__)

@prediction_.route('/prediction/<bed_id>')
def prediction(bed_id):
    myToken = request.cookies.get("mytoken")
    SECRET_KEY = current_app.config['SECRET_KEY']
    try:
        payload = jwt.decode(myToken, SECRET_KEY, algorithms=["HS256"])
        user_info = current_app.db.users.find_one({"email": payload["id"]})
        return render_template('dashboard/prediction.html', user_info=user_info, bed_id=bed_id)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("auth.sign_in", msg="Login time has expired!"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("auth.sign_in", msg="Please login first!"))
    
@prediction_.route('/get-prediction-data/<bed_id>', methods=['GET'])
def get_prediction_data_by_bed(bed_id):
    result = get_prediction_data(bed_id)
    return jsonify(result)