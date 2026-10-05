from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Headphones", "price": 2000},
    {"id": 3, "name": "Keyboard", "price": 1500}
]

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Product Service is running"})

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)