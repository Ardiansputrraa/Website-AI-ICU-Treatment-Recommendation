from flask import Flask
from config import Config
from app.extensions import socketio
from pymongo import MongoClient

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
    
    from .routes.vital_prediction import prediction_
    app.register_blueprint(prediction_)
    
    
    from .routes.patient_treatment import treatments_
    app.register_blueprint(treatments_)
    
    from .routes.summary import summary_
    app.register_blueprint(summary_)
    
    from .routes.predict import predict_
    app.register_blueprint(predict_)
    
    socketio.init_app(app)
    
    from .websockets.patient_monitoring_socket import patientMonitoringSocketio
    app.register_blueprint(patientMonitoringSocketio)
    
    from .websockets.data_prediction_socket import dataPredictionSocketio
    app.register_blueprint(dataPredictionSocketio)

    
    return app
