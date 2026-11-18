from flask import Flask, request, jsonify

app = Flask(__name__)

current_user = None
current_cart = []

CARTS = {"kim": ["notebook"], "lee": ["monitor", "keyboard"]}


def load_cart(username):
    return list(CARTS.get(username, []))


@app.route("/login", methods=["POST"])
def login():
    global current_user, current_cart
    current_user = request.form["username"]
    current_cart = load_cart(current_user)
    return jsonify({"ok": True})


@app.route("/cart")
def cart():
    return jsonify({"user": current_user, "items": current_cart})


if __name__ == "__main__":
    app.run(threaded=True)
