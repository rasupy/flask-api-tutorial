# flask-api-tutorial
```t
# FlaskAPIの学習用リポジトリ
バックエンド開発を学習する為に作成
```
```python
# main.py（APIの雛形）
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# サンプルデータ
todos = [{"id": 1, "task": "DockerでFlask API起動", "done": False}]

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    new_todo = request.json
    todos.append({"id": len(todos) + 1, "task": new_todo["task"], "done": False})
    return jsonify({"message": "Todo追加成功"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```