from flask import Flask, jsonify, request
from flask_cors import CORS  # type: ignore

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_flask():
    message = "Hello, Flask!"
    return jsonify(message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
