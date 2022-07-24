# -*- encoding: utf-8 -*-
'''
@项目名称：   58tc.py
@项目地址：   https://gitee.com/wsfsp4/auto-py/tree/master
@创建时间：   2022/04/28 21:07:52
@创作者  ：   wsfsp4 
@版本号  ：   2.2
@功能描述：   
@更新时间：   2022/05/23 00:11:52
@更新内容：   新增每日抽奖、关注服务号功能;满足条件自动切换梦想小镇场景;不再自动报名报名打卡和挖矿
'''
import hashlib
import sys
import os.path
import json
from time import sleep, time
import requests


projectNameCN = "58同城"
projectNameEN = "58tc"
accounts = []

scenceList = [
    #{"desc": "梦想小镇离线收益翻倍", "id": 30},
    {"desc": "新手激励金币", "id": 13},
    #{"desc": "矿工鸡腿", "id": 20},
    #{"desc": "矿工金币", "id": 21},
    #{"desc": "梦想小镇免费得车/房", "id": 32, "perCount": 1},
    #{"desc": "梦想小镇加速次数", "id": 31, "perCount": 1},
    #{"desc": "神奇矿签到额外奖励", "id": 27},
    #{"desc": "神奇矿山偷矿次数", "id": 34},
    #{"desc": "梦想小镇骰子次数", "id": 1},
    #{"desc": "梦想小镇骰子得金币", "id": 2},
    #{"desc": "梦想小镇我的房金币", "id": 4},
    #{"desc": "梦想小镇我的车金币", "id": 5},
    #{"desc": "梦想小镇我的房10分钟金币", "id": 6},
    #{"desc": "梦想小镇我的车10分钟金币", "id": 7},
    #{"desc": "我的家金币", "id": 9},
]


def initEnv():
    global accounts
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\{0}.json".format(projectNameEN)
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
        tempCounts = []
        if("accounts" in projectConfig):
            tempCounts = projectConfig['accounts']
        else:
            # 改为覆盖写模式
            file = open(filePath, "w", encoding="utf-8")
            accounts = []
            count = 5
            while(count):
                accounts.append({"name": "", "cookie": ""})
                count -= 1
            projectConfig = {
                "accounts": accounts, "projectNameCN": projectNameCN}
            file.write(json.dumps(projectConfig, indent=2))
            print("当前项目未配置账号，脚本关闭")
            file.close()
            exit()

        for account in tempCounts:
            # 设置了名称和密钥的账号才算有效
            if(account['name'] and account['cookie']):
                accounts.append(account)

        if(len(accounts) > 0):
            print("账号个数：{0}".format(len(accounts)))
        else:
            print("未发现有效账号，脚本结束")
            exit()

    else:
        # 创建配置文件
        file = open(filePath, "w", encoding="utf-8")
        accounts = []
        count = 5
        while(count):
            accounts.append({"name": "", "cookie": ""})
            count -= 1
        projectConfig = {
            "accounts": accounts, "projectNameCN": projectNameCN}
        file.write(json.dumps(projectConfig, indent=2))
        print("当前项目未配置账号，脚本关闭")
        file.close()
        exit()


# 签名函数
def MD5(s):
    hl = hashlib.md5()
    hl.update(s.encode(encoding='utf8'))
    md5 = hl.hexdigest()
    return str(md5)


# 统一GET 额外header用字典传递
def get(account, url, header=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account['cookie']
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
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
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


# 检查用户状态
def checkUserState(account):
    url = "https://magicisland.58.com/web/mineral/userInfo"
    rjson = get(account, url)
    if(rjson['code'] == 0):
        account['normal'] = True
        print("用户[{0}]黑名单：{1}".format(
            account['name'], rjson['result']['incrBlackUser']))
        print("用户[{0}]灰名单：{1}".format(
            account['name'], rjson['result']['grayUser']))
    else:
        account['normal'] = False
        print("用户{0}查询状态失败：{0}".format(rjson['message']))


# 获取任务列表
def getTaskList(account, scence):
    url = "https://taskframe.58.com/web/task/dolist?sceneId={0}&openpush=1&source=".format(
        scence['id'])
    rjson = get(account, url)
    taskList = []
    if(rjson['code'] == 0):
        if(rjson['result']['taskList']):
            for task in rjson['result']['taskList']:
                # 梦想小镇10分钟金币任务获取没有任务总次数 因此把没有次数的任务也加入
                # status: 0 - 未完成，1 - 已完成，2 - 已领取
                if(task['status'] == 0):
                    # 有些场景任务每次运行只获取指定数量的任务
                    if("perCount" in scence and scence['perCount'] >= len(taskList)):
                        continue
                    taskList.append(task['itemId'])
                if(task['status'] == 1):
                    getReward(account, scence, task['itemId'])

    else:
        print("用户[{0}]获取任务列表[{1}]失败：{2}".format(
            account['name'], scence['id'], rjson['message']))
    return taskList


# 任务入口
def doTasks(account):
    for scence in scenceList:
        taskIdList = getTaskList(account, scence)
        for taskId in taskIdList:
            doTask(account, scence, taskId)


# 提交任务 提交成功则执行领取奖励
def doTask(account, scene, taskId):
    timestamp = int(time()*1000)
    signFrom = "{0}{1}".format(timestamp, taskId)
    url = "https://taskframe.58.com/web/task/dotask?taskData=15&timestamp={0}&sign={1}&taskId={2}".format(
        timestamp, MD5(signFrom), taskId)

    rjson = get(account, url)
    if(rjson['code'] == 0 and rjson['message'] == "成功"):
        print("用户[{0}]完成任务[{1}-{2}]成功".format(account['name'],
              scene['desc'], taskId))
        getReward(account, scene, taskId)
        # 休眠一会，防止出现任务提交频繁
        print("---->休息20s，长久发展^_^")
        sleep(20)
        return True
    else:
        print("用户[{0}]完成任务[{1}-{2}]失败：{3}".format(account['name'],
              scene['desc'], taskId, rjson['message']))
        return False


# 领取任务奖励 有些奖励次数的任务会出现领取失败的情况
def getReward(account, scene, taskId):
    timestamp = int(time()*1000)
    signFrom = "{0}{1}".format(timestamp, taskId)
    url = "https://taskframe.58.com/web/task/reward?timestamp={0}&sign={1}&taskId={2}".format(
        timestamp, MD5(signFrom), taskId)
    rjson = get(account, url)
    if(rjson['code'] == 0):
        print("用户[{0}]领取任务[{1}-{2}]奖励成功".format(account['name'],
              scene['desc'], taskId))
        return True
    else:
        print("用户[{0}]领取任务[{1}-{2}]奖励失败：{3}".format(account['name'],
              scene['desc'], taskId, rjson['message']))
        return False


# 获取每日抽奖信息
def rouletteInfo(account):
    url = "https://magicisland.58.com/web/roulette/info"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['code'] == 0 and rjson['result']):
        times = rjson['result']['times']
        if(times > 1):
            for index in range(0, times):
                roulette(account)
                sleep(0.5)
        else:
            print("用户[{0}]每日抽奖已完成".format(account['name']))
    else:
        print("用户[{0}]获取每日抽奖信息失败：{1}".format(
            account['name'], rjson["message"]))


