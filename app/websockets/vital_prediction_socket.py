from flask_socketio import SocketIO, emit
from app.data_global import icu_beds_values
from app.middleware.authenticate import token_required

vitalPredictionSocketio = SocketIO()

@vitalPredictionSocketio.on('get_prediction_data')
@token_required
def handle_prediction_data_request(data):
    bed_id = data.get('bed_id')
    prediction_data = icu_beds_values[bed_id]["prediction"]
    emit('prediction_data', prediction_data)