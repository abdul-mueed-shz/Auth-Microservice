import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(data, key, iv):
    data = pad(data.encode(), 16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    return base64.b64encode(cipher.encrypt(data))


def decrypt(enc, key, iv):
    enc = base64.b64decode(enc)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    return unpad(cipher.decrypt(enc), 16)