# 每日抽奖抽奖
def roulette(account):
    url = "https://magicisland.58.com/web/roulette/luckyDraw?setNum=2"
    header = {
        "referer": "https://magicisland.58.com/web/v/turntablelottery?os=android"}
    rjson = get(account, url, header=header)
    if(not rjson):
        return
    if(rjson['code'] == 0):
        if(rjson['result']['type'] == 2):
            print("用户[{0}]每日抽抽奖成功：抽到矿石！".format(account['name']))
            rouletteReward(account, rjson['result']['awardId'])
        else:
            print("用户[{0}]每日抽抽奖成功：未抽到矿石".format(account['name']))
    else:
        print("用户[{0}]每日抽抽奖失败：{1}".format(
            account['name'], rjson["message"]))


# 领取每日抽奖矿石奖励
def rouletteReward(account, id):
    url = "https://magicisland.58.com/web/roulette/receiveOre?id={0}".format(
        id)
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['code'] == 0):
        print("用户[{0}]领取抽奖奖励成功".format(account['name']))
    else:
        print("用户[{0}]领取抽奖奖励失败：{1}".format(account['name'], rjson["message"]))


# 获取服务号列表
def getRecFollowList(account):
    url = "https://messcenter.58.com/app/service/aggregation/recommendation?pageNum=1&queryFollowType=1"
    rjson = get(account, url)
    if(not rjson or rjson['msg'] != 'success'):
        return
    for data in rjson['data']:
        follow(account, data['serviceId'])
        sleep(1.5)


# 关注服务号
def follow(account, serviceId):
    url = "https://messcenter.58.com/app/service/follow"
    header = {"content-type": "application/x-www-form-urlencoded"}
    body = "serviceId={0}&type=1".format(serviceId)
    rjson = post(account, url, header=header, body=body)
    if(not rjson or rjson['msg'] != 'success'):
        return
    print("用户[{0}]关注服务号[{1}]成功".format(account['name'], serviceId))


# 神奇矿主页
def mainHome(account):
    url = "https://magicisland.58.com/web/mineral/main?openSettings=1"
    header = {"Referer": "https://magicisland.58.com/web/v/home?os=android"}
    rjson = get(account, url, header)
    if(rjson['code'] == 0):
        print("用户[{0}]矿石余额：{1} ≈ {2}元".format(account['name'], rjson['result']
              ['userInfo']['minerOre'], rjson['result']['userInfo']['minerOreValue']))

        # 签到
        if(rjson['result']['tasks']['sign']['state'] == 0):
            mainSign(account)
            share(account)
        else:
            print("用户[{0}]签到状态：已签到".format(account['name']))

        # 采集神奇矿
        if(rjson['result']['userInfo']['dailyOre'] == 0):
            mainDailyOre(account)
        else:
            print("用户[{0}]神奇矿采集：已采集".format(account['name']))

        # 小游戏
        gameProcess = rjson['result']['games']['gameProcess']
        print("用户[{0}]小游戏进度：{1}/{2}".format(account['name'],
              gameProcess['joinedNum'], gameProcess['gameNum']))
        if(gameProcess['awardState'] == 0 and gameProcess['joinedNum'] == gameProcess['gameNum']):
            mainGameReward(account, gameProcess['awardOre'])

        # 浏览租房
        mainRent(account)

    else:
        print("用户[{0}]查询神奇矿主页失败：{1}".format(account['name'], rjson['message']))


# 神奇矿每日矿石采集
def mainDailyOre(account):
    url = "https://magicisland.58.com/web/mineral/dailyore"
    rjson = get(account, url)
    if(rjson['code'] == 0):
        print("用户[{0}]神奇矿采集成功".format(account['name']))
    else:
        print("用户[{0}]神奇矿采集失败：{1}".format(account['name'], rjson['message']))


# 神奇矿主页小游戏完成奖励领取
def mainGameReward(account, num):
    url = "https://magicisland.58.com/web/mineral/gameprocessore"
    rjson = get(account, url)
    if(rjson['code'] == 0):
        print("用户[{0}]领取小游戏奖励成功：获取{1}矿石".format(account['name'], num))
    else:
        print("用户[{0}]领取小游戏奖励失败：{1}".format(account['name'], rjson['message']))


# 神奇矿-签到
def mainSign(account):
    url = "https://magicisland.58.com/web/sign/signInV2?sessionId=&successToken=&scene=null"
    rjson = get(account, url)
    if(rjson['code'] == 0):
        print("用户[{0}]神奇矿签到成功：获得{1}矿石 ≈ {2}".format(
            account['name'], rjson['result']['ore'], rjson['result']['amount']))
    else:
        print("用户[{0}]神奇矿签到失败：{1}".format(account['name'], rjson['message']))


# 神奇矿-签到额外任务进度查询
def mainSignExtra(account):
    url = "https://magicisland.58.com/web/sign/signInfo"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account['cookie']}
    res = requests.get(url=url, headers=header)
    rjson = res.json()

    if(rjson['code'] == 0):
        if(float(rjson['result']['continueOre'])):
            print("用户[{0}]神奇矿签到额外任务可获取：{1}矿石".format(
                account['name'], rjson['result']['continueOre']))
        else:
            print("用户[{0}]神奇矿签到额外任务：已完成".format(account['name']))
    else:
        print("用户[{0}]获取神奇矿签到额外任务失败：{1}".format(
            account['name'], rjson['message']))


# 神奇矿-打开租房界面奖励(貌似没有效果)
def mainRent(account):
    url = "https://magicisland.58.com/web/task/callback/common/rent"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account['cookie']}
    res = requests.post(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]领取浏览租房界面奖励成功".format(account['name']))
    else:
        print("用户[{0}]领取浏览租房界面奖励失败：{1}".format(
            account['name'], rjson['message']))


