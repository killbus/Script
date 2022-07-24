import hashlib
import random
import sys
import os.path
import json
from time import localtime, sleep, strftime, time
import requests

projectNameCN = "快手极速版"
projectNameEN = "ksjsb"
accounts = []
adList = []
config = {}


# 初始化配置
def initEnv():
    global accounts
    global config
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\\{0}.json".format(projectNameEN)
    else:
        filePath += "/{0}.json".format(projectNameEN)

    projectConfig = {}
    if(os.path.isfile(filePath)):
        # 只读打开
        file = open(filePath, "r", encoding="utf-8")
        content = file.read()
        if(content):
            projectConfig = json.loads(content)
        file.close()

        # 账号配置
        tempAccounts = []
        if('accounts' in projectConfig):
            tempAccounts = projectConfig['accounts']
        else:
            # 改为覆盖写模式
            file = open(filePath, "w", encoding="utf-8")
            accounts = []
            count = 5
            while(count):
                accounts.append({"name": "", "cookie": ""})
                count -= 1
            projectConfig = {
                "accounts": accounts, "projectNameCN": projectNameCN, "config": {"log": False}}
            file.write(json.dumps(projectConfig, indent=2))
            print("当前项目未配置账号，脚本关闭")
            file.close()
            exit()
        position = 0
        for account in tempAccounts:
            # 设置了名称和密钥的账号才算有效
            if(account['name'] and account['cookie']):
                # 用户序号，用于运行过程修改用户信息
                account['index'] = position
                position += 1
                accounts.append(account)
        if(len(accounts) > 0):
            print("账号个数：{0}".format(len(accounts)))
        else:
            print("未发现有效账号，脚本结束")
            exit()
        # 其他配置
        if("config" in projectConfig):
            config = projectConfig['config']

    else:
        # 创建配置文件
        file = open(filePath, "w", encoding="utf-8")
        accounts = []
        count = 5
        while(count):
            accounts.append({"name": "", "cookie": ""})
            count -= 1
        projectConfig = {
            "accounts": accounts, "projectNameCN": projectNameCN, "config": {}}
        file.write(json.dumps(projectConfig, indent=2))
        print("当前项目未配置账号，脚本关闭")
        file.close()
        exit()


def log():
    content = strftime('%Y_%m_%d_%H_%M_%S', localtime(time()))
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\log\\{0}.log".format(content)
    else:
        filePath += "/log/{0}.log".format(content)
    file = open(filePath, "w+", encoding="utf-8")
    file.write(content)
    file.close()


# 加载广告信息
def initAdInfo():
    global adList
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\\adList.json"
    else:
        filePath += "/adList.json"
    if(os.path.isfile(filePath)):
        file = open(filePath, "r+", encoding="utf-8")
        rjson = json.loads(file.read())
        if("adList" in rjson):
            adList = rjson['adList']
    if(len(adList) > 0):
        print("加载广告信息成功：{0}".format(len(adList)))
    else:
        print("加载广告信息失败")



# 签名函数
def MD5(s):
    hl = hashlib.md5()
    hl.update(s.encode(encoding='utf8'))
    md5 = hl.hexdigest()
    return str(md5)

    
# 更换cookie关键字段 版本号，did
def sortCookie(account):
    cookieList = account['cookie'].replace(" ", "").split(";")
    cookie = ""
    for c in cookieList:
        dic = c.split("=")
        if(len(dic) == 2):
            if(dic[0] == "ver"):
                cookie += "ver=9.10;"
            elif(dic[0] == "appver"):
                cookie += "appver=9.10.40.2474;"
            else:
                cookie += "{0}={1};".format(dic[0], dic[1])
    account['cookie'] = cookie


# 统一GET 额外header用字典传递
def get(account, url, header=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10);",
        "Cookie": account['cookie']
    }
    if(header):
        for k, v in header.items():
            headers[k] = v
    # 捕获异常
    try:
        res = requests.get(url, headers=headers)
        return res.json()
    except Exception as e:
        print("用户[{0}]GET异常：{1}".format(account['name'], str(e)))
        return None


