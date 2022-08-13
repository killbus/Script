import json
import os
import sys
from time import sleep, time
import requests

PROJECT_NAME = "ks"
API_NAME = "ksApi"
API_URL = "http://127.0.0.1:8888/ks/sig?str="

class User:

    def __init__(self, account, index=1) -> None:
        self.account = account
        self.valid = True
        self.index = index

    # 统一GET 额外header用字典传递
    def get(self, url, header=None, isText=False):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; VCE-AL00 Build/HUAWEIVCE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.469 (rel;r) Mobile Safari/537.36 Yoda/2.8.1-rc3 Kwai/10.3.20.24977",
            "Cookie": self.account["cookie"]
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.get(url, headers=headers,timeout=3)
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
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; VCE-AL00 Build/HUAWEIVCE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.469 (rel;r) Mobile Safari/537.36 Yoda/2.8.1-rc3 Kwai/10.3.20.24977",
            "Cookie": self.account["cookie"]
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(url, data=body, headers=headers,timeout=3)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    # 更新签名
    def replaceSig(self, url, body):
        sig = ""
        kvs = body.split("&")
        for kv in kvs:
            if(kv.find("sig=") >= 0):
                sig = self.getSig3(url+kv.split("=")[1])
        if(sig):
            for index in range(len(kvs)):
                if(kvs[index].find("__NS_sig3") >= 0):
                    kvs[index] = "__NS_sig3="+sig
                    newBody = ""
                    for kv in kvs:
                        if(newBody):
                            newBody += "&"+kv
                        else:
                            newBody += kv
                    return newBody
        return None

    # 获取sig3
    def getSig3(self, param):
        url = API_URL+param
        return self.get(url, isText=True)

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
            print(f"金币余额：{rjson['data']['coin']}")
            print(f"现金余额：{rjson['data']['cash']}¥")
        else:
            self.valid = False
            print("登录失败：{0}".format(rjson['error_msg']))

    # 签到信息
    def signInfo(self):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/signIn/info?sigCatVer=1"
        rjson = self.get(url)
        if(not rjson):
            return
        #
        if(rjson['result'] == 1 and "data" in rjson):
            if("sevenDaysSignInData" in rjson['data']):
                sevenDaysSignInData = rjson['data']['sevenDaysSignInData']
                if(sevenDaysSignInData['todaySigned']):
                    print("金币签到：已签到")
                else:
                    print("金币签到：未签到")
                    self.sign(sevenDaysSignInData['signInBizId'])
            elif("cashSignInData" in rjson['data']):
                cashSignInData = rjson['data']['cashSignInData']
                currentDay = cashSignInData['currentDay']
                if(cashSignInData['tasks'][currentDay-1]['status'] !=2):
                    print("金币签到：未签到")
                    self.sign(cashSignInData['signInBizId']) 
                else:
                    print("金币签到：已签到")
            else:
                if(rjson['data']['todaySignInCompleted']):
                    print("金币签到：已签到")
                else:
                    print("金币签到：未签到")
                    self.sign(0)
        elif("error_msg" in rjson):
            print("获取签到信息失败：{0}".format(rjson['error_msg']))

    # 签到
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
                print("宝箱冷却时间：{0}s".format(
                    rjson['data']['treasureCurrentTaskRemainSeconds']))
                self.openBox(rjson['data']['token'])
                sleep(0.1)
                # 激活宝箱
                self.getBoxInfo()
            elif(status == 2):
                print(
                    f"宝箱冷却时间：{rjson['data']['treasureCurrentTaskRemainSeconds']}s")
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

    # 任务列表
    def getTasks(self):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/task/list?searchWidgetStatus=false&rankWidgetStatus=false"
        header = {
            "referer": "https://encourage.kuaishou.com/kwai/task?layoutType=4&source=pendant"}
        rjson = self.get(url, header=header)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            taskList = rjson['data']['dailyTasks']['taskList']
            for task in taskList:
                if(task['taskId'] == 100):
                    print(task['subTitle'])
                    self.ggTask()
                elif(task['taskId'] == 203):
                    print(task['subTitle'])
                    self.gjTask()
        else:
            print("获取任务列表失败："+rjson['error_msg'])

    #广告
    def ggTask(self):
        adList = self.account['ggData']
        if(len(adList)==0):
            print("未填写广告数据")
            return
        index = 0
        for ad in adList:
            index +=1
            if(not(ad['url'] and ad['body'])):
                print("未填写广告数据")
                continue
            url = ad['url']
            body = self.replaceSig("/rest/r/ad/task/report",ad['body'])
            if(not body):
                continue
            header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Client-Info": "model=P40;os=Android;nqe-score=24;network=WIFI;signal-strength=4;",
            "User-Agent": "kwai-android aegon/2.12.0",
            "X-REQUESTID": f"{int(time())*10^8}"}
            rjson = self.post(url, header=header, body=body)
            if(not rjson):
                continue
            if(rjson['result'] == 1):
                print(f"浏览广告[{index}]成功：+{rjson['data']['neoAmount']}金币")
                print("休息5s...")
                sleep(5)
            else:
                print(f"浏览广告[{index}]失败："+rjson['error_msg'])

    # 逛街
    def gjTask(self):
        if(not(self.account['gjData']['url'] and self.account['gjData']['body'])):
            print("未填写逛街数据")
            return
        url = self.account['gjData']['url']
        body = self.replaceSig("/rest/r/reward/task/getActivityReward", self.account['gjData']['body'])
        if(not body):
            return
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Client-Info": "model=P40;os=Android;nqe-score=24;network=WIFI;signal-strength=4;",
            "User-Agent": "kwai-android aegon/2.12.0",
            "X-REQUESTID": f"{int(time())*10^8}"}
        rjson = self.post(url, header=header, body=body)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            print(f"逛街成功：+{rjson['data']['amount']}金币")
        else:
            print("逛街失败："+rjson['error_msg'])

    # 金币抽奖签到
    def gameSignIn(self):
        url = "https://activity.e.kuaishou.com/rest/r/game/sign-in"
        header = {
            "X-Requested_With":"com.smile.gifmaker",
            "Referer":"https://activity.e.kuaishou.com/incentiveAdvertising?layoutType=4"
        }
        rjson = self.get(url,header=header)
        if(not rjson):
            self.gameValid = False
            return
        if(rjson['result'] == 1):
            self.gameValid = True
        else:
            self.gameValid = False

    #金币抽奖信息
    def gameInfo(self):
        url = "https://activity.e.kuaishou.com/rest/r/game/user/info"
        header = {
            "X-Requested_With":"com.smile.gifmaker",
            "Referer":"https://activity.e.kuaishou.com/incentiveAdvertising?layoutType=4"
        }
        rjson = self.get(url,header=header)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            print("===>金币抽奖")
            print(f"积累金币：{rjson['data']['userCoinResult']['coins']}")
            print(f"宝石进度：{rjson['data']['userDiamondResult']['diamondPercent']}")
            print(f"可抽奖次数：{rjson['data']['userDailyLotteryTimesResult']['remainTimes']}")
            if(rjson['data']['userDailyLotteryTimesResult']['remainTimes'] >0):
                self.gameLottery()
        else:
            print("获取抽奖信息失败："+rjson['error_msg'])

    #金币抽奖定时奖励信息
    def gameTimerInfo(self):
        url = "https://activity.e.kuaishou.com/rest/r/game/timer-reward/info"
        header = {
            "X-Requested_With":"com.smile.gifmaker",
            "Referer":"https://activity.e.kuaishou.com/incentiveAdvertising?layoutType=4"
        }
        rjson = self.get(url,header=header)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            if(not rjson['data']):
                return
            if(not rjson['data']['lastTimerTime'] or rjson['data']['lastTimerTime']+1000*60*rjson['data']['minutesInterval'] < rjson['data']['serverTime']):
                print(f"定时奖励可领取")
                self.gameTimerReqward()
            else:
                print("定时奖励冷却中")
        else:
            print("获取定时奖励信息失败："+rjson['error_msg'])

    #金币抽奖定时奖励领取
    def gameTimerReqward(self):
        url = "https://activity.e.kuaishou.com/rest/r/game/timer-reward"
        header = {
            "X-Requested_With":"com.smile.gifmaker",
            "Referer":"https://activity.e.kuaishou.com/incentiveAdvertising?layoutType=4"
        }
        rjson = self.post(url,header=header)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            print("领取定时奖励成功")
        else:
            print("领取定时奖励失败："+rjson['error_msg'])

    #金币抽奖
    def gameLottery(self):
        url = "https://activity.e.kuaishou.com/rest/r/game/lottery?wheelVersion=1"
        header = {
            "X-Requested_With":"com.smile.gifmaker",
            "Referer":"https://activity.e.kuaishou.com/incentiveAdvertising?layoutType=4"
        }
        rjson = self.post(url,header=header)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            print(f"抽奖成功：+{rjson['data']['coinCount']}金币  +{rjson['data']['diamondCount']}钻石")
        else:
            print("抽奖失败："+rjson['error_msg'])

    #金币抽奖看视频
    def gameView(self):
        adList = self.account['lotteryData']
        if(len(adList)==0):
            print("未填写金币抽奖视频数据")
            return
        index = 0
        for ad in adList:
            index +=1
            if(not(ad['url'] and ad['body'])):
                continue
            params = self.replaceSig("/rest/r/ad/task/report",ad['url'])
            if(not params):
                continue
            url = "https://api.e.kuaishou.com/rest/r/ad/task/report?"+params
            header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Client-Info": "model=P40;os=Android;nqe-score=24;network=WIFI;signal-strength=4;",
            "User-Agent": "kwai-android aegon/2.12.0",
            "X-REQUESTID": f"{int(time())*10^8}"}            
            rjson = self.post(url,ad['body'],header=header)        
            if(rjson['result'] == 1):
                print(f"浏览金币抽奖视频[{index}]成功")
                print("休息5s...")
                sleep(5)
            else:
                print(f"浏览金币抽奖视频[{index}]失败："+rjson['error_msg'])
    
    #金币抽奖任务
    def gameTasks(self):
        url = "https://activity.e.kuaishou.com/rest/r/game/tasks"
        header = {
            "X-Requested_With":"com.smile.gifmaker",
            "Referer":"https://activity.e.kuaishou.com/incentiveAdvertising?layoutType=4"
        }
        rjson = self.get(url,header=header)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            dailyTasks = rjson['data']['dailyTasks']
            growthTasks = rjson['data']['growthTasks']
            for dailyTask in dailyTasks:
                if(dailyTask['taskState'] == 1):
                    print(f"任务[{dailyTask['taskTitle']}]可领取奖励")
                    self.gameTasksReward(dailyTask)
            for growthTask in growthTasks:
                if(growthTask['taskState'] == 1):
                    print(f"任务[{dailyTask['taskTitle']}]可领取奖励")
                    self.gameTasksReward(growthTask)
        else:
            print("获取任务失败："+rjson['error_msg'])        

    #金币抽奖领取任务奖励
    def gameTasksReward(self,task):
        url = "https://activity.e.kuaishou.com/rest/r/game/task/reward-receive?taskName="+task['taskName']
        header = {
            "X-Requested_With":"com.smile.gifmaker",
            "Referer":"https://activity.e.kuaishou.com/incentiveAdvertising?layoutType=4"
        }
        rjson = self.get(url,header=header)
        if(not rjson):
            return    
        if(rjson['result'] == 1):
            if(rjson['data']['success']):
                print(f"领取任务[{task['taskTitle']}]成功")
            else:
                print(f"领取任务[{task['taskTitle']}]奖励失败："+rjson['data']['msg'])          
        else:
            print(f"领取任务[{task['taskTitle']}]奖励失败："+rjson['error_msg'])          

    def run(self):
        print(f"=====账号[{self.index}]=====")
        if(self.account['remark']):
            print("账号备注："+self.account['remark'])
        self.home()
        if(self.valid):
            self.signInfo()
            self.getBoxInfo()
            print("")
            self.getTasks()
            self.gameSignIn()
            if(self.gameValid):
                print("")
                self.gameInfo()
                self.gameTimerInfo()
                self.gameView()
                self.gameTasks()
            print("")


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
            {"remark": "", "cookie": "", "gjData": {"url": "", "body": ""}, "ggData": [{"url": "", "body": ""}]}]}
        file.write(json.dumps(newContent, indent=2))
        file.close()
    if(API_NAME in os.environ):
        API_URL = os.environ[API_NAME]
    return accountList


if __name__ == "__main__":
    accounts = initEnv()
    users = []
    index = 1
    for account in accounts:
        if(account["cookie"]):
            users.append(User(account, index))
            index += 1
    for user in users:
        try:
            user.run()
        except Exception as e:
            print("运行出错："+str(e))