# 矿工-信息
def mineInfo(account):
    url = "https://dreamtown.58.com/web/mine/maininfo?collect=true"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        # 矿工余额
        userInfo = rjson['result']['userInfo']
        print("用户[{0}]矿工矿石余额：{1}".format(
            account['name'], userInfo['totalOre']))
        print("用户[{0}]矿工金币余额：{1}".format(account['name'], userInfo['coin']))
        print("用户[{0}]矿工鸡腿数量：{1}".format(
            account['name'], userInfo['drumstickCount']))
        if(userInfo['drumstickCount'] >= userInfo['drumstickConsumeNum']):
            print("用户[{0}]矿工鸡腿数量充足,开始吃鸡!".format(account['name']))
            mineDrumStick(account)

        # 矿工离线产量
        mineInfo = rjson['result']['mineInfo']
        print("用户[{0}]矿工离线产矿：{1}".format(
            account['name'], mineInfo['mineCarOre']))
        if(float(mineInfo['mineCarOre'])):
            mineRevenue(account)

        # 收矿积累奖励
        withdraw = rjson['result']['withdraw']
        print("用户[{0}]矿工阶段奖励：{1}/{2}\t{3}元".format(account['name'],
              withdraw['accumulateOre'], withdraw['maxOre'], withdraw['currentAmount']))
        if(float(withdraw['accumulateOre']) >= float(withdraw['maxOre'])):
            mineWithdraw(account, withdraw)

        # 召唤金币矿工
        machineInfo = rjson['result']['machineInfo']
        if(machineInfo['freeFirstTime']):
            print("用户[{0}]开始召唤免费金币矿工".format(account['name']))
            mineOpen(account)
        else:
            print("用户[{0}]已召唤过免费金币矿工".format(account['name']))

        # 金币处理(优先召唤一个矿工,最多召唤3个，多了不划算,多余则升级矿工)
        updateInfo = rjson['result']['updateInfo']
        print("用户[{0}]当前临时矿工数：{1}".format(
            account['name'], updateInfo['currentEmployMinerNum']))
        print("用户[{0}]当前矿工装备等级：{1}/{2}".format(account['name'],
              updateInfo['equipmentLevel'], updateInfo['equipmentLevelLimit']))

        toEmploy = (updateInfo['currentEmployMinerNum'] < 3 and int(
            updateInfo['employMinerConsumeCoinNum']) <= int(userInfo['coin']))
        if(toEmploy):
            print("用户[{0}]当前未雇佣临时矿工且金币充足，开始雇佣".format(account['name']))
            mineEmploy(account)

        toUpgrade = int(userInfo['coin']) >= int(
            updateInfo['employMinerConsumeCoinNum']) + int(updateInfo['employMinerUpgradeCostNumber'])
        if(toUpgrade):
            print("用户[{0}]金币充足,升级矿工装备".format(account['name']))
            mineUpgrade(account)
    else:
        print("用户[{0}]获取矿工信息失败：{1}".format(account['name'], rjson['message']))


# 矿工-召唤
def mineOpen(account):
    url = "https://dreamtown.58.com/web/machine/open"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]召唤矿工成功".format(account['name']))
    else:
        print("用户[{0}]召唤矿工失败：{1}".format(account['name'], rjson['message']))


# 矿工-收矿
def mineRevenue(account):
    url = "https://dreamtown.58.com/web/mine/offlineRevenue"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]矿工收矿成功".format(account['name']))
    else:
        print("用户[{0}]矿工收矿失败：{1}".format(account['name'], rjson['message']))


# 矿工-吃鸡腿
def mineDrumStick(account):
    url = "https://dreamtown.58.com/web/mine/drumstick"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]吃鸡成功".format(account['name']))
    else:
        print("用户[{0}]吃鸡失败：{1}".format(account['name'], rjson['message']))


# 矿工-雇佣
def mineEmploy(account):
    url = "https://dreamtown.58.com/web/mine/employ"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]雇佣临时矿工成功".format(account['name']))
    else:
        print("用户[{0}]雇佣临时矿工失败：{1}".format(account['name'], rjson['message']))


# 矿工-升级
def mineUpgrade(account):
    url = "https://dreamtown.58.com/web/mine/upgrade"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]矿工装备升级成功".format(account['name']))
        print(rjson)
    else:
        print("用户[{0}]矿工装备升级失败：{1}".format(account['name'], rjson['message']))


# 矿工-兑换现金
def mineWithdraw(account, info):
    url = "https://dreamtown.58.com/web/withdraw/ore"
    rjson = get(account, url)
    if(rjson['code'] == 0):
        print("用户[{0}]矿工兑换现金成功：+{1}元".format(account['name'],
              info['currentAmount']))
    else:
        print("用户[{0}]矿工兑换现金失败：{1}".format(account['name'], rjson['message']))


# 神奇矿山用户信息（不再自动召唤，只进行收矿）
def miningUserInfo(account):
    url = "https://magicisland.58.com/web/mining/userInfo"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        # 收取矿石
        if(rjson["result"]['grantList']):
            for grant in rjson["result"]['grantList']:
                miningGain(account, grant['id'])
                sleep(0.5)
        # 召唤小帮手
        if(rjson['result']['status'] == 0):
            if(float(rjson['result']['usableOre']) >= float(rjson['result']['threshold'])):
                #miningEnroll(account)
                pass
            else:
                print("用户[{0}]矿石余额少于{1},无法召唤小帮手".format(
                    account['name'], rjson['result']['threshold']))
        else:
            print("用户[{0}]神奇矿山已召唤小帮手".format(account['name']))
    else:
        print("用户[{0}]查询神奇矿山主页失败：{0}".format(
            account['name'], rjson['message']))


# 神奇矿山收矿
def miningGain(account, mineID):
    url = "https://magicisland.58.com/web/mining/gain?id={0}".format(mineID)
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]神奇矿山成功收取矿石：{1}".format(
            account['name'], rjson['result']['gainOre']))
    else:
        print("用户[{0}]神奇矿山收取矿石失败：{1}".format(
            account['name'], rjson['message']))


# 神奇矿山召唤小帮手
def miningEnroll(account):
    url = "https://magicisland.58.com/web/mining/enroll"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]神奇矿山召唤小帮手成功".format(
            account['name']))
    else:
        print("用户[{0}]神奇矿山召唤小帮手失败：{1}".format(
            account['name'], rjson['message']))


# 神奇矿山偷矿列表 有次数则执行偷矿(偷矿失败则是需要做任务 等下次运行做了任务再偷)
def miningStealList(account):
    url = "https://magicisland.58.com/web/mining/strangerInfo"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        strangerList = rjson['result']['strangerList']
        if(len(strangerList) == rjson['result']['strangerCurrent']):
            print("用户[{0}]今日偷矿次数已用完".format(account['name']))
        else:
            for stranger in strangerList:
                if(stranger['status'] == 0):
                    if(miningSteal(account, stranger['id'])):
                        break
    else:
        print("用户[{0}]获取神奇矿山陌生人列表失败：{1}".format(
            account['name'], rjson['message']))


