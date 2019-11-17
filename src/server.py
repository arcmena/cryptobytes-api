from flask import Flask, json, jsonify, request
import requests

app = Flask('__name__')

r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
coins = r.json()

@app.route('/coin')
def home():
    return jsonify(coins), 200

@app.route('/coin/<string:id>', methods=['GET'])
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