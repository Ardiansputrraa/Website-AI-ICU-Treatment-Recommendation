from flask import Flask
from config import Config
from pymongo import MongoClient



def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # MONGODB
    client = MongoClient(app.config['MONGODB_URI'])
    app.db = client[app.config['DBNAME']]
    
    from .routes.bed_selection import bed_selection_
    app.register_blueprint(bed_selection_)
    
    return app