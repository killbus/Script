# -*- encoding: utf-8 -*-

import requests
import os.path
import json
from time import sleep

COOKIE_NAME = "ksptbCookie"

requests.packages.urllib3.disable_warnings()

class User:

    def __init__(self,cookie,index=1) -> None:
        self.cookie = cookie
        self.valid = True
        self.index = index

    # 统一GET 额外header用字典传递
    def get(self, url, header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; VCE-AL00 Build/HUAWEIVCE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.469 (rel;r) Mobile Safari/537.36 Yoda/2.8.1-rc3 Kwai/10.3.20.24977",
            "cookie": self.cookie
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.get(url, headers=headers,verify=False)
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    # 统一POST 额外header用字典传递
    def post(self, url, body='', header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; VCE-AL00 Build/HUAWEIVCE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.469 (rel;r) Mobile Safari/537.36 Yoda/2.8.1-rc3 Kwai/10.3.20.24977",
            "cookie": self.cookie
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(url, data=body, headers=headers,verify=False)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    # 主页
    def home(self):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/home"
        rjson = self.get(url)
        if(not rjson):
            self.valid = False
            return
        self.basicInfo = {}
        if(rjson['result'] == 1):
            self.valid = True
            self.basicInfo['cash'] = rjson['data']['cash']
            self.basicInfo['coin'] = rjson['data']['coin']
            print(f"金币余额：{rjson['data']['coin']}")
            print(f"现金余额：{rjson['data']['cash']}¥")
        else:
            self.valid = False
            print("登录失败：{0}".format(rjson['error_msg']))

    # 签到信息
    def signInfo(self):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/signIn/info"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            # 普通金币签到
            if("tasks" in rjson['data'] and not rjson['data']['todaySignInCompleted']):
                print("金币签到：未签到")
                self.sign(0)
            else:
                print("金币签到：已签到")
        else:
            print("获取签到信息失败：{0}".format(rjson['error_msg']))

    #签到
    def sign(self, id):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/signIn/report"
        body = {"signInBizId": id}
        header = {"content-type": "application/json"}
        rjson = self.post(url, body=json.dumps(body), header=header)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            print("今日金币签到成功")
        else:
            print("今日金币签到失败：{0}".format(rjson['error_msg']))

    # 获取宝箱信息 如果可开启则开启 开启宝箱后还需查询一次宝箱信息来激活宝箱
    def getBoxInfo(self):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/treasureBox/info"
        rjson = self.get(url)
        if(not rjson or not rjson['data']):
            return
        if(rjson['result'] == 1):
            print(f"宝箱总额：{rjson['data']['treasureRewardAmountEveryDay']}")
            status = rjson['data']['status']
            # status 2领取中 3冷却完成 4次数已完
            if(status == 4):
                print("宝箱冷却时间：开启次数已满，明日再来!")
            elif(status == 3):
                print("宝箱冷却时间：{0}s".format(rjson['data']['treasureCurrentTaskRemainSeconds']))
                self.openBox(rjson['data']['token'])
                sleep(0.1)
                # 激活宝箱
                self.getBoxInfo()
            elif(status == 2):
                print(f"宝箱冷却时间：{rjson['data']['treasureCurrentTaskRemainSeconds']}s")
        else:
            print("获取宝箱信息失败：{0}".format(rjson['error_msg']))

    # 开启宝箱
    def openBox(self, token):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/treasureBox/report"
        body = {"taskToken": token}
        rjson = self.post(url, body=json.dumps(body))
        if(not rjson):
            return
        if(rjson['result'] == 1):
            print("开启宝箱成功：获得{0}金币".format(rjson['data']['rewardCount']))
        else:
            print("开启宝箱失败：{0}".format(rjson['error_msg']))

    def run(self):
        print(f"=====账号[{self.index}]=====")
        self.home()
        if(self.valid):
            self.signInfo()
            self.getBoxInfo()
            print("")

def initEnv():
    env = os.environ
    if(COOKIE_NAME in env):
        cookies = env[COOKIE_NAME]
        if(cookies.find("&")):
            return cookies.split("&")
    return []


if __name__ == "__main__":
    users = []
    cookies = initEnv()
    index = 1
    for cookie in cookies:
        users.append(User(cookie,index))
        index +=1
    for user in users:
        user.run()