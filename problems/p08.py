import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

PAYMENT_KEY = b"Sup3rS3cretKey!!"


def encrypt_card_number(card_number: str) -> str:
    iv = get_random_bytes(16)
    cipher = AES.new(PAYMENT_KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(card_number.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted).decode()


def decrypt_card_number(token: str) -> str:
    raw = base64.b64decode(token)
    iv, body = raw[:16], raw[16:]
    cipher = AES.new(PAYMENT_KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(body), AES.block_size).decode()


def mask(card_number: str) -> str:
    return "*" * (len(card_number) - 4) + card_number[-4:]
