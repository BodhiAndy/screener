from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_crypto_data():
    # Binance API endpoint for example
    url = 'https://api.binance.com/api/v3/ticker/24hr'
    response = requests.get(url)
    data = response.json()

    # Process data, extracting relevant information
    processed_data = {
        item['symbol']: {
            'price': float(item['lastPrice']),
            'change': float(item['priceChangePercent'])
        } for item in data
    }
    return processed_data

@app.route('/')
def index():
    return "Crypto Screener API"

@app.route('/data', methods=['GET'])
def data():
    data = get_crypto_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
