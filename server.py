from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"

# データファイルがなければ作成
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)


@app.route("/add", methods=["POST"])
def add_marker():
    data = request.json

    # JSON 読み込み
    with open(DATA_FILE, "r") as f:
        markers = json.load(f)

    # 新しいデータを追加
    markers.append(data)

    # JSON 保存
    with open(DATA_FILE, "w") as f:
        json.dump(markers, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "ok"})


@app.route("/list", methods=["GET"])
def list_markers():
    with open(DATA_FILE, "r") as f:
        markers = json.load(f)
    return jsonify(markers)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
