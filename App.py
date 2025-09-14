from flask import Flask, request, jsonify

app = Flask(__name__)

contador = {"valor": 0}

@app.get("/contador")
def get_contador():
    return jsonify(contador)

@app.post("/contador")
def post_contador():
    data = request.get_json(silent=True) or {}
    if "valor" in data and isinstance(data["valor"], int):
        contador["valor"] = data["valor"]
    if "sumar" in data and isinstance(data["sumar"], int):
        contador["valor"] += data["sumar"]
    return jsonify(contador), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