# 神奇矿山偷矿 需要先做任务则返回True(若做任务失败则偷矿会失败，一般运行一次就可以偷一次)
def miningSteal(account, strangerID):
    url = "https://magicisland.58.com/web/mining/stealStranger?id={0}".format(
        strangerID)
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        if(rjson['result']['state'] == 0):
            print("用户[{0}]神奇矿山偷矿成功：{1}矿石".format(
                account['name'], rjson['result']['ore']))
        elif(rjson['result']['state'] == 1):  # 重复偷
            print("用户[{0}]神奇矿山偷矿失败：{1}".format(
                account['name'], rjson['result']['message']))
        elif(rjson['result']['state'] == 2):  # 需要做任务获取次数
            print("用户[{0}]神奇矿山偷矿失败：{1}".format(
                account['name'], rjson['result']['message']))
    else:
        print("用户[{0}]神奇矿山偷矿失败：{1}".format(account['name'], rjson['message']))


# 我的家主页
def houseInfo(account):
    url = "https://lovely-house.58.com/web/main/mainInfo"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0 and "result" in rjson and "userInfo" in rjson['result'] and rjson['result']['userInfo']):
        print("用户[{0}]我的家金币数量：{1}".format(
            account['name'], rjson['result']['userInfo']['coin']))
        print("用户[{0}]我的家清洁天数：{1}".format(account['name'],
              rjson['result']['userInfo']['totalCleanDays']))
        signState = rjson['result']['redPoint']['sign']
        if(signState):
            print("用户[{0}]我的家签到状态：已签到".format(account['name']))
        else:
            print("用户[{0}]我的家签到状态：未签到".format(account['name']))
            houseSign(account)
        fortuneCatCoin = rjson['result']['userInfo']['fortuneCatCoin']
        if(fortuneCatCoin and "totalAmount" in fortuneCatCoin):
            print("用户[{0}]我的家猪罐生产状态：{1}/{2}".format(account['name'],
                  fortuneCatCoin['totalAmount'], fortuneCatCoin['limitAmount']))
            # 收集
            if(int(fortuneCatCoin['totalAmount'])):
                houseCollect(account)
    else:
        print("用户[{0}]查询我的家主页失败：{1}".format(account['name'], rjson['message']))


# 我的家签到
def houseSign(account):
    url = "https://lovely-house.58.com/sign/signin"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.post(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]我的家签到成功：获得{1}金币".format(
            account['name'], rjson['result']['gold']))
    else:
        print("用户[{0}]我的家签到失败：{1}".format(account['name'], rjson['message']))


# 我的家-查看家务
def houseWork(account):
    url = "https://lovely-house.58.com/housework/get"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        tasks = rjson['result']['houseworkTaskVOList']
        if(len(tasks)):
            print("用户[{0}]我的家发现家务：{1}".format(
                account['name'], tasks[0]['tip']))
            houseWorkClean(account, tasks[0])
        else:
            print("用户[{0}]我的家暂无可做家务".format(account['name']))
    else:
        print("用户[{0}]获取我的家家务失败：{1}".format(account['name'], rjson['message']))


# 我的家-清理家务
def houseWorkClean(account, task):
    url = "https://lovely-house.58.com/housework/clean"
    body = "furnitureId={0}".format(task['furnitureId'])
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.post(url=url, headers=header, data=body)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]我的家做家务成功：{1}".format(account['name'], task['okMsg']))
    else:
        print("用户[{0}]我的家做家务失败：{1}".format(account['name'], rjson['message']))


# 我的家-家务清单
def houseWorkState(account):
    url = "https://lovely-house.58.com/housework/list"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        items = rjson['result']['items']
        for item in items:
            print("用户[{0}]我的家家务[{1}]：{2}".format(
                account['name'], item['taskName'], item['btnTitle']))
            # state 1进行中 2领取奖励 3已完成
            if(item['state'] == 2):
                # 未解密
                pass
    else:
        print("用户[{0}]查询我的家家务状态列表失败：{1}".format(
            account['name'], rjson['message']))


# 我的家-收集猪罐
def houseCollect(accout):
    url = "https://lovely-house.58.com/fortunecat/collect"
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    body = "_d=ff08790dd0116146b1cdead4a1fe07a3eyZgaXFwfW5wRVpNXRYCHjsYajklPTwAQl40TiwoJF7CtMKzwrzCtcKkw7bCqMKtwo3DgMOJw4%2FDkcKZwozCj8OxwqXDpcKtw6DDpcOvw7HDk8ORw53Cj8OIwpbCnMOIxLHFp8SxxarFjMWIxYTEvsW8xIbEhMWwxJLFgsWUxZPEo8SlxKTEpcS0xIjFusWmxLzFhsS0xLDErMWWxKTEoMecxqbHlMauxrzHiMa6x6rHhceWx5vHhcefx5rHpMaex7rGmMeqxpDGjMaIx7rHrceRx4rHm8eCx4XGqMakxqDIosmYyKrIoMmMyLbJq8m%2FyYHJiMmNybDIksiOyaTInsicyJjIlMmuyaHIiMiEyIDJgsi4yYrJgMisyZbIl8iMy6XLqsu9y6jLucuwy4TKvsqay7jKisuwy6zLqMqay5vKtcqhyrvKuMqxyrfLqcupy5jLlsqJy5TLgcuBy47KmMy0zLzMscy4zKnNssyozKnMmMySzJHMnMyDzIbNm8yKzbjNtMyuzKnMjMyIzITNvsy8zYbNhMywzZLMl8yRzJjPnM6mzrLPkM6yz4jPhM%2BAzoLOlc6fzp7PrM%2Boz6TOns6cz6bPpM6Qz7LOoc6xzrjOvM%2BGz5LOsM%2BSzqjOpM6g0KLQvNC%2F0L3QqNCg0KvQrNCT0JHQkdCV0IPQgtCM0aDQnNCY0arQkNGy0bjQhNG%2B0InQgNGd0ZTQrNGW0YLQoNKi04fTuNOd05TTjNOf05bTltKd04LTptOX07PTstOy0rHSlNK%2F07XSgtKV0r%2FSgNOC0pnTitOA05LSldKd0o%2FVq9Wh1bHVnNWx1abVudWx1ILUntSK1ZfVrNSW1ZHVkdSl1K3UlNWu1arUiNW61IDVgtWI1LTVjtSF1J3UnNSg1qLWvteU1q7XjNeI14TWvtaY1pPWmdaU1oTWh9aI1o%2FXtde917HXv9em16DWhNaA1rzXhta0147XnNao15rWjNmy2avZrNm52bPZoNmE2L7Ymtm42IrZsNms2ajYmtiJ2bjYpdi42LzYjNiI2ITZvti82YbZhNiw2ZLYgtid2I7bs9ut26fbotuM2rbaotuA2oLbuNu027DaktqF2onaktuz26rbvdqQ2ozaiNu62oDbgtuI2rTbjtqA2pjamdqI3abdq9263aHdjNy23KLdgNyC3bjdtN2w3JLdld2W3Zjcstyr3KHcqNyM3IjchN2%2B3Lzdht2E3LDdktyV3JTcm9%2Bc3qbest%2BQ3rLfot6r34Degt6I37Tejt%2BE353fld%2BZ3rPesN6p3qHeoN6I37rfpt6834bfmd%2Ba34Xfhd%2BN34zgoLTgoLzgoLngoL3goKjgoKHgoK7goYDgoILgoIjgobTgoI7goYTgoZvgoZPgoZngoK7goJjgoargobbgoIzgobbgoIDgoJ3goLbgoJDgoJrgoL%2FgoKDgoYLgoJngoK3go5fgo7Dgo6bgo6vgo77go7Pgo4%2Fgo5Hgo4bgopHgo43go63go6fgooHgo5LgoongoqHgo7Hgoqbgo7jgorzgorPgoq7gorjgopXgoqrgoo7go5vgoorgo4zgopbgor7gpbngpYXgpargpLngpbLgpKDgpbbgpavgpYHgpbXgpYrgpZvgpZrgpYPgpZHgpb3gpKHgpJXgpIDgpbHgpJrgpIzgpLTgpJPgpI7gpJDgpIrgpZvgpKngpLXgpKTgpZ7gp73gpqbgp7U%3D%7CdG58P3pKaz9sTnF1ZzhqYFRQejVFhEdTe1BpM0pDTF9OPFQ7ZHc7XT9tf2laNXyISkI-aVt-TFF_P1Z_XGR_Ql1jQzt0VzpYU3Y-XmFVelx9QWRlQmtXPF-BgzpEakhnenSEcUV6a1hbPzcyTDJgS3Y9RFRdels6PUxLOWh8WYQ4QHQ9PUhnaD04cDp6NEZybWtyaUpINjc4bj86Sjx1Qn9fhTxIfE5HOGpRZ0gvjWk%3D%7CxWzvDxY8YU8neyrtaDrlT88ky5RbNL6ZqwUhiBb2nDuL5OdTGH2KgoEjdU6u18Xr"
    rjson = post(account, url, body=body, header=header)
    if(not rjson):
        return
    if(rjson['code'] == 0):
        print("用户[{0}]我的家收集猪罐成功：获得{1}金币".format(
            account['name'], rjson['result']))
    else:
        print("用户[{0}]我的家收集猪罐失败：{1}".format(account['name'], rjson['message']))


