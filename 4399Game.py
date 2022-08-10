
from math import fabs
import os
import requests
import json


COOKIE_NAME = "4399Headers"


class User:
    def __init__(self,header,index) -> None:
        self.header = self.parseHeaders(header)
        self.index = index

    def get(self, url, header=None):
        headers = self.header.copy()
        if(header):
            headers.update(header)
        try:
            res = requests.get(url, headers=headers)
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    def post(self, url, body='', header=None):
        headers = headers = self.header.copy()
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(url, data=body, headers=headers)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def parseHeaders(self,str):
        res = {}
        headers = str.split("\n")
        for hs in headers:
            hs = hs.split(":")
            if(len(hs) == 2 and hs[1].strip()):
                res[hs[0]] = hs[1].strip()
        res.pop("Content-Length","")
        return res

    def centerIndex(self):
        url = "https://mapi.yxhapi.com/user/task/box/android/v2.1/center-index.html"
        rjson = self.post(url)
        if(not rjson):
            self.valid = False
        if(rjson['code'] == 100):
            self.valid = True
            userInfo = rjson['result']['user_info']
            print(f"用户ID：{userInfo['pt_uid']}")
            print(f"普通盒币：{userInfo['hebi']} ≈ {userInfo['hebi']/100}元")
            print(f"超级盒币：{userInfo['super_hebi']}")
            sign = rjson['result']['sign']
            print(f"积累签到天数：{sign['total_signed']}")
            print(f"周期签到天数：{sign['signed_day']}\n")
            if(sign['today_signed']):
                print("今日已签到")
            else:
                print("今日未签到")
            daily = rjson['result']['daily']
            if(daily['unlock']):
                print("今日任务未解锁")
            else:
                print("今日任务已解锁")
        else:
            self.valid = False
            print("账号异常："+rjson['message'])
        print(json.dumps(rjson,indent=2))

    def run(self):
        print(f"======账号[{self.index}]======")
        self.centerIndex()

def initEnv():
    env = os.environ
    env[COOKIE_NAME] = '''mauth: 0b4538bf7a9dc3f083ee0e1575b7e55e
mareacode: 440100
zxaid: A01-itPJ%2B%2Bg%2FgN855oceHJm1Odpg%2FYk%2FT6ZS
mauthcode: 12b8da274|6be278bc780caca6f886c6c34f5ccccb|3303007075
SM-DEVICEID: 20220809141325e003faf6ef8c79d35d70564e67ae6d74010942b021997e03
m-id: B0%3A12%3A69%3A69%3A25%3A9E
a-id: 7A962E41866879B2
e-id: 
User-Agent: 4399GameCenter/6.8.0.59(android;P40;7.1.2;720x1184;WIFI;1791.840;baidu)
mdeviceId: B0:12:69:69:25:9E
pauth: 3303007075%7C14767929623%7Cc17e20c7129f7c4b162fe4580b546ac5%7C1660032882%7C10001%7Cc942ee14b99db8674b5c3dd9d261ba8d%7C0
s-id: 
mudid: 1103gKwPpiHUAcWIdHsXeee3b
Content-Type: application/x-www-form-urlencoded
Content-Length: 140
Host: mapi.yxhapi.com
Connection: Keep-Alive
Accept-Encoding: gzip
'''
    if(COOKIE_NAME in env):
        cookies = env[COOKIE_NAME]
        if(cookies.find("&")):
            return cookies.split("&")
    return []

if __name__ == "__main__":
    accounts = initEnv()
    users = []
    index = 1
    for account in accounts:
        users.append(User(account,index))
        index += 1

    for user in users:
        user.run()
