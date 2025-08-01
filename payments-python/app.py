from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for payment history
payments = []

@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.json
    payments.append(data)  # Save payment data
    return jsonify({"message": "Payment processed", "data": data}), 201

@app.route('/payment_history', methods=['GET'])
def payment_history():
    return jsonify(payments), 200

if __name__ == '__main__':
    app.run(debug=True)