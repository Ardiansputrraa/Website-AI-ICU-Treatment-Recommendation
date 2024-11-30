from flask import Flask, request, render_template, current_app, Blueprint, jsonify, redirect, url_for
import pandas as pd
import jwt

bed_selection_ = Blueprint('home', __name__)

@bed_selection_.route('/')
def home():   
        return render_template('main/index.html')

@bed_selection_.route('/login')
def login():   
        return render_template('auth/register.html')
