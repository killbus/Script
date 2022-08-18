import base64
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


def getProxies():
    cliper = AESCipher()
    url = "https://config.v2cross.com/profiles/encryptcfg"
    res = requests.get(url,timeout=20)
    data = res.text
    proxies = cliper.decrypt(data).split("\n")
    res = []
    for proxy in proxies:
        print(proxy)
        if(proxy.find("ss://") == 0):
            proxy = proxy.split("ss://",2)[1]
            if(proxy.find("@") > -1):
                proxy = proxy.split("@",2)[0]
            if(proxy.find("#") > -1):
                proxy = proxy.split("#",2)[0]
            proxy = base64.decodebytes(proxy.encode()).decode("utf-8")
            if(proxy.find("@") == -1):
                continue
            proxy = proxy.split("@")
            proxy = proxy[len(proxy)-1]
            if(proxy.find(":") == -1):
                continue
            proxy = proxy.split(":")
            res.append({"ip":proxy[0],"port":proxy[1]})
    return res

url = "http://www.baidu.com"
proxies = getProxies()
exit()
for proxy in proxies:
    try:
        p = {"http":f"socks5h://{proxy['ip']}:{proxy['port']}","https":f"socks5h://{proxy['ip']}:{proxy['port']}"}
        res = requests.get(url,timeout=1,proxies=p)
        print(res.text)
        exit()
    except Exception as e:
        print(f"======{proxy['ip']}:{proxy['port']}======")
        print(str(e))