# 我的家兑换信息查询
def houseWithdrawPage(account):
    url = "https://lovely-house.58.com/web/exchange/info"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        oreList = rjson['result']['oreList']
        if(oreList[len(oreList)-1]['oreStatus'] == 0 and rjson['result']['coin'] >= int(oreList[len(oreList)-1]['coin'])):
            houseWithdraw(account, oreList[len(oreList)-1])
    else:
        print("用户[{0}]查询我的家兑换页失败：{1}".format(
            account['name'], rjson['message']))


# 我的家金币兑换矿石
def houseWithdraw(account, item):
    url = "https://lovely-house.58.com/web/exchange/ore"
    body = "id={0}".format(item['id'])
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.post(url=url, headers=header, data=body)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]我的家兑换矿石成功：{1} ≈ {2}元".format(
            account['name'], item['amount'], item['money']))
    else:
        print("用户[{0}]我的家兑换矿石失败：{1}".format(account['name'], rjson['message']))


# 梦想小镇-场景信息查询
def dreamtownScence(account):
    url = "https://dreamtown.58.com/web/dreamtown/maininfo?receive=coin&initialization=1"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.get(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        # 场景等级
        print("用户[{0}]梦想小镇[我的车]等级：{1}".format(
            account['name'], rjson['result']['levelInfo']['car']))
        print("用户[{0}]梦想小镇[我的房]等级：{1}".format(
            account['name'], rjson['result']['levelInfo']['house']))
        # 场景信息
        sceneName = ["我的房", '我的车']
        userInfo = rjson['result']['userInfo']
        gameScene = userInfo['gameScene']
        print("用户[{0}]梦想小镇当前场景：{1}".format(
            account['name'], sceneName[gameScene-1]))
        print("用户[{0}]梦想小镇当前场景财富：{1} 金币".format(
            account['name'], userInfo['coin']))
        print("用户[{0}]梦想小镇当前场景产率：{1} 金币/秒".format(account['name'],
              userInfo['coinSpeed']))
        if(gameScene == 1 and rjson['result']['levelInfo']['house'] > 15):
            dreamtownSwitch(account)
    else:
        print("用户[{0}]查询梦想小镇场景失败：{1}".format(
            account['name'], rjson['message']))


# 梦想小镇-切换场景(车)
def dreamtownSwitch(account):
    url = "https://dreamtown.58.com/web/dreamtown/switch"
    body = "target=2"
    header = {"content-type": "application/x-www-form-urlencoded;charset=UTF-8"}
    rjson = post(account, url, body=body, header=header)
    if(not rjson):
        return
    if(rjson['code'] == 0):
        print("用户[{0}]切换场景成功".format(account['name']))
    else:
        print("用户[{0}]切换场景失败：{1}".format(account['name'], rjson['message']))


# 梦想小镇-签到
def dreamtownSign(account):
    url = "https://dreamtown.58.com/web/dreamtown/sign/getaward"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "cookie": account["cookie"]}
    res = requests.post(url=url, headers=header)
    rjson = res.json()
    if(rjson['code'] == 0):
        print("用户[{0}]梦想小镇签到成功".format(account['name']))
    else:
        print("用户[{0}]梦想小镇签到失败：{1}".format(account['name'], rjson['message']))


# 梦想小镇-查询骰子状态
def dreamtownMonopolyInfo(account):
    url = "https://dreamtown.58.com/web/dreamtown/monopoly/info"
    rjson = get(account, url)
    if(rjson['code'] == 0):
        timesInfo = rjson['result']['timesInfo']
        print("用户[{0}]梦想小镇可摇骰子次数：{1}".format(
            account['name'], timesInfo['usableTimes']))
        dreamtownMonopolyRoll(account)
        sleep(2)
    else:
        print("用户[{0}]梦想小镇查询骰子状态失败：{1}".format(
            account['name'], rjson['message']))


# 梦想小镇-摇骰子
def dreamtownMonopolyRoll(account):
    url = "https://dreamtown.58.com/web/dreamtown/monopoly/rolldice"
    rjson = post(account, url)

    if(rjson['code'] == 0):
        # 金币、次数和现金
        print("用户[{0}]梦想小镇摇骰子成功：获得{1}金币（或次数或其他）".format(
            account['name'], rjson['result']['award']['data']))
        print("用户[{0}]梦想小镇可摇骰子次数：{1}".format(account['name'],
              rjson['result']['timesInfo']['usableTimes']))
        # 有次数则递归执行
        if(rjson['result']['timesInfo']['usableTimes']):
            sleep(2)
            dreamtownMonopolyRoll(account)
    else:
        print("用户[{0}]梦想小镇摇骰子失败：{1}".format(account['name'], rjson['message']))


