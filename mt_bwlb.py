# -*- encoding: utf-8 -*-
'''
@项目名称：   mt_bwlb.py
@更新时间：   2022/08/01 12:54:51
@版本号  ：   
@环境变量：   
@更新内容：   
'''


import json
import os
import sys
import base64
from time import time
import requests


PROJECT_NAME = "mt_bwlb"


class User():

    def __init__(self,cookie,index) -> None:
        self.cookie = cookie
        self.index = index

    def get(self, url, header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; TAS-AL02 Build/N2G48C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 MMWEBID/840 MicroMessenger/8.0.2.1860(0x28000234) Process/appbrand1 WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 MiniProgramEnv/android",
            "accept-encoding": "gzip, deflate, br",
            "connection": "keep-alive",
            "cookie":self.cookie['cookie']
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
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; TAS-AL02 Build/N2G48C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 MMWEBID/840 MicroMessenger/8.0.2.1860(0x28000234) Process/appbrand1 WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 MiniProgramEnv/android",
            "accept-encoding": "gzip, deflate, br",
            "connection": "keep-alive",
            "cookie":self.cookie['cookie'],
            "Referer": "https://servicewechat.com/wx6132f03005a8082e/13/page-frame.html"
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
    
    def loadData(self):
        url = "https://request.mtgamefruit.com:8023/game/loadData"
        body = {
        "accessToken":{
            "access_token":self.cookie['access_token'],
            "openId":self.cookie['openId']},
        "data":{},
        "tms":int(time()*1000)}
        print(body)
        rjson = self.post(url=url,body=base64.b64encode(json.dumps(body).encode()))
        print(rjson)        

    def login(self):
        url = "https://request.mtgamefruit.com:8023/auth/login"
        body = {
            "accessToken":{"access_token":"","openId":""},
            "data":{
                "channel":"weixin","channelId":"weixin",
                "channelToken":self.cookie['channelToken'],
                "nickName":"momo",
                "avatarUrl":"https://thirdwx.qlogo.cn/mmopen/vi_32/Q3auHgzwzM5NNOOlsKPx4yRydvScQd6yCdic0icaUO06NPLpW22Cdzf6Qia4pnzVk4VQicbOVUib9Y7UvzS8EGVJePA/132",
                "invitationCode":"",
                "isCookieOld":True,"mgcId":""}}
        rjson = self.post(url=url,body=base64.b64encode(json.dumps(body).encode()))
        print(rjson)

    def run(self):
        self.loadData()

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
            {"channelToken": "","remark": ""}]}
        file.write(json.dumps(newContent, indent=2))
        file.close()
    return accountList

if __name__ == "__main__":
    cookies = initEnv()
    users = []
    index = 1
    for cookie in cookies:
        users.append(User(cookie,index))
        index +=1

    for user in users:
        user.run()
    