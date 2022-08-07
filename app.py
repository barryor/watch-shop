from flask import Flask, jsonify, request
from business_logic import checkout

app = Flask(__name__)


@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.get_json()
    total_price = checkout.calculate_total(data)

    if total_price is None:
        return jsonify({'error': 'checkout-0001',
                        'message': 'There was an error calculating total price',
                        'detail': 'Check request was formatted correctly with valid IDs'
                        }), 400
    else:
        return jsonify({'price': total_price}), 200


if __name__ == '__main__':
    app.run()
