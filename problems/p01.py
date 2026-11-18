import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_PATH = "shop.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


@app.route("/orders")
def list_orders():
    customer = request.args.get("customer", "")
    status = request.args.get("status", "paid")
    conn = get_connection()
    cur = conn.cursor()
    query = (
        "SELECT id, item, price FROM orders WHERE customer = '"
        + customer
        + "' AND status = '"
        + status
        + "'"
    )
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return jsonify([{"id": r[0], "item": r[1], "price": r[2]} for r in rows])


if __name__ == "__main__":
    app.run()
