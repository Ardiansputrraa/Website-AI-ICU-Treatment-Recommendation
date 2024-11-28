from flask import Flask, request, render_template, current_app, Blueprint, jsonify, redirect, url_for
import pandas as pd
import jwt

bed_selection_ = Blueprint('dashboard', __name__)

@bed_selection_.route('/')
def dashboard():   
        return render_template('dashboard/index.html')
