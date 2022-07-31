# -*- encoding: utf-8 -*-
'''
@项目名称：   meituan.py
@更新时间：   2022/07/31 10:15:12
@版本号  ：   
@环境变量：   
@更新内容：   
'''

import json
import os
import sys

import requests


PROJECT_NAME = "meituan"


class User:
    def get(self, url, header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; TAS-AL00 Build/N2G48C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 MMWEBID/4561 MicroMessenger/8.0.2.1860(0x28000234) Process/appbrand0 WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 MiniProgramEnv/android",
            "referer": "https://servicewechat.com/wxde8ac0a21135c07d/1011/page-frame.html",
            "m-appkey": "wxmp_mt-weapp",
            "accept-encoding": "gzip, deflate, br",
            "connection": "keep-alive",
            "token": self.cookie['token']
        }
        if(header):
            headers.update(header)
        try:
            res = requests.get(url, headers=headers)
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    def post(self, url, body='', header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; TAS-AL00 Build/N2G48C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 MMWEBID/4561 MicroMessenger/8.0.2.1860(0x28000234) Process/appbrand0 WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 MiniProgramEnv/android",
            "referer": "https://servicewechat.com/wxde8ac0a21135c07d/1011/page-frame.html",
            "m-appkey": "wxmp_mt-weapp",
            "accept-encoding": "gzip, deflate, br",
            "connection": "keep-alive",
            "token": self.cookie['token']
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(url, data=body, headers=headers)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def __init__(self, cookie, index=1) -> None:
        self.cookie = cookie
        self.index = index
        self.valid = True

    def userInfo(self):
        url = f"https://web.meituan.com/web/user/points?token={self.cookie['token']}&userId={self.cookie['userId']}"
        print(url)
        rjson = self.get(url)
        print(rjson)

    def run(self):
        self.userInfo()


def initEnv() -> list:
    accountList = []
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\{0}.json".format(PROJECT_NAME)
    else:
        filePath += "/{0}.json".format(PROJECT_NAME)
    # 读写配置
    if(os.path.isfile(filePath)):
        file = open(filePath, "r", encoding="utf-8")
        content = file.read()
        file.close()
        accountList = json.loads(content)['accounts']
    else:
        file = open(filePath, "w+", encoding="utf-8")
        newContent = {"accounts": [
            {"token": "", "userId": "", "uuid": "", "remark": ""}]}
        file.write(json.dumps(newContent, indent=2))
        file.close()
    return accountList


if __name__ == "__main__":
    cookies = initEnv()
    users = []
    index = 1
    for cookie in cookies:
        users.append(User(cookie, index=index))
        index += 1

    for user in users:
        user.run()
