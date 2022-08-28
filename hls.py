import os
from time import sleep
import requests

COOKIE_NAME = "hlsToken"

proxies = None

class User:
    def __init__(self,token,index=1) -> None:
        self.token = token
        self.index = index
        self.valid = True

    def get(self, url, header=None):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; P40 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/24.0)",
            "token": self.token
        }
        if(header):
            headers.update(header)
        try:
            res = requests.get(url, headers=headers)
            if(res.status_code == 200):
                return res.json()
            else:
                return None
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    def post(self, url, body='', header=None):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; P40 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/24.0)",
            "token": self.token
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(url, data=body,headers=headers,proxies=proxies)
            if(res.status_code == 200):
                return res.json()
            else:
                return None
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None
    
    def getUserInfo(self):
        url = "http://api.hls178.cn:8080/user/info"
        rjson = self.get(url)
        if(not rjson):
            self.valid = False
            return
        if(rjson['code'] == 0):
            self.money = rjson['data']['money']
            self.hasParent = rjson['data']['hasParent']
            print(f"手机号码：{rjson['data']['mobile']}")
            print(f"积累金币：{rjson['data']['historyMoney']}")
            print(f"可用金币：{rjson['data']['money']}")
            if(rjson['data']['hasParent']):
                print("邀请状态：已绑定上级")
            else:
                print("邀请状态：未绑定上级")
            if(rjson['data']['alipay']):
                self.bindCash = True
                print(f"支付宝账号：{rjson['data']['alipay']}")
                print(f"支付宝用户：{rjson['data']['alipayRealName']}")
            else:
                self.bindCash = False
                print("未绑定支付宝，无法提现")
        else:
            self.valid = False
            print(f"获取用户信息失败：{rjson['message']}")

    def advertiseInfo(self):
        for id in [1,2]:
            url = f"http://api.hls178.cn:8080/advertise?id={id}"
            rjson = self.get(url)
            if(not rjson):
                continue
            if(rjson['code'] == 0):
                acceptable = rjson['data']['acceptable']
                countdown = rjson['data']['countdown']
                if(acceptable):
                    print(f"任务[{id}]未领取")
                    self.advertiseDouble(id)
                    flag = self.advertiseAccept(id)
                    if(flag):
                        self.advertiseProcess(id,4)
                else:
                    if(countdown > 0):
                        print(f"任务[{id}]已领取奖励，等待冷却")
                        print(f"任务[{id}]冷却时间：{countdown}s")
                    else:
                        print(f"任务[{id}]已领取")
                        user = rjson['data']['user']
                        currentTimes = user['currentTimes']
                        if(currentTimes >= 4):
                            print(f"任务[{id}]可领取奖励")
                        else:
                            print(f"任务[{id}]当前已执行次数：{currentTimes}")
                            self.advertiseProcess(id,4)
            else:
                print(f"获取任务[{id}]信息失败：{rjson['message']}")

    def advertiseAccept(self,id):
        url = f"http://api.hls178.cn:8080/advertise/accept"
        body = f"awardType=1&id={id}"
        rjson = self.post(url,body=body)
        if(not rjson):
            return False
        if(rjson['code'] == 0):
            print(f"任务[{id}]领取成功")
            return True
        else:
            print(f"任务[{id}]领取失败：{rjson['message']}")
            return False

    def advertiseProcess(self,id,count):
        url = "http://api.hls178.cn:8080/advertise/process"
        body = f"id={id}"
        for i in range(count):
            rjson = self.post(url,body=body)
            if(not rjson):
                continue
            if(rjson['code'] == 0):
                print(f"任务[{id}]执行成功,等待3s...")
                sleep(3)
            else:
                print(f"任务[{id}]执行失败：{rjson['message']}")

    def advertiseDouble(self,id):
        url = "http://api.hls178.cn:8080/advertise/awardDouble"
        body = f"id={id}"
        self.post(url=url,body=body)

    def cash(self,money):
        url = "http://api.hls178.cn:8080/user/cash"
        body = f"money={money}"
        rjson = self.post(url,body=body)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"提现成功：+{money/100}元")
        else:
            print(f"提现失败：{rjson['message']}")

    def run(self):
        print(f"======账号[{self.index}]======")
        self.getUserInfo()
        if(not self.valid):
            return
        print("")
        self.advertiseInfo()
        print("")
        if(self.bindCash and self.money >= 10):
            self.cash(self.money)
        print("\n")

def initEnv():
    env = os.environ
    if(COOKIE_NAME in env):
        cookies = env[COOKIE_NAME]
        if(cookies.find("&")):
            return cookies.split("&")
    res = []
    res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjQxMDQsImV4cCI6MTY5Mjk2MDExOCwiaXNzIjoiaHpxIn0.cHuEhdwsoLwflSGu6JgTT1wzKBcp0rwwv8qEG5pJDjY")
    res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjI5ODcsImV4cCI6MTY5MjkzNjgwMiwiaXNzIjoiaHpxIn0.bhh0M9vRmT9VwowsBdyMNLLF8jvE21XgCyw9CDmpKBY")
    res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjIxODQsImV4cCI6MTY5MjkzMDYwNywiaXNzIjoiaHpxIn0.3COVDlgEyKUnPVZZaWNPV8o1dBLHxDAdno0UBFJ7y-s")
    res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjM3ODAsImV4cCI6MTY5Mjk1NDM1MCwiaXNzIjoiaHpxIn0.JkqwpAqT7o15rUGS7wvuDO7hdBerqdF_pz9-Eq8B72w")
    res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjY0NTcsImV4cCI6MTY5MzExMDg0MSwiaXNzIjoiaHpxIn0.Xc8lXYafL0BwNFymSeDqAVZm7Y2D--owRh0GjVyNuNU")
    res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjY0NTUsImV4cCI6MTY5MzExMTQzMiwiaXNzIjoiaHpxIn0.M7iUhzu5VsA7zsw2-qpvhLPOdFROAvp_QsY1cA2cEqE")
    return res


if __name__ == "__main__":
    datas = initEnv()
    users = []
    index = 1
    for data in datas:
        users.append(User(data, index))
        index +=1
    for user in users:
        try:
            user.run()
        except Exception as e:
            print("运行异常：", str(e))
