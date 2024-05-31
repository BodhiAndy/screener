from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return "Crypto Screener API"

@app.route('/data', methods=['GET'])
def data():
    data = {"example": "This is a placeholder"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
