from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model + metadata
model_data = pickle.load(open("model.pkl", "rb"))
model = model_data["model"]
features = model_data["features"]

@app.route('/')
def home():
    return "API Running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # Ensure correct feature order
        input_data = [data[feature] for feature in features]

        prediction = model.predict([input_data])[0]

        return jsonify({
            "predicted_score": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)