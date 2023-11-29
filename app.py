from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return "Go to the URL /predict to make a prediction"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    model = joblib.load("iris_classifier.pkl")
    prediction = model.predict(data["features"])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run()