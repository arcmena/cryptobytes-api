from flask import Flask, json, jsonify, request
import requests
from flask_cors import CORS, cross_origin

app = Flask('__name__')
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
coins = r.json()

@app.route('/')
@cross_origin()
def init():
    return jsonify({
        "ok": "true"
    })

@app.route('/coin')
@cross_origin()
def home():
    return jsonify(coins), 200

@app.route('/coin/<string:id>', methods=['GET'])
@cross_origin()
def searchOne(id):
    show = [obj for obj in coins if obj['id'] == id]
    show = show[0]
    if not show: return jsonify({'error' : 'not found'}), 404
    return jsonify({
        'id': show['id'],
        'name': show['name'],
        'price_usd': show['price_usd'],
        'price_btc': show['price_btc']
    }), 200

@app.route('/coin/topten', methods=['GET'])
@cross_origin()
def showTop():
    top = []
    i = 0
    while i < 10:
        top.append({
            'id': coins[i]['id'],
            'name': coins[i]['name'],
            'price_usd': coins[i]['price_usd'],
            'price_btc': coins[i]['price_btc']
        })
        i += 1
    return jsonify(top)

if __name__ == '__main__':
    app.run(debug=True)