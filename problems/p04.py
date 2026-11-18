import os
from flask import Flask, request

app = Flask(__name__)
UPLOAD_DIR = "/var/www/static/uploads"
MAX_BYTES = 5 * 1024 * 1024
app.config["MAX_CONTENT_LENGTH"] = MAX_BYTES


@app.route("/profile/photo", methods=["POST"])
def upload_photo():
    f = request.files.get("photo")
    if f is None or f.filename == "":
        return "no file", 400
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    save_path = os.path.join(UPLOAD_DIR, f.filename)
    f.save(save_path)
    return "/static/uploads/" + f.filename, 201


@app.route("/profile/photo/<name>", methods=["DELETE"])
def delete_photo(name):
    target = os.path.join(UPLOAD_DIR, os.path.basename(name))
    if os.path.exists(target):
        os.remove(target)
    return "", 204