# 统一POST 额外header用字典传递
def post(account, url, body='', header=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;)",
        "cookie": account['cookie']
    }
    if(header):
        for k, v in header.items():
            headers[k] = v
    # 捕获异常
    try:
        res = requests.post(url, data=body, headers=headers)
        return res.json()
    except Exception as e:
        print("用户[{0}]POST异常：{1}".format(account['name'], str(e)))
        return None


# 获取用户基本信息
def getBasicInfo(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/activity/earn/overview/basicInfo"
    rjson = get(account, url)
    if(not rjson):
        return {"normal": False}

    if(rjson['result'] == 1):
        data = rjson['data']
        print("用户[{0}]：{1}金币\t{2}元\t待审核{3}元".format(data['userData']['nickname'],
              data['totalCoin'], data['totalCash'], float(data['allCash'])-float(data['totalCash'])))
        return {"normal": True, "nickname": data['userData']['nickname'], 'avatar': data['userData']['avatar'], "totalCoin": data['totalCoin'], 'totalCash': data['totalCash'], 'allCash': data['allCash']}
    else:
        print("用户[{0}]登录失败".format(account['name']))
        return {"normal": False}


# 获取签到信息
def getSignInfo(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/sign/queryPopup"
    rjson = get(account, url)
    if(not rjson):
        return

    if(not rjson):
        return
    if(rjson['result'] == 1):
        if(rjson['data']['nebulaSignInPopup']['todaySigned']):
            print("用户[{0}]今日已签到".format(account['basicInfo']['nickname']))
        else:
            sign(account)
    else:
        print("用户[{0}]查询签到信息失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 签到
def sign(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/sign/sign?source=activity"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]签到成功：{1}".format(account['basicInfo']
              ['nickname'], rjson['data']['toast']))
        #signDouble(account)
        setShare(account)
    else:
        print("用户[{0}]签到失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 签到翻倍视频
def signDouble(account):
    header = {"content-type": "application/x-www-form-urlencoded"}
    url1 = "https://api.e.kuaishou.com/rest/r/ad/nebula/reward"
    body1 = 'bizStr={{"endTime":{endTime},"eventValue":-1,"rewardList":[{{"creativeId":21763320194,"extInfo":"","llsid":2001303165933396200,"taskType":1}}],"startTime":{startTime},"taskId":136}}'.format(
        startTime=int(time()-30)*1000, endTime=int(time()))
    rjson1 = post(account, url1, body=body1, header=header)
    if(not rjson1):
        return
    if(rjson1['result'] == 1):
        print("用户[{0}]看签到翻倍视频1成功：+{1}金币".format(account['basicInfo']
              ['nickname'], rjson1['data']['awardAmount']))
    else:
        print("用户[{0}]看签到翻倍视频失败：{1}".format(
            account['basicInfo']['nickname'], rjson1['error_msg']))

    url2 = "https://api.e.kuaishou.com/rest/r/ad/task/report"
    body2 = 'bizStr={{"businessId":168,"endTime":{endTime},"extParams":"56dfe31594b858e69ef613f5e97227fbd5f9da00aa5144df8830a5781ae07d7cfaf4d95abc2510c950f99404a9e0bf62f5b5765a867c385685e0570ed76b858a159dacd55e41e4a9813db4e619a8b092","mediaScene":"video","neoInfos":[{{"creativeId":22689582371,"extInfo":"","llsid":2001303467453322800,"taskType":1}}],"pageId":100012068,"posId":6765,"startTime":{startTime},"subPageId":100015089}}'.format(
        startTime=int(time()-30)*1000, endTime=int(time()))
    rjson2 = post(account, url2, body=body2, header=header)
    if(not rjson2):
        return
    if(rjson2['result'] == 1):
        print("用户[{0}]看签到翻倍视频2成功：+{1}金币".format(account['basicInfo']
              ['nickname'], rjson2['data']['neoAmount']))
    else:
        print("用户[{0}]看签到翻倍视频2失败：{1}".format(
            account['basicInfo']['nickname'], rjson2['error_msg']))


# 分享得金币任务
def setShare(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/account/withdraw/setShare"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]准备分享得金币".format(account['basicInfo']['nickname']))
        getShareReward(account)


# 领取分享任务奖励
def getShareReward(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/daily/report?taskId=122"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("账号[{0}]完成任务[122]成功，获得{1}金币".format(
            account['basicInfo']['nickname'], rjson['data']['amount']))
    else:
        print("账号[{0}]完成任务[122]失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))
    if('taskProcess' in account):
        account['taskProcess']['share'] = True
    else:
        account['taskProcess'] = {"share": True}


# 宝箱信息
def boxInfo(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/box/explore?isOpen=false&isReadyOfAdPlay=true"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        if(rjson['data']['treasureBoxOpenTimestamp'] < 0):
            print("用户[{0}]开宝箱次数已用完".format(account['basicInfo']['nickname']))
            return
        openTime = int(rjson['data']['openTime']/1000)
        print("用户[{0}]宝箱冷却时间：{1}s".format(
            account['basicInfo']['nickname'], openTime))
        if(openTime == 0):
            openBox(account)
    else:
        print("用户[{0}]获取宝箱信息失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 开启宝箱
def openBox(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/box/explore?isOpen=true&isReadyOfAdPlay=true"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1 and rjson['data']['commonAwardPopup']):
        print("用户[{0}]开启宝箱成功：+{1}金币".format(
            account['basicInfo']['nickname'], rjson['data']['commonAwardPopup']['awardAmount']))
        #boxDouble(account)
    elif("error_msg" in rjson):
        print("用户[{0}]开启宝箱失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 宝箱翻倍
def boxDouble(account):
    url = "https://api.e.kuaishou.com/rest/r/ad/nebula/reward"
    header = {"content-type": "application/x-www-form-urlencoded"}
    body = 'bizStr={"endTime":1651642933626,"eventValue":-1,"rewardList":[{"creativeId":22640573497,"extInfo":"","llsid":2005130886717778000,"taskType":1}],"startTime":1651642875845,"taskId":77}'
    rjson = post(account, url, body=body, header=header)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]看宝箱翻倍视频成功：+{1}金币".format(account['basicInfo']
              ['nickname'], rjson['data']['awardAmount']))
    else:
        print("用户[{0}]看宝箱翻倍视频失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 获取日常任务列表
def getDailyTasks(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/activity/earn/overview/tasks?addressBookAccessStatus=true&pushNotificationStatus=false"
    rjson = get(account, url)
    if(not rjson):
        return
    if(not rjson):
        return
    if(rjson['result']):
        dailyTasks = rjson['data']['dailyTasks']
        print("用户[{0}]任务完成情况：".format(account['basicInfo']['nickname']))
        for task in dailyTasks:
            # 17广告视频 34直播 161抽奖 148逛街
            if(task['id'] in [17, 34, 161, 148]):
                if("taskProcess" not in account):
                    account['taskProcess'] = {}
                account['taskProcess']["{0}".format(task['id'])] = {
                    "name": task['name'], "stages": task['stages'], "completedStages": task['completedStages']}
                print(
                    "【{0}】：{1}/{2}".format(task['name'], task['completedStages'], task['stages']))
    else:
        print("用户[{0}]获取日常任务列表失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 逛街
def taskGJ(account):
    url = "https://api.e.kuaishou.com/rest/r/reward/task/getActivityReward"
    body = "activityId=148&client_key=ksgjbody"
    header = {"content-type": "application/x-www-form-urlencoded"}
    rjson = post(account, url, body=body, header=header)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]逛街成功：+{1}金币".format(account['basicInfo']
              ['nickname'], rjson['data']['amount']))
    else:
        print("用户[{0}]逛街失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 广告视频
def taskAdView(account):
    url = "https://api.e.kuaishou.com/rest/r/ad/nebula/reward"
    header = {"content-type": "application/x-www-form-urlencoded"}
    body = 'bizStr={{"endTime":{endTime},"eventValue":-1,"rewardList":[{{"creativeId":22675806909,"extInfo":"","llsid":2001301948745607200,"taskType":1}}],"startTime":{startTime},"taskId":0}}'.format(
        startTime=int(time()-30)*1000, endTime=int(time()))
    rjson = post(account, url, body=body, header=header)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]看广告视频成功：+{1}金币".format(account['basicInfo']
              ['nickname'], rjson['data']['awardAmount']))
    else:
        print("用户[{0}]看广告视频失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 直播任务
def taskOnline(account):
    url = "https://api.e.kuaishou.com/rest/r/ad/task/report"
    header = {"content-type": "application/x-www-form-urlencoded"}
    ad = adList[random.randint(0, len(adList)-1)]
    body = 'bizStr={{"businessId":75,"endTime":{endTime},"extParams":"56dfe31594b858e69ef613f5e97227fbd5f9da00aa5144df8830a5781ae07d7cfaf4d95abc2510c950f99404a9e0bf62f5b5765a867c385685e0570ed76b858a159dacd55e41e4a9813db4e619a8b092","mediaScene":"video","neoInfos":[{{"creativeId":{creativeId},"extInfo":"","llsid":{llsid},"taskType":1}}],"pageId":100012068,"posId":6765,"startTime":{startTime},"subPageId":100015089}}'.format(
        startTime=int(time()-30)*1000, endTime=int(time()), llsid=ad['llsid'], creativeId=ad['creativeId'])
    rjson = post(account, url, body=body, header=header)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]看直播任务成功：+{1}金币".format(account['basicInfo']
              ['nickname'], rjson['data']['neoAmount']))
    else:
        print("用户[{0}]看直播任务失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 抽奖视频
def taskLuckView(account):
    url = "https://api.e.kuaishou.com/rest/r/ad/task/report"
    header = {"content-type": "application/x-www-form-urlencoded"}

    paramList = [
        {'extParams': "56dfe31594b858e69ef613f5e97227fbf89856abafca7f90fab063cf60935d6faedb05b76646dc3ece57cd4898d412d86e985a2b510216ad4853603d2992501cea0a08182731fcbf023467cf30ecda80",
         'businessId': 161,
         'pageId': 11101,
         'posId': 4685,
         'subPageId': 100013630,
         'name': "抽奖视频161-213"},
        {
            "extParams": "56dfe31594b858e69ef613f5e97227fbf89856abafca7f90fab063cf60935d6faedb05b76646dc3ece57cd4898d412d86e985a2b510216ad4853603d2992501cea0a08182731fcbf023467cf30ecda80",
            "businessId": 11,
            "pageId": 11101,
            "posId": 4684,
            "subPageId": 100013629,
            "name": "抽奖视频11-213"
        },
        {'extParams': "56dfe31594b858e69ef613f5e97227fbf89856abafca7f90fab063cf60935d6faedb05b76646dc3ece57cd4898d412d86e985a2b510216ad4853603d2992501cea0a08182731fcbf023467cf30ecda80",
         'businessId': 161,
         'pageId': 11101,
         'posId': 4685,
         'subPageId': 100013630,
         'name': "抽奖视频161-213"},
        {
            "extParams": "56dfe31594b858e69ef613f5e97227fbf89856abafca7f90fab063cf60935d6faedb05b76646dc3ece57cd4898d412d86e985a2b510216ad4853603d2992501cea0a08182731fcbf023467cf30ecda80",
            "businessId": 11,
            "pageId": 11101,
            "posId": 4684,
            "subPageId": 100013629,
            "name": "抽奖视频11-213"
        },
        {
            'extParams': "56dfe31594b858e69ef613f5e97227fb67b973ad1394855c549442d15702f96393178eaeef5635134bb7e4ff97e69218c1f18455baf645dbaef685b7bf30c0914ea53ddcde26b2fa67b888203dab0fd4",
            'businessId': 161,
            'pageId': 11101,
            'posId': 4684,
            'subPageId': 100013629,
            'name': '抽奖视频161-100'
        },
        {
            "extParams": "56dfe31594b858e69ef613f5e97227fb67b973ad1394855c549442d15702f96393178eaeef5635134bb7e4ff97e69218c1f18455baf645dbaef685b7bf30c0914ea53ddcde26b2fa67b888203dab0fd4",
            "businessId": 11,
            "pageId": 11101,
            "posId": 4684,
            "subPageId": 100013629,
            "name": "抽奖视频11-100"
        }
    ]

    for param in paramList:
        ad = adList[random.randint(0, len(adList)-1)]
        body = 'bizStr={{"businessId":{businessId},"endTime":{endTime},"extParams":"{extParams}","mediaScene":"video","neoInfos":[{{"creativeId":{creativeId},"extInfo":"","llsid":{llsid},"taskType":1}}],"pageId":{pageId},"posId":{posId},"startTime":{startTime},"subPageId":{subPageId}}}'.format(
            businessId=param['businessId'], extParams=param['extParams'], subPageId=param['subPageId'], posId=param[
                'posId'], pageId=param['pageId'], llsid=ad['llsid'], creativeId=ad['creativeId'],
            startTime=int(time()-30)*1000, endTime=int(time()))
        rjson = post(account, url, body=body, header=header)
        if(not rjson):
            continue
        if(rjson['result'] == 1):
            print("用户[{0}]看{1}成功：+{2}金币".format(account['basicInfo']
                  ['nickname'], param['name'], rjson['data']['neoAmount']))
            sleep(2)
            gameTask(account)
        else:
            print("用户[{0}]看{1}失败：{2}".format(account['basicInfo']
                  ['nickname'], param['name'], rjson['error_msg']))


# 激励游戏签到 同时检测是否有资格
def gameSignIn(account):
    url = "https://activity.e.kuaishou.com/rest/r/game/sign-in"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        account['basicInfo']['canRunGame'] = True
    else:
        account['basicInfo']['canRunGame'] = False
        print("用户[{0}]参与激励游戏失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 激励游戏-定时激励查询
def gameTimerInfo(account):
    url = "https://activity.e.kuaishou.com/rest/r/game/timer-reward/info"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1 and rjson['data']):
        flag = not rjson["data"]['lastTimerTime'] or rjson['data']['serverTime'] >= 60 * \
            1000*rjson['data']['minutesInterval'] + \
            rjson['data']['lastTimerTime']
        if(flag):
            gameTimerReward(account, rjson['data']['goldNum'])


# 激励游戏-定时激励领取
def gameTimerReward(account, amount):
    url = "https://activity.e.kuaishou.com/rest/r/game/timer-reward"
    rjson = post(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print(
            "用户[{0}]领取激励游戏定时激励成功：+{1}金币".format(account['basicInfo']['nickname'], amount))
    else:
        print("用户[{0}]领取激励游戏定时激励失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 激励游戏-用户信息
def gameUserInfo(account):
    url = "https://activity.e.kuaishou.com/rest/r/game/user/info"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]激励游戏：{1}钻石，{2}次抽奖机会".format(account['basicInfo']['nickname'], rjson['data']['userDiamondResult']['diamondPercent'],
                                                  rjson['data']['userDailyLotteryTimesResult']['remainTimes']))
        if(rjson['data']['userDailyLotteryTimesResult']['remainTimes'] > 0):
            gameWheel(account)


# 激励游戏-任务
def gameTask(account):
    url = "https://activity.e.kuaishou.com/rest/r/game/tasks"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        for task in rjson['data']['dailyTasks']:
            if(task['taskState'] == 1):
                gameTaskReward(account, task)
        for task in rjson['data']['growthTasks']:
            if(task['taskState'] == 1):
                gameTaskReward(account, task)


# 激励游戏-领取任务奖励
def gameTaskReward(account, task):
    url = "https://activity.e.kuaishou.com/rest/r/game/task/reward-receive?taskName={0}".format(
        task['taskName'])
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1 and rjson['data']['popUp']):
        print("用户[{0}]激励游戏领取[{1}]奖励：{2}".format(account['basicInfo']['nickname'],
              task['taskTitle'], rjson['data']['popUp']["taskRewardName"]))


