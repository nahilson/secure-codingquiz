import hashlib
import hmac
import sqlite3

DB_PATH = "users.db"


def check_password(stored_hash, salt, password):
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
    return hmac.compare_digest(digest, stored_hash)


def login(username, password):
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT pw_hash, salt FROM users WHERE username = ?", (username,)
    ).fetchone()
    conn.close()
    if row is None:
        return False
    return check_password(row[0], row[1], password)


def handle_login_request(form):
    username = form.get("username", "")
    password = form.get("password", "")
    if login(username, password):
        return {"ok": True}
    return {"ok": False, "message": "로그인 실패"}
