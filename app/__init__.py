from flask import Flask
from config import Config
from pymongo import MongoClient
from app.task.patient_thread import start_patient_thread

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    client = MongoClient(app.config['MONGODB_URI'])
    app.db = client[app.config['DBNAME']]
    
    from .routes.auth import auth_
    app.register_blueprint(auth_)
    
    from .routes.profile import profile_
    app.register_blueprint(profile_)
    
    from .routes.bed_selection import home_
    app.register_blueprint(home_)
    
    from .routes.similarity import similarity_
    app.register_blueprint(similarity_)
    
    from .routes.prediction import prediction_
    app.register_blueprint(prediction_)
    
    from .routes.patient import patient_
    app.register_blueprint(patient_)
    
    from .routes.treatments import treatments_
    app.register_blueprint(treatments_)
    
    from .routes.summary import summary_
    app.register_blueprint(summary_)

    start_patient_thread()
    
    return app
