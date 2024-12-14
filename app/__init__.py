from flask import Flask
from config import Config
from pymongo import MongoClient
from app.task.patient_thread import start_patient_thread
from app.services.vital_prediction_service import load_hr_data_predict, load_rr_data_predict, load_oxygen_data_predict


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    client = MongoClient(app.config['MONGODB_URI'])
    app.db = client[app.config['DBNAME']]
    
    load_hr_data_predict('app/data/selected_data.csv')
    load_oxygen_data_predict('app/data/selected_data.csv')
    load_rr_data_predict('app/data/selected_data.csv')
    
    from .routes.auth import auth_
    app.register_blueprint(auth_)
    
    from .routes.profile import profile_
    app.register_blueprint(profile_)
    
    from .routes.bed_selection import home_
    app.register_blueprint(home_)
    
    from .routes.similarity import similarity_
    app.register_blueprint(similarity_)
    
    from .routes.vital_prediction import prediction_
    app.register_blueprint(prediction_)
    
    from .websockets.vital_prediction_socket import vitalPredictionSocketio
    vitalPredictionSocketio.init_app(app)
    
    from .websockets.patient_monitoring_socket import patientMonitoringSocketio
    patientMonitoringSocketio.init_app(app)
    
    from .routes.patient_treatment import treatments_
    app.register_blueprint(treatments_)
    
    from .routes.summary import summary_
    app.register_blueprint(summary_)

    start_patient_thread()
    
    return app
