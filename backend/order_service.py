from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

PRODUCT_SERVICE_URL = "http://product:5001"
PAYMENT_SERVICE_URL = "http://payment:5003"

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Order Service is running"})

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    product_response = requests.get(
        f"{PRODUCT_SERVICE_URL}/products"
    )

    products = product_response.json()
    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if not product:
        return jsonify({"error": "Product not found"}), 404

    total = product["price"] * quantity

    payment_response = requests.post(
        f"{PAYMENT_SERVICE_URL}/pay",
        json={"amount": total}
    )

    return jsonify({
        "message": "Order created successfully",
        "product": product["name"],
        "quantity": quantity,
        "total": total,
        "payment": payment_response.json()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)