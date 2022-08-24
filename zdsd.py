
import json
import os
import sys
from xml.dom.expatbuilder import Rejecter
import requests

PROJECT_NAME = "zdsd"


class User:
    def __init__(self, account, index=1) -> None:
        self.account = account
        self.index = index
        self.valid = True

    def get(self, url, header=None, isText=False):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; P40 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.22.2.43 Mobile Safari/537.36 UCBS/3.22.2.43_220223200704 ChannelId(1) NebulaSDK/1.8.100112 Nebula AlipayDefined(nt:WIFI,ws:360|0|2.0) AliApp(AP/10.2.90.8100) AlipayClient/10.2.90.8100 Language/zh-Hans useStatusBar/true isConcaveScreen/false Region/CNAriver/1.0.0",
            "Referer": "https://2021002117637233.hybrid.alipay-eco.com/2021002117637233/0.2.2208111755.38/index.html#pages/navigation/navigation",
            "x-release-type": "ONLINE",
            "alipayMiniMark": "p2U3pO9EH7yd4fH4wSkCIa/5aFgCIp8SKCRjny0IJKt5wXYupISeWdDs5FSrERrHPxSclf0D3Mf3w6Y1Soahv8eV9aK+Tnmfwzv+horfWdo="
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.get(url, headers=headers, timeout=5)
            if(isText):
                return res.text
            else:
                return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    def post(self, url, body='', header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; P40 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.22.2.43 Mobile Safari/537.36 UCBS/3.22.2.43_220223200704 ChannelId(1) NebulaSDK/1.8.100112 Nebula AlipayDefined(nt:WIFI,ws:360|0|2.0) AliApp(AP/10.2.90.8100) AlipayClient/10.2.90.8100 Language/zh-Hans useStatusBar/true isConcaveScreen/false Region/CNAriver/1.0.0",
            "Referer": "https://2021002117637233.hybrid.alipay-eco.com/2021002117637233/0.2.2208111755.38/index.html#pages/navigation/navigation",
            "x-release-type": "ONLINE",
            "alipayMiniMark": "p2U3pO9EH7yd4fH4wSkCIa/5aFgCIp8SKCRjny0IJKt5wXYupISeWdDs5FSrERrHPxSclf0D3Mf3w6Y1Soahv8eV9aK+Tnmfwzv+horfWdo="
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(url, data=body, headers=headers, timeout=5)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def getUserInfo(self):
        url = f"https://www.ketingkeji.com/api/Index/index?access=i20180418&appid=2021002117637233&channel=0&edition=190001&gid=0&postion=1&token={self.account['token']}&userid={self.account['userid']}&yaoqingid=0"
        rjson = self.get(url)
        if(not rjson):
            self.valid = False
            return
        if(rjson['state'] == 1):
            self.coin = rjson['data']['money_zc']
            self.cash = rjson['data']['price_zc']
            print(f"可兑换金币：{self.coin}")
            print(f"可提现余额：{self.cash}")
            print("")
            print(rjson['data']['nickNameMsg'])
            print(f"活跃金币倒计时：{rjson['data']['timeMoney']}s")
            if(rjson['data']['timeMoney'] <= 0):
                self.getTimeMoney()
        else:
            self.valid = False
            print(f"获取信息失败：{rjson['msg']}")

    def getSignInfo(self):
        url = f"https://json.dd-gz.com/zhuandianshidian/public/api.php/integral/sign_list2?access=i20180418&appid=2021002117637233&channel=132&edition=190001&gid=0&postion=1&sign=DQfleO6Tq68u6wy4jrQQ%2FTonTOe6ZKJeBsT1Y0cA8w2kCWLQQaMAxhskm153j%2Fq9cAyio5Zvw%2BpTC4AG%2B14jm%2FYWE3ZuI0HP1%2B27%2Ba4EcdItuX8abfhSU3ffUVBQ2R0QwUw9rUTMdV1Sauek9rMTfWeEYCX1g0mAG2XbqLSAIAc%3D&token={self.account['token']}&userid={self.account['userid']}&yaoqingid=0"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['state'] == 1):
            print(f"今日签到奖励：{rjson['data']['jinri_money']}金币")
            if(rjson['data']['sign'] == 0):
                print("今日未签到")
                self.signIn()
            else:
                print("今日已签到")
        else:
            print(f"获取签到信息失败：{rjson['msg']}")

    def signIn(self):
        url = f"https://json.dd-gz.com/zhuandianshidian/public/api.php/integral/sign?access=i20180418&appid=2021002117637233&edition=190001&token={self.account['token']}&userid={self.account['userid']}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['state'] == 1):
            print(rjson['data']['priceMsg'])
        else:
            print("签到失败："+rjson['msg'])

    def getTimeMoney(self):
        url = f"https://json.dd-gz.com/zhuandianshidian/public/api.php/integral/timeMoney?access=i20180418&appid=2021002117637233&edition=190001&token={self.account['token']}&userid={self.account['userid']}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['state'] == 1):
            print(f"领取活跃奖励成功：{rjson['data']['price']}")
        else:
            print(f"领取活跃奖励失败：{rjson['msg']}")

    def addMoney(self,price):
        url = f"https://json.dd-gz.com/zhuandianshidian/public/api.php/user/addMoney?access=i20180418&appid=2021002117637233&edition=190001&price={price}&token={self.account['token']}&userid={self.account['userid']}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['state'] == 1):
            print("金币兑换现金成功")
        else:
            print(f"金币兑换现金失败：{rjson['msg']}")

    def run(self):
        print(f"======账号[{self.index}]======")
        if(self.account["remark"]):
            print(f"账号备注：{self.account['remark']}")
        self.getUserInfo()
        if(not self.valid):
            return
        print("")
        self.getSignInfo()
        if(self.coin >= 998):
            self.addMoney(self.coin)
        print("\n")


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
            {"remark": "", "token": "", "userid": ""}]}
        file.write(json.dumps(newContent, indent=2))
        file.close()
    return accountList


if __name__ == "__main__":
    accounts = initEnv()
    users = []
    index = 1
    for account in accounts:
        if("token" in account and "userid" in account):
            users.append(User(account, index))
            index += 1

    for user in users:
        user.run()
