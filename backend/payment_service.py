from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Payment Service is running"})

@app.route("/pay", methods=["POST"])
def process_payment():
    data = request.get_json()
    amount = data.get("amount", 0)

    return jsonify({
        "message": "Payment successful",
        "amount": amount
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)