import os
from flask import Flask
from config import Config
from pymongo import MongoClient
from dotenv import load_dotenv



def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    SECRET_KEY = os.environ.get("SECRET_KEY")

    MONGODB_URI = os.environ.get("MONGODB_URI")
    DB_NAME =  os.environ.get("DB_NAME")
    
    # MONGODB
    client = MongoClient(MONGODB_URI)
    app.db = client[DB_NAME]
    
    from .routes.bed_selection import bed_selection_
    app.register_blueprint(bed_selection_)
    
    return app