from flask import Flask, jsonify, request

app = Flask(__name__)
products = []

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

@app.route('/products', methods=['POST'])
def create_product():
    product = request.json
    products.append(product)
    return jsonify(product), 201

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return jsonify(product), 200 if product else 404

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        product.update(request.json)
        return jsonify(product), 200
    return jsonify({'error': 'Product not found'}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p['id'] != product_id]
    return jsonify({'result': True}), 200

if __name__ == '__main__':
    app.run(debug=True)