# 梦想小镇-模拟操作总入口
def dreamtownEnter(account):
    # 宝箱
    dreamtownOpenEnter(account)
    # 合成
    dreamtownCompoundEnter(account)
    # 卖出
    dreamtownSellEnter(account)
    # 空投
    dreamtownFall(account)
    # 宝箱
    dreamtownOpenEnter(account)
    # 合成
    dreamtownCompoundEnter(account)
    # 卖出
    dreamtownSellEnter(account)
    # 买入
    dreamtownBuyEnter(account)


# 梦想小镇-开宝箱入口
def dreamtownOpenEnter(account):
    url = "https://dreamtown.58.com/web/dreamtown/maininfo?initialization=1"
    rjson = get(account, url)
    if(not rjson):
        return
    locations = list(rjson['result']['locationInfo'].values())
    for location in locations:
        if(location and location['state'] == 1):
            print("用户[{0}]梦想小镇发现宝箱".format(account['name']))
            dreamtownOpen(account, location['locationIndex'])


# 梦想小镇-开宝箱
def dreamtownOpen(account, index):
    url = "https://dreamtown.58.com/web/dreamtown/open"
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://dreamtown.58.com/web/v/dreamtown?from=magicisland&taskname=magicisland&os=android"
    }
    body = "locationIndex={0}".format(index)
    rjson = post(account, url, body=body, header=header)
    if(not rjson):
        return
    if(rjson['code'] == 0):
        print("用户[{0}]梦想小镇开宝箱成功：{1}".format(
            account['name'], rjson['result']['name']))
    else:
        print("用户[{0}]梦想小镇开宝箱失败：{1}".format(account['name'], rjson['message']))


# 梦想小镇-合成入口
def dreamtownCompoundEnter(account):
    url = "https://dreamtown.58.com/web/dreamtown/maininfo?initialization=1"
    # 循环合成 最多合成11次
    times = 11
    # 如果发生过合成 则置为True
    isCompound = False
    while(times):
        times -= 1
        rjson = get(account, url)
        if(not rjson):
            return
        locations = list(rjson['result']['locationInfo'].values())
        # 寻找相同等级,每次只合成一次
        p = 0
        while(p < 11):
            fromLo = locations[p]
            # 避开宝箱类型和空位置
            if(not fromLo or fromLo['state'] == 1):
                p += 1
                continue
            pp = p+1
            flag = False
            while(pp < 12):
                toLo = locations[pp]
                # 避开宝箱类型和空位置
                if(not toLo or toLo['state'] == 1):
                    pp += 1
                    continue
                if(fromLo['level'] == toLo['level']):
                    dreamtownCompound(
                        account, fromLo['locationIndex'], toLo['locationIndex'])
                    isCompound = True
                    flag = True
                    break
                pp += 1
            # 若合成 则进入下一轮合成
            if(flag):
                break
            p += 1
        # 未合成过则退出合成
        if(not isCompound):
            break
        sleep(1.5)


# 梦想小镇-合成
def dreamtownCompound(account, fromId, toId):
    url = "https://dreamtown.58.com/web/dreamtown/compound"
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://dreamtown.58.com/web/v/dreamtown?from=magicisland&taskname=magicisland&os=android"
    }
    body = "fromId={0}&toId={1}".format(fromId, toId)
    rjson = post(account, url, body=body, header=header)
    if(not rjson):
        return

    if(rjson['code'] == 0):
        print("用户[{0}]梦想小镇合成车/房成功：{1}级".format(account['name'],
              rjson['result']['level']))
    else:
        print("用户[{0}]梦想小镇合成车/房失败：{1}".format(account['name'], rjson['message']))


# 梦想小镇-卖出入口
def dreamtownSellEnter(account):
    url = "https://dreamtown.58.com/web/dreamtown/maininfo?initialization=1"
    rjson = get(account, url)
    if(not rjson):
        return
    level = int(rjson['result']['userInfo']['level'])
    locations = list(rjson['result']['locationInfo'].values())
    for location in locations:
        # 小于当前等级4级则卖出
        if(location and location['level']+4 < level):
            dreamtownSell(account, location)


# 梦想小镇-卖出
def dreamtownSell(account, location):
    url = "https://dreamtown.58.com/web/dreamtown/sell"
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://dreamtown.58.com/web/v/dreamtown?from=magicisland&taskname=magicisland&os=android"
    }
    body = "locationIndex={0}".format(location['locationIndex'])
    rjson = post(account, url, body=body, header=header)
    if(not rjson):
        return

    if(rjson['code'] == 0):
        print("用户[{0}]梦想小镇卖出{1}级车/房成功：获得{2}金币".format(account['name'],
              location['level'], rjson['result']['coin']))
    else:
        print("用户[{0}]梦想小镇卖出车/房失败：{1}".format(account['name'], rjson['message']))


# 梦想小镇-买入入口(只购等级差4以内的,边买边合成直到金币不足)
def dreamtownBuyEnter(account):
    url_info = "https://dreamtown.58.com/web/dreamtown/maininfo?initialization=1"
    url_store = "https://dreamtown.58.com/web/dreamtown/store"
    while(not dreamtownFull(account)):
        # 获取等级
        rjson = get(account, url_info)
        if(not rjson):
            return
        currentLevel = int(rjson['result']['userInfo']['level'])
        # 获取金币和商店信息
        rjson = get(account, url_store)
        if(not rjson):
            return
        allCoin = int(rjson['result']['allCoin'])
        elements = rjson['result']['elements']
        length = len(elements)-1
        # 一个循环只能购买一次 因为购买后车/房的价格已变化
        while(length >= 0):
            element = elements[length]
            # 未解锁的会出现价格为空的情况
            # 相差小于4级(新手出现小于4级，非新手最小差4级)
            if(element['price'] and (element['level'] >= (currentLevel-4)) and (int(element['price']) <= allCoin)):
                dreamtownBuy(account, element['level'])
                break
            elif(element['price'] and (element['level'] == (currentLevel-5)) and (int(element['price'])*2.5 <= allCoin)):
                dreamtownBuy(account, element['level'])
                dreamtownBuy(account, element['level'])
                break
            elif(element['price'] and (element['level'] == (currentLevel-6)) and (int(element['price'])*6 <= allCoin)):
                dreamtownBuy(account, element['level'])
                dreamtownBuy(account, element['level'])
                dreamtownBuy(account, element['level'])
                dreamtownBuy(account, element['level'])
                break
            # 金币不足时退出
            elif(element['price'] and (element['level'] <= (currentLevel-6))):
                return
            length -= 1


