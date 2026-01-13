from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)

DATA_FILE = "data.json"

# データファイルがなければ作成
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)


@app.route("/add", methods=["POST"])
def add_marker():
    data = request.json

    with open(DATA_FILE, "r") as f:
        markers = json.load(f)

    markers.append(data)

    with open(DATA_FILE, "w") as f:
        json.dump(markers, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "ok"})


@app.route("/list", methods=["GET"])
def list_markers():
    with open(DATA_FILE, "r") as f:
        markers = json.load(f)
    return jsonify(markers)


# ★ index.html を返すルート
@app.route("/")
def index():
    return send_from_directory("static", "index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
