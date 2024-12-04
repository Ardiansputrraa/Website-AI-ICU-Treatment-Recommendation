from flask import Flask, request, render_template, current_app, Blueprint, jsonify, redirect, url_for
import json
import jwt

similarity_ = Blueprint('similarity', __name__)

@similarity_.route('/similarity')
def summary():
    myToken = request.cookies.get("mytoken")
    SECRET_KEY = current_app.config['SECRET_KEY']
    try:
        payload = jwt.decode(myToken, SECRET_KEY, algorithms=["HS256"])
        user_info = current_app.db.users.find_one({"email": payload["id"]})
        return render_template('main/similarity.html', user_info=user_info, title="Similarity")
    except jwt.ExpiredSignatureError:
        return redirect(url_for("auth.sign_in", msg="Login time has expired!"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("auth.sign_in", msg="Please login first!"))