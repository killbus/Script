import hashlib
import os
from random import randint
from time import sleep, time
import requests

from SQLHelper import SQLHelper


COOKIE_NAME = "hlsToken"
cashTime = 12
database = "resource"
host = "81.68.247.240"
user = "resource"
password = "cTAenenXhFNHyk7x"


class User:
    def __init__(self, token, index=1) -> None:
        self.token = token
        self.index = index
        self.valid = True
        self.proxies = self.getProxies()

    def getProxies(self):
        result = []
        try:
            db = SQLHelper(database=database, host=host,
                           user=user, password=password)
            fields = ["ip", "port"]
            cls = db.setTable("proxies").setFields(fields).query()
            db.close()
            for cl in cls:
                url = f"http://{cl[0]}:{cl[1]}"
                result.append({"http": url, "https": url})
            result.append(None)
            return result
        except Exception as e:
            print(f"获取代理失败：{str(e)}")
            result.append(None)
            return result

    def get(self, url, header=None):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; P40 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/24.0)",
            "token": self.token
        }
        if(header):
            headers.update(header)
        try:
            res = requests.get(url, headers=headers, timeout=5)
            if(res.status_code == 200):
                return res.json()
            else:
                return None
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    def post(self, url, body='', header=None, proxies=None):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; P40 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/24.0)",
            "token": self.token
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(
                url, data=body, headers=headers, proxies=proxies, timeout=5)
            if(res.status_code == 200):
                return res.json()
            else:
                return None
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def sign(self, data):
        md5Salt = "!@#ecommerce%^"
        data += f"&key={md5Salt}"
        md5 = hashlib.md5()
        md5.update(data.encode())
        return md5.hexdigest()

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
        for id in [1, 2, 3, 4, 5]:
            url = f"http://api.hls178.cn:8080/advertise?id={id}"
            rjson = self.get(url)
            if(not rjson):
                continue
            if(rjson['code'] == 0):
                if(not rjson['data']):
                    continue
                acceptable = rjson['data']['acceptable']
                countdown = rjson['data']['countdown']
                self.advertiseAward(id)
                if(acceptable):
                    print(f"任务[{id}]未领取")
                    if(id > 3):
                        flag = self.advertiseAccept(id,2)
                    else:
                        flag = self.advertiseAccept(id,1)
                
                    if(flag):
                        self.advertiseProcess(id, 4)
                else:
                    user = rjson['data']['user']
                    if(countdown > 0):
                        print(f"任务[{id}]已领取奖励，等待冷却")
                        print(f"任务[{id}]冷却时间：{countdown}s")
                    else:
                        print(f"任务[{id}]已领取")

                        currentTimes = user['currentTimes']
                        if(currentTimes >= 4):
                            print(f"任务[{id}]可领取奖励")
                        else:
                            print(f"任务[{id}]当前已执行次数：{currentTimes}")
                            self.advertiseProcess(id, 4)
                        code = user['code']
                        awardType = user['awardType']
                        self.advertiseFinish(id, code, awardType)
            else:
                print(f"获取任务[{id}]信息失败：{rjson['message']}")

    def advertiseAccept(self, id,awardType =1):
        url = f"http://api.hls178.cn:8080/advertise/accept"
        body = f"awardType={awardType}&id={id}"
        # 使用代理进行请求
        proxies = self.proxies[randint(0, len(self.proxies)-1)]
        rjson = self.post(url, body=body, proxies=proxies)
        if(not rjson):
            return False
        if(rjson['code'] == 0):
            print(f"任务[{id}]领取成功")
            return True
        else:
            print(f"任务[{id}]领取失败：{rjson['message']}")
            return False

    def advertiseProcess(self, id, count):
        url = "http://api.hls178.cn:8080/advertise/process"
        body = f"id={id}"
        for i in range(count):
            rjson = self.post(url, body=body)
            if(not rjson):
                continue
            if(rjson['code'] == 0):
                print(f"任务[{id}]执行成功,等待1s...")
                sleep(1)
            else:
                print(f"任务[{id}]执行失败：{rjson['message']}")

    def advertiseFinish(self, id, code, awardType):
        url = "http://api.hls178.cn:8080/advertise/finish"
        ts = int(time()*1000)
        data = f"awardType={awardType}&code={code}&time={ts}"
        sign = self.sign(data)
        body = data+f"&sign={sign}"
        rjson = self.post(url, body=body)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"任务[{id}]提交成功")
            sleep(1)
            self.advertiseAward(id)
        else:
            print(f"任务[{id}]提交失败：{rjson['message']}")

    def advertiseAward(self, id):
        url = "http://api.hls178.cn:8080/advertise/award"
        body = f"id={id}"
        rjson = self.post(url=url, body=body)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"任务[{id}]领取奖励成功")
            sleep(1)
            self.advertiseDouble(id)
        else:
            print(f"任务[{id}]领取奖励失败：{rjson['message']}")

    def advertiseDouble(self, id):
        url = "http://api.hls178.cn:8080/advertise/awardDouble"
        body = f"id={id}"
        rjson = self.post(url=url, body=body)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"任务[{id}]领取额外奖励成功")
        else:
            print(f"任务[{id}]领取额外奖励失败：{rjson['message']}")

    def ticketInfo(self):
        url = "http://api.hls178.cn:8080/ticket"
        rjson = self.get(url=url)
        if(not rjson):
            self.ticketValid = False
            return
        if(rjson['code'] == 0):
            print(f"积累门票：{rjson['data']['historyNumber']}张")
            print(f"当前门票：{rjson['data']['number']}张")
            self.ticketValid = True
        else:
            self.ticketValid = False
            print(f"获取抽奖信息失败：{rjson['message']}")

    def ticketSignInfo(self):
        url = "http://api.hls178.cn:8080/sign/index"
        rjson = self.get(url=url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"签到天数：{rjson['data']['days']}")
            if(rjson['data']['signed']):
                print("今日已签到")
            else:
                print("今日未签到")
                self.ticketSign()
        else:
            print(f"获取抽奖签到信息失败：{rjson['message']}")

    def ticketSign(self):
        url = "http://api.hls178.cn:8080/sign"
        rjson = self.post(url=url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"签到成功：+{rjson['data']['number']}张")
        else:
            print(f"签到失败：{rjson['message']}")

    def cash(self, money):
        url = "http://api.hls178.cn:8080/user/cash"
        body = f"money={money}"
        # 使用代理进行请求
        proxies = self.proxies[randint(0, len(self.proxies)-1)]
        rjson = self.post(url, body=body, proxies=proxies)
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
        self.ticketSignInfo()
        print("")
        self.ticketInfo()
        if(self.bindCash and self.money >= 10):
            print("")
            self.cash(self.money)
        print("\n")