# 梦想小镇-买入
def dreamtownBuy(account, level):
    url = "https://dreamtown.58.com/web/dreamtown/buy"
    body = "level={0}&type=quick&source=magicisland".format(level)
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://dreamtown.58.com/web/v/dreamtown?from=magicisland&taskname=magicisland&os=android"
    }

    rjson = post(account, url, body=body, header=header)
    if(not rjson):
        return
    if(rjson['code'] == 0 and rjson['result']['state'] == 0):
        print("用户[{0}]梦想小镇购买{1}级车/房成功".format(account['name'], level))
        # 每次买入都进行合成
        dreamtownCompoundEnter(account)
    else:
        print("用户[{0}]梦想小镇购买{1}级车/房失败：{2}".format(account['name'],
              level, rjson['message']))


# 梦想小镇-查询是否已满
def dreamtownFull(account):
    url = "https://dreamtown.58.com/web/dreamtown/full"
    rjson = get(account, url)
    if(not rjson):
        return

    if(rjson['code'] == 0):
        return rjson['result']['full']
    else:
        print("用户[{0}]梦想小镇查询位置状态失败：{1}".format(
            account['name'], rjson['message']))
        return True


# 梦想小镇-生产加速
def dreamtownSpeed(account):
    url = "https://dreamtown.58.com/web/dreamtown/speed"
    rjson = get(account, url)
    if(not rjson):
        return

    if(rjson['code'] == 0):
        print("用户[{0}]梦想小镇生产加速成功".format(account['name']))
    else:
        print("用户[{0}]梦想小镇生产加速失败：{1}".format(
            account['name'], rjson['message']))


# 梦想小镇-召唤空投
def dreamtownFall(account):
    url_info = "https://dreamtown.58.com/web/dreamtown/maininfo?initialization=1"
    url_fall = "https://dreamtown.58.com/web/dreamtown/falldown"
    rjson_info = get(account, url_info)
    if(not rjson_info):
        return
    locations = list(rjson_info['result']['locationInfo'].values())
    for location in locations:
        # 有位置才能召唤空投
        if(not location):
            rjson_fall = get(account, url_fall)
            if(rjson_info['code'] == 0):
                if(not rjson_fall['result']):
                    continue
                print("用户[{0}]梦想小镇召唤空投成功：{1}级+{2}矿石".format(account['name'],
                      rjson_fall['result']['level'], rjson_fall['result']['ore']))
                sleep(1)
            else:
                print("用户[{0}]梦想小镇召唤空投失败：{1}".format(
                    account['name'], rjson_fall['message']))


# 矿石竞拍信息查询
def auctionInfo(account):
    url = "https://magicisland.58.com/web/auction/second"
    header = {"Referer": "https://magicisland.58.com/web/v/lowauctiondetail"}
    rjson = get(account, url, header)

    if(rjson['code'] == 0):
        status = int(rjson['result']['bidInfo']['bidStatus'])
        if(status == 0):
            print("用户[{0}]未参与矿石竞拍".format(account['name']))
            # 保留5矿石用于神奇矿山挖矿(只投入1)
            usableOre = int(float(rjson['result']['userInfo']['usableOre']))-5
            if(usableOre < 1):
                print("用户[{0}]矿山余额小于6，不参与竞拍".format(account['name']))
            else:
                auctionBid(account, 1)
        else:
            print("用户[{0}]已参与矿石竞拍".format(account['name']))

    else:
        print("用户[{0}]查询矿石竞拍主页失败：{1}".format(
            account['name'], rjson['message']))


# 矿石竞拍
def auctionBid(account, num):
    url = "https://magicisland.58.com/web/auction/bid"
    header = {
        "Referer": "https://magicisland.58.com/web/v/lowauctiondetail",
        "Content-Type": "application/x-www-form-urlencoded"}
    body = "ore={0}".format(num)
    rjson = post(account, url, body=body, header=header)

    if(rjson['code'] == 0):
        print("用户[{0}]矿石竞拍成功：{1}矿石".format(account['name'], num))
    else:
        print("用户[{0}]矿石竞拍失败：{1}".format(account['name'], rjson['message']))


# 早起打卡信息（不再自动报名，只进行签到）
def attendanceDetail(account):
    typeDict = {'oneDay': "一天", "multiDay": "三天"}
    url = "https://magicisland.58.com/web/attendance/detail/info?productorid=3"
    rjson = get(account, url)

    if(rjson['code'] == 0):
        infoList = rjson['result']['infoList']
        for info in infoList:
            state = info['userState']
            if(state == 1):
                print("用户[{0}]{1}期{2}打卡：已报名".format(
                    account['name'], info['number'], typeDict[info['type']]))
            elif(state == 0):
                print("用户[{0}]{1}期{2}打卡：未报名".format(
                    account['name'], info['number'], typeDict[info['type']]))
                #attendanceSignIn(account, info)
            elif(state == 5):
                print("用户[{0}]{1}期{2}打卡：可打卡".format(
                    account['name'], info['number'], typeDict[info['type']]))
                attendanceAttend(account, info)

    else:
        print("用户[{0}]获取早起打卡信息失败：{1}".format(
            account['name'], rjson['message']))


# 早起打卡报名
def attendanceSignIn(account, item):
    typeDict = {'oneDay': "一天", "multiDay": "三天"}
    url = "https://magicisland.58.com/web/attendance/signIn"
    body = "number={0}&category={1}&productorid=3".format(
        item['number'], item['type'])
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://magicisland.58.com/web/v/client"}
    rjson = post(account, url, body=body, header=header)

    if(rjson['code'] == 0):
        print("用户[{0}]{1}期{2}打卡报名成功：预计可获取{3}矿石".format(account['name'],
              item['number'], typeDict[item['type']], rjson['result']['averageRewardOre']))
    else:
        print("用户[{0}]{1}期{2}打卡报名失败：{3}".format(account['name'],
              item['number'], typeDict[item['type']], rjson['message']))


# 早起打卡签到
def attendanceAttend(account, item):
    typeDict = {'oneDay': "一天", "multiDay": "三天"}
    numType = {"oneDay": "number", "multiDay": "numberMany"}
    url = "https://magicisland.58.com/web/attendance/attend"
    body = "productorid=1&{0}={1}".format(
        numType[item['type']], item['number'])
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://magicisland.58.com/web/v/client"}
    rjson = post(account, url, body=body, header=header)

    if(rjson['code'] == 0):
        print("用户[{0}]{1}期{2}打卡成功".format(account['name'],
              item['number'], typeDict[item['type']]))
    else:
        print("用户[{0}]{1}期{2}打卡失败：{3}".format(account['name'],
              item['number'], typeDict[item['type']], rjson['message']))


# 现金签到页
def cashSigninlist(account):
    url = "https://tzbl.58.com/tzbl/taskcenter/signinlist?requestSource=1"
    rjson = get(account, url)

    if(rjson['code'] == 0):
        status = rjson['data']['signInVO']['status']
        if(status == 1):
            print("用户[{0}]现金签到：已签到".format(account['name']))
        elif(status == 2):  # 进行签到
            cashSignin(account)
    else:
        print("用户[{0}]查询签到页失败：{1}".format(account['name'], rjson['message']))


