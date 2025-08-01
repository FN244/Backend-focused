from flask import Flask, request, jsonify

app = Flask(__name__)

orders = {}

@app.route('/orders', methods=['POST'])
def create_order():
    order_id = len(orders) + 1
    order_data = request.json
    orders[order_id] = order_data
    return jsonify({'order_id': order_id}), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    if order_id in orders:
        orders[order_id].update(request.json)
        return jsonify(orders[order_id]), 200
    return jsonify({'error': 'Order not found'}), 404

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    if order_id in orders:
        return jsonify(orders[order_id]), 200
    return jsonify({'error': 'Order not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)