# 激励游戏-抽奖
def gameWheel(account):
    url = "https://activity.e.kuaishou.com/rest/r/game/lottery?wheelVersion=1"
    rjson = post(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]激励游戏抽奖：{1}钻石+{2}金币".format(account['basicInfo']['nickname'],
              rjson['data']['diamondCount'], rjson['data']['coinCount']))
        gameTask(account)
        gameUserInfo(account)


# 周周赚-获取助力码
def getAssistCode(account):
    url = "https://nebula.kuaishou.com/rest/zt/encourage/assistance/detail?assistanceMetaId=2"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]获取周周赚助力码成功：{1}".format(account['basicInfo']
              ['nickname'], rjson['assistanceInfo']['assistanceId']))
        account['basicInfo']['assistanceId'] = rjson['assistanceInfo']['assistanceId']
    else:
        print("用户[{0}]获取周周赚助力码失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 周周赚-助力
def assist(fromAccount, toAccount):
    url = "https://nebula.kuaishou.com/rest/zt/encourage/assistance/friendAssist"
    if(not toAccount['basicInfo']['assistanceId']):
        print("用户[{0}]助力码不存在，助力失败".format(account['basicInfo']['nickname']))
        return
    body = {"assistanceId": toAccount['basicInfo']['assistanceId']}
    header = {"Content-Type": "application/json"}
    rjson = post(fromAccount, url, header=header, body=json.dumps(body))
    if(not rjson):
        return
    if("msg" in rjson):
        print("[{0}]-->[{1}]：{2}".format(fromAccount['basicInfo']
              ['nickname'], toAccount['basicInfo']['nickname'], rjson['msg']))
    else:
        print("[{0}]-->[{1}]：{2}".format(fromAccount['basicInfo']['nickname'],
              toAccount['basicInfo']['nickname'], rjson['error_msg']))


# 周周赚-助力详细
def assistDetail(account):
    url = "https://nebula.kuaishou.com/rest/zt/encourage/assistance/detail?assistanceMetaId=2"
    rjson = get(account, url)
    if(not rjson):
        return
    if(not rjson or "assistanceInfo" not in rjson):
        return
    print("用户[{0}]受助次数：{1}".format(account['basicInfo']
          ['nickname'], rjson['assistanceInfo']['assistedCount']))
    print("用户[{0}]积累金币：{1}".format(account['basicInfo']['nickname'],
          rjson['assistanceInfo']['accumulatedAmount']))
    print("用户[{0}]兑换金币：{1}".format(account['basicInfo']['nickname'],
          rjson['assistanceInfo']['accumulatedWithdraw']))
    stageAmount = rjson['assistanceInfo']['withdrawRule']['stageAmount']
    for amount in stageAmount:
        if(amount > rjson['assistanceInfo']['accumulatedWithdraw']):
            print("用户[{0}]当前阶段：{1}".format(
                account['basicInfo']['nickname'], amount))
            break


# 获取账号绑定情况
def getBindInfo(account):
    url = "https://www.kuaishoupay.com/pay/account/h5/provider/bind_info"
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    body = "account_group_key=NEBULA_CASH_ACCOUNT&bind_page_type=3"
    rjson = post(account, url, header=header, body=body)
    if(not rjson):
        return
    if(rjson['result'] == "SUCCESS"):
        account['bind'] = {"wechat": rjson['wechat_bind'],
                           "alipay": rjson['alipay_bind']}
        print("用户[{0}]提现账号绑定情况：微信{1}\t支付宝{2}".format(
            account['basicInfo']['nickname'], rjson['wechat_bind'], rjson['alipay_bind']))
    else:
        print("用户[{0}]获取提现绑定账号失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 更换金币兑换方式
def changeExchangeType(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/exchange/changeExchangeType"
    header = {"Content-Type": "application/json"}
    # 1自动兑换 2手动兑换
    body = {"type": 2}
    rjson = post(account, url, body=json.dumps(body), header=header)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]更换金币兑换方式成功：手动兑换".format(
            account['basicInfo']['nickname']))
    else:
        print("用户[{0}]更换金币兑换方式失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 查询可用金币
def coinOverview(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/exchange/coinToCash/overview"
    header = {"Content-Type": "application/json"}
    rjson = post(account, url, header=header)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        coinBalance = int(rjson['data']['coinBalance']) - \
            int(rjson['data']['coinBalance']) % 100
        if(coinBalance):
            print("用户[{0}]当前可兑换金币：{1}".format(
                account['basicInfo']['nickname'], coinBalance))
            coinSubmit(account, coinBalance)
        else:
            print("用户[{0}]当前可兑换金币不足".format(account['basicInfo']['nickname']))
    else:
        print("用户[{0}]查询可兑换金币失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 金币兑换
def coinSubmit(account, coinBalance):
    url = "https://nebula.kuaishou.com/rest/n/nebula/exchange/coinToCash/submit"
    header = {"Content-Type": "application/json"}
    body = {"coinAmount": coinBalance,
            "token": "rE2zK-Cmc82uOzxMJW7LI2-wTGcKMqqAHE0PhfN0U4bJY4cAM5Inxw"}
    rjson = post(account, url, body=json.dumps(body), header=header)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]金币兑换成功：{1}元".format(
            account['basicInfo']['nickname'], coinBalance/10000.0))
    else:
        print("用户[{0}]金币兑换失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


if __name__ == "__main__":
    #log()
    print("{0}{1}{0}".format(10*'*', projectNameCN))
    initEnv()

    print("\n\n{0}登录{0}".format(9*'='))
    for account in accounts:
        basicInfo = getBasicInfo(account)
        account['basicInfo'] = basicInfo

    # 日常任务
    for account in accounts:
        if("basicInfo" not in account or not account['basicInfo']['normal']):
            continue
        print("\n\n{0} {1} {0}".format(
            9*'=', account['basicInfo']['nickname']))
        # 签到
        getSignInfo(account)
        # 开宝箱
        boxInfo(account)
        # 获取任务进度
        getDailyTasks(account)
        # 激励游戏
        gameSignIn(account)
        if(account['basicInfo']['canRunGame']):
            gameTimerInfo(account)
            gameUserInfo(account)
            gameTask(account)

    print("\n\n{0}金币兑换{0}".format(9*'='))
    for account in accounts:
        if("basicInfo" not in account or not account['basicInfo']['normal']):
            continue
        changeExchangeType(account)
        coinOverview(account)

    print("\n\n{0}运行统计{0}".format(9*'='))
    for account in accounts:
        if("basicInfo" not in account or not account['basicInfo']['normal']):
            continue
        basicInfo = getBasicInfo(account)

    print("\n\n{0}绑定查询{0}".format(9*'='))
    for account in accounts:
        if("basicInfo" not in account or not account['basicInfo']['normal']):
            continue
        getBindInfo(account)