# 现金签到
def cashSignin(account):
    url = "https://tzbl.58.com/tzbl/taskcenter/signin?requestSource=1"
    rjson = get(account, url)
    if(rjson['code'] == 0):
        if("amount" in rjson['data']):  # 成功签到
            print("用户[{0}]现金签到：获取{1}元".format(
                account['name'], rjson["data"]['amount']))
        else:  # 已签到
            print("用户[{0}]现金签到：{1}".format(
                account['name'], rjson["data"]['msg']))
    else:
        print("用户[{0}]现金签到失败：{1}".format(account['name'], rjson['message']))


# 新手激励信息
def motivateInfo(account):
    url = "https://rightsplatform.58.com/web/motivate/maininfo"
    rjson = get(account, url)
    if(rjson['code'] == 0):
        print("用户[{0}]新人激励金币余额：{1} = {2}元".format(account['name'],
              rjson['result']['coin'], rjson['result']['amount']))
        # 签到
        if(rjson['result']['todaySignDay'] <= 7):
            item = rjson['result']['signInfo'][rjson['result']
                                               ['todaySignDay']-1]
            if(item['status'] == 0):
                motivateSign(account, item)
            else:
                print("用户[{0}]新人激励签到：已签到".format(account['name']))
        else:
            print("用户[{0}]新人激励签到：天数已满".format(account['name']))

        # 兑换
        withdrawInfo = rjson['result']['withdrawInfo']
        # 默认兑换5元
        flag = withdrawInfo and float(
            withdrawInfo[0]['cardCoin']) <= float(rjson['result']['coin'])
        if(flag):
            motivateWithdraw(account, withdrawInfo[0])
        else:
            print("用户[{0}]新人激励兑换条件不满足：{1}/{2}".format(account['name'],
                  rjson['result']['coin'], withdrawInfo[0]['cardCoin']))
    else:
        print("用户[{0}]新人激励信息查询失败：{1}".format(
            account['name'], rjson['message']))


# 新手激励签到
def motivateSign(account, item):
    url = "https://rightsplatform.58.com/web/motivate/sign"
    rjson = post(account, url)
    if(rjson['code'] == 0):
        print("用户[{0}]新人激励签到成功：获得{1}金币".format(
            account['name'], item['signCoin']))
    else:
        print("用户[{0}]新人激励签到失败：{1}".format(account['name'], rjson['message']))


# 新手激励金币兑换
def motivateWithdraw(account, item):
    url = "https://rightsplatform.58.com/web/motivate/withdraw"
    body = "id={0}".format(item['id'])
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    rjson = post(account, url, body=body, header=header)
    if(rjson['code'] == 0):
        print("用户[{0}]新人激励金币兑换成功：{1}元".format(
            account['name'], item['cardAmount']))
    else:
        print("用户[{0}]新人激励金币兑换失败：{1}".format(
            account['name'], rjson['message']))


# 每日分享得矿石
def share(account):
    url = "https://magicisland.58.com/web/invitationhelp/clickAddOre"
    header = {"referer": "https://magicisland.58.com/web/v/boost?os=android"}
    rjson = get(account, url, header=header)
    if(not rjson):
        return
    if(rjson['code'] == 0):
        print("用户[{0}]每日分享得矿石成功".format(account['name']))
    else:
        print("用户[{0}]每日分享得矿石失败：{1}".format(account['name'], rjson['message']))


# 任务执行按活动页划分
if __name__ == "__main__":
    print("{0}{1}{0}".format(10*'*', projectNameCN))
    initEnv()

    print("\n\n{0}风控检查{0}".format(8*'='))
    for account in accounts:
        checkUserState(account)
        print("{0}".format(10*'——'))

    # print("\n\n{0}现金签到{0}".format(8*'='))
    # for account in accounts:
    #     if(not account['normal']):
    #         continue
    #     cashSigninlist(account)
    #     print("{0}".format(10*'——'))

    # print("\n\n{0}神奇矿主页{0}".format(8*'='))
    # for account in accounts:
    #     if(not account['normal']):
    #         continue
    #     mainHome(account)
    #     mainSignExtra(account)
    #     print("{0}".format(10*'——'))

    # print("\n\n{0}每日抽奖{0}".format(8*'='))
    # for account in accounts:
    #     if(not account['normal']):
    #         continue
    #     rouletteInfo(account)
    #     print("{0}".format(10*'——'))

    # print("\n\n{0}关注服务号{0}".format(8*'='))
    # for account in accounts:
    #     if(not account['normal']):
    #         continue
    #     getRecFollowList(account)
    #     print("{0}".format(10*'——'))

    print("\n\n{0}场景任务{0}".format(8*'='))
    for account in accounts:
        if(not account['normal']):
            continue
        doTasks(account)
        print("{0}".format(10*'——'))

    print("\n\n{0}新人激励{0}".format(8*'='))
    for account in accounts:
        if(not account['normal']):
            continue
        motivateInfo(account)
        print("{0}".format(10*'——'))

    # print("\n\n{0}我的家{0}".format(8*'='))
    # for account in accounts:
    #     if(not account['normal']):
    #         continue
    #     houseInfo(account)
    #     houseWork(account)
    #     houseWorkState(account)
    #     houseWithdrawPage(account)
    #     print("{0}".format(10*'——'))

    # print("\n\n{0}梦想小镇{0}".format(8*'='))
    # for account in accounts:
    #     if(not account['normal']):
    #         continue
    #     dreamtownScence(account)
    #     dreamtownSign(account)
    #     dreamtownMonopolyInfo(account)
    #     dreamtownEnter(account)
    #     dreamtownSpeed(account)
    #     print("{0}".format(10*'——'))

    # print("\n\n{0}矿工{0}".format(8*'='))
    # for account in accounts:
    #     if(not account['normal']):
    #         continue
    #     mineInfo(account)
    #     print("{0}".format(10*'——'))

    # print("\n\n{0}神奇矿山{0}".format(8*'='))
    # for account in accounts:
    #     if(not account['normal']):
    #         continue
    #     miningUserInfo(account)
    #     miningStealList(account)
    #     print("{0}".format(10*'——'))

    # print("\n\n{0}早起打卡{0}".format(8*'='))
    # for account in accounts:
    #     if(not account['normal']):
    #         continue
    #     attendanceDetail(account)
    #     print("{0}".format(10*'——'))

    # print("\n\n{0}矿石竞拍{0}".format(8*'='))
    # for account in accounts:
    #     if(not account['normal']):
    #         continue
    #     auctionInfo(account)
    #     print("{0}".format(10*'——'))
