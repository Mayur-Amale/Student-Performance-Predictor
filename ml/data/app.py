from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = [[
        data["study_hours"],
        data["attendance"],
        data["sleep_hours"],
        data["previous_marks"]
    ]]
    score = model.predict(features)[0]
    return jsonify({"predicted_score": round(float(score), 2)})

if __name__ == "__main__":
    app.run(debug=True)
