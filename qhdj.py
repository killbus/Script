import base64
import hashlib
import json
from math import fabs
from random import randint
from re import T
from time import sleep, time
from urllib.parse import urlencode
import warnings
import requests


login = "appId=wx532ecb3bdaaf92f9&md5Secret=111111111112222222233333333333&openId=oBk224qXvXTiaRutzvH8kia5FI2A&wid=10072285262"
api = "clientKey=IfWu0xwXlWgqkIC7DWn20qpo6a30hXX6&clientSecret=A4rHhUJfMjw2I5CODh5g40Ja1d3Yk1CH&nonce=n7xBzQPKZy5k7EpM&timestamp=1660378205939"

warnings.filterwarnings("ignore")


class User:
    def __init__(self, data, index) -> None:
        self.index = index
        self.info = self.parseInfo(data)
        if(self.info):
            self.valid = True
            self.authorization = ""
        else:
            self.valid = False

   # 统一GET 额外header用字典传递
    def get(self, url, header=None, isText=False):
        headers = {
            "Content-Type": "application/json",
            "Referer": "https://thekingoftomato.ioutu.cn/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; VCE-AL00 Build/HUAWEIVCE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.469 (rel;r) Mobile Safari/537.36 Yoda/2.8.1-rc3 Kwai/10.3.20.24977",
            "authorization": self.authorization}
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.get(url, headers=headers, timeout=3, verify=False)
            if(isText):
                return res.text
            else:
                return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    # 统一POST 额外header用字典传递
    def post(self, url, body='', header=None):
        headers = {
            "Content-Type": "application/json",
            "Referer": "https://thekingoftomato.ioutu.cn/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; VCE-AL00 Build/HUAWEIVCE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.469 (rel;r) Mobile Safari/537.36 Yoda/2.8.1-rc3 Kwai/10.3.20.24977",
            "authorization": self.authorization}
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(
                url, data=body, headers=headers, timeout=3, verify=False)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def md5(self, data):
        md5 = hashlib.md5()
        md5.update(data.encode())
        return md5.hexdigest().upper()

    def getNonce(self):
        ch = "abcdefghjklmnopqrstuvwyz1234567890ABCDEFGHJKLMNOPQRSTUVWYZ"
        nonce = ""
        for i in range(16):
            nonce += ch[randint(0, len(ch)-1)]
        return nonce

    def getSign(self):
        nonce = self.getNonce()
        timestamp = int(time()*1000)
        encodeData = f"clientKey=IfWu0xwXlWgqkIC7DWn20qpo6a30hXX6&clientSecret=A4rHhUJfMjw2I5CODh5g40Ja1d3Yk1CH&nonce={nonce}&timestamp={timestamp}"
        sign = self.md5(encodeData)
        return {"nonce": nonce, "timestamp": timestamp, "signature": sign}

    def parseInfo(self, data):
        data = base64.decodebytes(data.encode()).decode()
        try:
            info = json.loads(data)
            if("thirdAppId" in info and "openId" in info and "wid" in info):
                return {
                    "appId": info['thirdAppId'],
                    "openId": info['openId'],
                    "wid": info['wid']}
            else:
                return None
        except Exception as e:
            return None

    def login(self):
        url = "https://api.xiaoyisz.com/qiehuang/ga/public/api/login"
        encodeData = f"appId={self.info['appId']}&md5Secret=111111111112222222233333333333&openId={self.info['openId']}&wid={self.info['wid']}"
        sign = self.md5(encodeData)
        body = {
            "signature": sign,
            "appId": self.info['appId'],
            "openId": self.info['openId'],
            "wid": self.info['wid']
        }
        rjson = self.post(url, body=json.dumps(body))
        if(rjson['code'] == 0):
            self.valid = True
            self.authorization = rjson['data']
        else:
            self.valid = False
            print("登录失败："+rjson['message'])

    def userInfo(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/user/info?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"用户昵称：{rjson['data']['nickName']}")
            print(f"番茄数量：{rjson['data']['tomatoNum']}")
            print(f"账号等级：{rjson['data']['level']}")
            print(
                f"等级经验：{rjson['data']['levelExp']}/{rjson['data']['needExp']}")
            print(f"游戏次数：{rjson['data']['gaNum']}")
            print(f"阳光数量：{rjson['data']['sunshineNum']}")
            self.sunshineNum = rjson['data']['sunshineNum']
        else:
            print("获取账号信息失败："+rjson['message'])
        
    def dailyInfo(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/user/daily/info?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"今日可领阳光：{rjson['data']['yesterdaySunshineNum']}")
            if(rjson['data']['yesterdaySunshineNum']):
                self.dailyPickup()
            print(f"明天可领阳光：{rjson['data']['sunshineNum']}")
        else:
            print("获取日常信息失败："+rjson['message'])

    def taskList(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/user/task/list?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            tasks = rjson['data']
            for task in tasks:
                if(task['status'] == 1):
                    print(f"任务[{task['name']}] 未完成")
                    self.taskReport(task['taskId'],task['taskType'])
                    sleep(3)
                elif(task['status'] == 2):
                    print(f"任务[{task['name']}] 待领取奖励")
                    self.taskPrize(task['taskId'])
                    sleep(3)
                else:
                    print(f"任务[{task['name']}] 已完成")
        else:
            print("获取任务列表失败："+rjson['message'])

    def taskReport(self,taskId,taskType):
        params = self.getSign()
        params['taskId'] = taskId
        params['taskType'] = taskType
        params['attachId'] = int(time()*1000)
        url = f"https://api.xiaoyisz.com/qiehuang/ga/user/task/report?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print("提交任务成功")
        else:
            print("提交任务失败："+rjson['message'])

    def taskPrize(self,taskId):
        params = self.getSign()
        params['taskId'] = taskId
        url = f"https://api.xiaoyisz.com/qiehuang/ga/user/task/drawPrize?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print("领取奖励成功")
        else:
            print("领取奖励失败："+rjson['message'])

    def adventureInfo(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/user/adventure/info?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            if(rjson['data']['status'] == 0):
                print("冒险状态：空闲中")
                self.adventureStart()
            else:
                print("冒险状态：进行中")
                print(f"倒计时：{rjson['data']['endTime'] -int(time())}s")
        else:
            print("获取冒险信息失败："+rjson['message'])

    def adventureStart(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/user/adventure/start?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print("开始冒险成功")
        else:
            print("开始冒险失败："+rjson['message'])        

    def plantInfo(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/plant/info?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"种植阶段：{rjson['data']['stage']}")
            print(f"阶段进度：{rjson['data']['currentSunshineNum']}/{rjson['data']['needSunshineNum']}")
            if(rjson['data']['currentSunshineNum'] == rjson['data']['needSunshineNum']):
                self.plantUpgrade()
        else:
            print("获取种植信息失败："+rjson['message'])        
    
    def plantUpgrade(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/plant/upgrade?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"种植进阶成功：{rjson['data']['stage']}")
        else:
            print("种植进阶失败："+rjson['message'])

    def dailyPickup(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/user/daily/pickup?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"领取阳光成功：+{rjson['data']}")
        else:
            print("领取阳光失败："+rjson['message'])

    def giveSunshine(self):
        if(self.sunshineNum < 200):
            return
        params = self.getSign()
        params.update({"plantId": "1558363025227128832"})
        url = f"https://api.xiaoyisz.com/qiehuang/ga/plant/giveSunshine?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(
                f"施洒阳光成功：{rjson['data']['currentSunshineNum']}/{rjson['data']['needSunshineNum']}")
        else:
            print("施洒阳光失败："+rjson['message'])

    def run(self):
        print(f"======账号[{self.index}]======")
        if(not self.valid):
            print("账号无效，退出执行")
            return
        self.login()
        if(not self.valid):
            return
        self.userInfo()
        print("")
        self.dailyInfo()
        print("")
        self.taskList()
        print("")
        self.adventureInfo()
        print("")
        self.plantInfo()
        print("")
        self.giveSunshine()


data = "eyJ0aGlyZEFwcElkIjoid3g1MzJlY2IzYmRhYWY5MmY5Iiwid2lkIjoxMDA3MjI4NTI2Miwib3BlbklkIjoib0JrMjI0cVh2WFRpYVJ1dHp2SDhraWE1RkkyQSIsImhvbWVTdG9yZUlkIjpudWxsLCJ1dG1fbWVkaXVtIjoiYXBiYW5uZXIiLCJ1dG1fY29udGVudCI6ImFwYmFubmVyIiwidXRtX3NvdXJjZSI6ImhhcHB5bXAiLCJ1dG1fY2FtcGFpZ24iOiJoYXBweWFwIiwiX2NoYW5uZWxfdHJhY2tfa2V5IjoiQTNuZ294djkiLCJ1c2VySW5mbyI6e30sImNoYW5uZWxJbmZvIjp7InV0bV9jYW1wYWlnbiI6ImhhcHB5YXAiLCJ1dG1fc291cmNlIjoiaGFwcHltcCIsInV0bV9tZWRpdW0iOiJhcGJhbm5lciIsInV0bV9jb250ZW50IjoiYXBiYW5uZXIifX0="
User(data, 1).run()