def initEnv():
    env = os.environ
    if(COOKIE_NAME in env):
        cookies = env[COOKIE_NAME]
        return cookies.split("&")
    res = []
    #res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6Mjg5MTQsImV4cCI6MTY5MzIwNjU2NiwiaXNzIjoiaHpxIn0.BAizyzT5uKdCZr1dx74sAu2Apbnc96NgrmGXo28OgKQ")
    #res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6Mjg5MTcsImV4cCI6MTY5MzIwNjQwNSwiaXNzIjoiaHpxIn0.PqFkZvIQCQsTZCIXuYflAK1jx5Ey-hp3HWCzWbhT4Jk")
    #res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6Mjg5MzMsImV4cCI6MTY5MzIwNTgwOCwiaXNzIjoiaHpxIn0.h3dxlX4utaV8jz_7FCyN6Os2s-kGaEzyVjOxCydfdfg")
    #res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjQxMDQsImV4cCI6MTY5Mjk2MDExOCwiaXNzIjoiaHpxIn0.cHuEhdwsoLwflSGu6JgTT1wzKBcp0rwwv8qEG5pJDjY")
    #res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjI5ODcsImV4cCI6MTY5MjkzNjgwMiwiaXNzIjoiaHpxIn0.bhh0M9vRmT9VwowsBdyMNLLF8jvE21XgCyw9CDmpKBY")
    #res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjM3ODAsImV4cCI6MTY5Mjk1NDM1MCwiaXNzIjoiaHpxIn0.JkqwpAqT7o15rUGS7wvuDO7hdBerqdF_pz9-Eq8B72w")
    #res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjY0NTcsImV4cCI6MTY5MzExMDg0MSwiaXNzIjoiaHpxIn0.Xc8lXYafL0BwNFymSeDqAVZm7Y2D--owRh0GjVyNuNU")
    #res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjY0NTUsImV4cCI6MTY5MzExMTQzMiwiaXNzIjoiaHpxIn0.M7iUhzu5VsA7zsw2-qpvhLPOdFROAvp_QsY1cA2cEqE")
    #res.append("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6MjIxODQsImV4cCI6MTY5MjkzMDYwNywiaXNzIjoiaHpxIn0.3COVDlgEyKUnPVZZaWNPV8o1dBLHxDAdno0UBFJ7y-s")
    return res


if __name__ == "__main__":
    tokens = initEnv()
    users = []
    index = 1
    for token in tokens:
        if(token):
            users.append(User(token, index))
            index += 1
    for user in users:
        try:
            user.run()
        except Exception as e:
            print("运行异常：", str(e))
