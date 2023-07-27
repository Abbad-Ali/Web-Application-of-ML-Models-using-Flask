import traceback
from flask import Flask, render_template, request

class ML:
    def __init__(self):
        self.available_models = {
            "face_detection": "/additional_drive/ML/face_detection",
            "car_detection": "/additional_drive/ML/car_detection",
            "shoe_detection": "/additional_drive/ML/shoe_detection",
            "cloth_detection": "/additional_drive/ML/cloth_detection",
            "signal_detection": "/additional_drive/ML/signal_detection",
            "water_level_detection": "/additional_drive/ML/water_level_detection",
            "missile_detection": "/additional_drive/ML/missile_detection"
        }
        self.loaded_models_limit = 2
        self.loaded_models = {} 

        for model in list(self.available_models)[:self.loaded_models_limit]:
            self.loaded_models[model] = {"model": self.available_models[model], "request_count": 1}

    def load_weights(self, model):
        return self.available_models.get(model, None)

    def load_balancer(self, new_model):
        least_frequent_model = min(self.loaded_models, key=lambda model: self.loaded_models[model]["request_count"])
        del self.loaded_models[least_frequent_model]
        self.loaded_models[new_model] = {"model": self.available_models[new_model], "request_count": 1}

    def process_request(self, model):
        if model not in self.loaded_models:
            self.load_balancer(model)

        self.loaded_models[model]["request_count"] += 1
        return ml.loaded_models

app = Flask(__name__)
ml = ML()
@app.route("/")
def get_loaded_models():
    return render_template("model.html", prediction_text= ml.loaded_models)
@app.route('/process_request', methods=['GET', 'POST'])
def process_request():
    try:
        model = request.form["model"]
        return render_template("model.html", prediction_text= ml.process_request(model))
    except:
        return str(traceback.format_exc())

app.run(host='0.0.0.0', port=5000)