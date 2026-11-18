import base64
import os
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def load_key() -> bytes:
    return os.environ["APP_PHONE_KEY"].encode()[:8]


def encrypt_phone(phone: str) -> str:
    cipher = DES.new(load_key(), DES.MODE_ECB)
    padded = pad(phone.encode(), DES.block_size)
    return base64.b64encode(cipher.encrypt(padded)).decode()


def decrypt_phone(token: str) -> str:
    cipher = DES.new(load_key(), DES.MODE_ECB)
    raw = cipher.decrypt(base64.b64decode(token))
    return unpad(raw, DES.block_size).decode()


def format_phone(phone: str) -> str:
    digits = "".join(ch for ch in phone if ch.isdigit())
    return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
