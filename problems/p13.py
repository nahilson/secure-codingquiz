import sqlite3
import traceback
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/member")
def member():
    member_id = request.args.get("id", "")
    try:
        conn = sqlite3.connect("members.db")
        row = conn.execute(
            "SELECT name, email FROM members WHERE id = ?", (member_id,)
        ).fetchone()
        conn.close()
        return jsonify({"name": row[0], "email": row[1]})
    except Exception as e:
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500


if __name__ == "__main__":
    app.run()
