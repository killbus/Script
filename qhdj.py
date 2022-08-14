import base64
import hashlib
import json
from math import fabs
import os
from random import randint
from re import T
from time import sleep, time
from urllib.parse import urlencode
import warnings
import requests

COOKIE_NAME = "qhdj"
adventureIds = []
userIds = []
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
            self.userId = rjson['data']['id']
            self.gameNum = rjson['data']['gaNum']
        else:
            print("获取账号信息失败："+rjson['message'])
    
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
                    if(task['name'] != "助力任务"):
                        self.taskReport(task['taskId'],task['taskType'])
                        sleep(3)
                    else:
                        userIds.append(self.userId)
                elif(task['status'] == 2):
                    print(f"任务[{task['name']}] 待领取奖励")
                    self.taskPrize(task['taskId'])
                    sleep(3)
                else:
                    print(f"任务[{task['name']}] 已完成")
        else:
            print("获取任务列表失败："+rjson['message'])

    #提交任务
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

    #领取任务奖励
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

    #冒险信息
    def adventureInfo(self,start = False):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/user/adventure/info?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            self.adventureId = rjson['data']['adventureId']
            if(start):
                if(rjson['data']['status'] == 0):
                    self.adventureStart()
                return
            if(rjson['data']['status'] == 0):
                print("冒险状态：空闲中")
                adventureIds.append(self.adventureId)
            else:
                print("冒险状态：进行中")
                print(f"倒计时：{rjson['data']['endTime'] -int(time())}s")
                print(f"同行人数：{len(rjson['data']['friendVoList'])}")
        else:
            print("获取冒险信息失败："+rjson['message'])

    #开始冒险
    def adventureStart(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/user/adventure/start?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"账号[{self.index}]开始冒险成功")
        else:
            print(f"账号[{self.index}]开始冒险失败："+rjson['message'])        

    #冒险参团
    def adventureHelp(self):
        for adventureId in adventureIds:
            if(adventureId == self.adventureId):
                continue
            params = self.getSign()
            params['adventureId'] = adventureId
            url = f"https://api.xiaoyisz.com/qiehuang/ga/user/adventure/help?{urlencode(params)}"
            rjson = self.get(url)
            if(not rjson):
                continue
            if(rjson['code'] == 0):
                print(f"账号[{self.index}]协助冒险[{adventureId}]成功")
            else:
                print(f"账号[{self.index}]协助冒险[{adventureId}]失败："+rjson['message'])
            sleep(2)

    #好友助力
    def inviteHelp(self):
        for userId in userIds:
            if(self.userId == userId):
                continue
            params = self.getSign()
            params['taskType'] = 1
            params['taskId'] = "1558733726417952768"
            params['attachId'] = userId
            url = f"https://api.xiaoyisz.com/qiehuang/ga/user/task/report?{urlencode(params)}"
            rjson = self.get(url)
            if(not rjson):
                continue
            if(rjson['code'] == 0):
                print(f"账号[{self.index}]助力[{userId}]成功")
            else:
                print(f"账号[{self.index}]助力[{userId}]失败："+rjson['message'])

    #种植信息
    def plantInfo(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/plant/info?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            self.plantId = rjson['data']['plantId']
            print(f"种植阶段：{rjson['data']['stage']}")
            print(f"阶段进度：{rjson['data']['currentSunshineNum']}/{rjson['data']['needSunshineNum']}")
            if(rjson['data']['currentSunshineNum'] == rjson['data']['needSunshineNum']):
                self.plantUpgrade()
        else:
            print("获取种植信息失败："+rjson['message'])        
    
    #种植升级
    def plantUpgrade(self):
        params = self.getSign()
        params['plantId'] = self.plantId
        url = f"https://api.xiaoyisz.com/qiehuang/ga/plant/upgrade?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"种植进阶成功：{rjson['data']['stage']}")
        else:
            print("种植进阶失败："+rjson['message'])
    
    #每日阳光
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

    #每日阳光领取
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

    #开始挑战
    def challengeStart(self):
        params = self.getSign()
        url = f"https://api.xiaoyisz.com/qiehuang/ga/challenge/start?{urlencode(params)}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print("开始游戏成功，等待6s...")
            sleep(5)
            self.challengeFinish(rjson['data'])
        else:
            print("开始挑战游戏失败："+rjson['message'])

    def challengeFinish(self,battleId):
        params = self.getSign()
        body = {"battleId":battleId,"result":1,"costMillisecond":6000}
        url = f"https://api.xiaoyisz.com/qiehuang/ga/challenge/report?{urlencode(params)}"
        rjson = self.post(url,body=json.dumps(body))
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print(f"挑战成功：+{rjson['data']['infos'][0]['num']}阳光")
        else:
            print("挑战失败："+rjson['message'])

    #施洒阳光
    def giveSunshine(self):
        if(self.sunshineNum < 200):
            return
        params = self.getSign()
        params.update({"plantId": self.plantId})
        url = ""
        if(self.sunshineNum >600):
            url = f"https://api.xiaoyisz.com/qiehuang/ga/plant/batchgiveSunshine?{urlencode(params)}"
        else:
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
        if(self.gameNum):
            print("")
            self.challengeStart()
        print("")
        self.adventureInfo()
        print("")
        self.plantInfo()
        print("")
        self.giveSunshine()
        print("\n")

def initEnv():
    env = os.environ
    if(COOKIE_NAME in env):
        cookies = env[COOKIE_NAME]
        if(cookies.find("&")):
            return cookies.split("&")
    return []

if __name__ == "__main__":
    tokens = initEnv()
    users = []
    index = 1
    for token in tokens:
        users.append(User(token,index))
        index +=1
    for user in users:
        try:
            user.run()
        except Exception as e:
            print("运行出错："+str(e))

    if(len(userIds)):
        print("\n>>>>好友助力")
        for user in users:
            try:
                user.taskInvite()
            except Exception as e:
                print("运行出错："+str(e))

    if(len(adventureIds)):
        print("\n>>>>冒险探索")
        for user in users:
            try:
                user.adventureHelp()
            except Exception as e:
                print("运行出错："+str(e))
        
        for user in users:
            try:
                user.adventureInfo(True)
            except Exception as e:
                print("运行出错："+str(e))
