from flask import send_file
from ml_model import generate_shap_plot
from ml_model import predict_stock
from flask import Flask, request, jsonify
from flask_cors import CORS
from services import search_stock, get_stock_summary

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Stock Screener API is running!"})

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    return jsonify(search_stock(query))

@app.route("/summary", methods=["GET"])
def summary():
    symbol = request.args.get("symbol", "")
    return jsonify(get_stock_summary(symbol))

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    result = predict_stock(data)
    return jsonify(result)
    
@app.route("/shap-image", methods=["POST"])
def shap_image():
    data = request.get_json()
    path = generate_shap_plot(data)
    return send_file(path, mimetype="image/png")
