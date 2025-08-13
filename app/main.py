from flask import Flask, jsonify, request
from flask_cors import CORS  # type: ignore

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_flask():
    message = "Hello, Flask!"
    return jsonify(message=message)


# サンプルデータ
tasks = [{"id": 1, "title": "Pythonの学習"}]


@app.route("/tasks", methods=["POST"])
def add_task():
    new_task = request.json
    # ここでタスクを追加する処理を実装
    tasks.append({"id": len(tasks) + 1, "title": new_task["title"]})
    return jsonify(tasks), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    # ここでタスクを取得する処理を実装
    return jsonify(tasks), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks[:] = [task for task in tasks if task["id"] != task_id]
    return jsonify(tasks), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
