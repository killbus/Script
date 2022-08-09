import socket
from Crypto.Cipher import AES
from base64 import b64decode, b64encode
import socks
from requests import request
import requests

BLOCK_SIZE = AES.block_size


class AESCipher:

    def __init__(self):
        self.key = "8YfiQ8wrkziZ5YFa"
        self.iv = "8YfiQ8wrkziZ5YFa"

    @staticmethod
    def pad(text):
        return text + (BLOCK_SIZE - len(text.encode()) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(text.encode()) % BLOCK_SIZE)

    @staticmethod
    def un_pad(text):
        return text[:-ord(text[len(text) - 1:])]

    # 加密
    def encrypt(self, text):
        text = self.pad(text).encode()
        cipher = AES.new(key=self.key.encode(),
                         mode=AES.MODE_CBC, IV=self.iv.encode())
        encrypted_text = cipher.encrypt(text)
        return b64encode(encrypted_text).decode('utf-8')

    # 解密
    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        cipher = AES.new(key=self.key.encode(),
                         mode=AES.MODE_CBC, IV=self.iv.encode())
        decrypted_text = cipher.decrypt(encrypted_text)
        return self.un_pad(decrypted_text).decode('utf-8')

cliper = AESCipher()
url = "https://config.v2cross.com/profiles/encryptcfg"
res = requests.get(url,timeout=20)
data = res.text
proxies = cliper.decrypt(data).split("\n")
print("本次更新：",len(proxies))
for proxy in proxies:
    print(proxy)
