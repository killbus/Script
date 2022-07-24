# -*- encoding: utf-8 -*-
'''
@项目名称：   elmPlus.py
@项目地址：   
@创建时间：   2022/05/23 11:23:48
@创作者  ：   wsfsp4 
@版本号  ：   
@功能描述：   
@特别提醒：   
@更新时间：   
@更新内容：   
'''

from email import header
import random
import sys
import os.path
import json
from time import sleep
import requests

projectNameCN = "饿了么"
projectNameEN = "elm"
accounts = []
basicInfo = {}


def initEnv():
    global accounts
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\{0}.json".format(projectNameEN)
    else:
        filePath += "/{0}.json".format(projectNameEN)

    projectConfig = {}
    # 配置文件存在
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


# 统一GET 额外header用字典传递
def get(url, header=None):
    headers = {
        "UA": 'Rajax/1 Apple/iPhone13,2 iOS/15.0 Eleme/10.7.15 ID/76C6E983-2F91-B1F7-593D-12661C12B59B; IsJailbroken/0 Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 AliApp(ELMC/10.7.15) UT4Aplus/ltracker-0.0.6 WindVane/8.7.2 1170x2532 WK',
        "XUA": 'RenderWay/H5 AppName/elmc DeviceId/76C6E983-2F91-B1F7-593D-12661C12B59B AppExtraInfo/%7B%22miniWua%22%3A%22838eb602%22%2C%22umidToken%22%3A%22a73c50d9%22%2C%22ttid%22%3A%22201200%40eleme_iphone_10.7.15%22%2C%22deviceUUID%22%3A%2276C6E983-2F91-B1F7-593D-12661C12B59B%22%2C%22utdid%22%3A%2257f6440b%22%7D',
        "x_shard": 'loc=113.3617596348414,22.9190543405622',
        "longitude": '113.3617596348414',
        "latitude": '22.9190543405622'
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
def post(url, body='', header=None):
    headers = {
        "UA": 'Rajax/1 Apple/iPhone13,2 iOS/15.0 Eleme/10.7.15 ID/76C6E983-2F91-B1F7-593D-12661C12B59B; IsJailbroken/0 Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 AliApp(ELMC/10.7.15) UT4Aplus/ltracker-0.0.6 WindVane/8.7.2 1170x2532 WK',
        "XUA": 'RenderWay/H5 AppName/elmc DeviceId/76C6E983-2F91-B1F7-593D-12661C12B59B AppExtraInfo/%7B%22miniWua%22%3A%22838eb602%22%2C%22umidToken%22%3A%22a73c50d9%22%2C%22ttid%22%3A%22201200%40eleme_iphone_10.7.15%22%2C%22deviceUUID%22%3A%2276C6E983-2F91-B1F7-593D-12661C12B59B%22%2C%22utdid%22%3A%2257f6440b%22%7D',
              "x_shard": 'loc=113.3617596348414,22.9190543405622',
        "longitude": '113.3617596348414',
        "latitude": '22.9190543405622'
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


def getPosition():
    return {"longitude": "113.3871{0}".format(random.randint(1000, 2000)), "latitude": "22.931{0}".format(random.randint(1000, 2000))}


def getTaskBasic():
    global basicInfo
    url = "https://h5.ele.me/restapi/biz.growth_finetune/v1/finetune/operate?bizScenarioCode=home_ch_tasklist"
    rjson = get(url)
    if(not rjson):
        print("获取数据失败,脚本退出！")
    if(rjson['header']['message'] == "success"):
        basicInfo['actId'] = rjson['outputJson']['moduleList'][3]['content']['$attr']['actId']
        basicInfo['acceptTagCode'] = rjson['outputJson']['moduleList'][5]['content']['$attr']['acceptTagCode']
        basicInfo['queryTagCode'] = rjson['outputJson']['moduleList'][5]['content']['$attr']['queryTagCode']
        print("瓜分吃货豆ID：{0}".format(basicInfo['actId']))
        print("活动acceptTagCode：{0}".format(basicInfo['acceptTagCode']))
        print("活动queryTagCode：{0}".format(basicInfo['queryTagCode']))
    else:
        print("获取数据失败,脚本退出！")
        exit()


def getUserInfo(account):
    url = "https://restapi.ele.me/eus/v4/user_mini"
    header = {"cookie": account['cookie']}
    rjson = get(url, header=header)
    if(not rjson):
        return
    account['info'] = rjson
    print("用户[{0}]登录成功".format(rjson['mobile']))


def enrollInfo(account):
    url = 'https://h5.ele.me/restapi/biz.svip_scene/svip/engine/queryTrafficSupply?tagParams=[{{"tagCode":"347079","extra":{{"solutionType":"QUERY","actId":"{0}","sceneCode":"divide_chd_interact","client":"eleme"}}}}]&bizCode=biz_card_main&longitude=113.3617596348414&latitude=22.9190543405622'.format(
        basicInfo["actId"])
    header = {"cookie": account['cookie']}
    rjson = get(url, header=header)
    attribute = rjson['data'][0]['data'][0]['attribute']
    if(attribute['userStatus'] == 10):
        print("用户[{0}]已报名瓜分豆豆".format(account['info']['mobile']))
    else:
        print("用户[{0}]未报名瓜分豆豆".format(account['info']['mobile']))
        safeCode = attribute['safeCode']
        phaseId = attribute['curPhaseId']
        enrollEnter(account, safeCode, phaseId)

    if("lastPrizeInfo" in attribute and "amount" in attribute['lastPrizeInfo']):
        lastPrizeInfo = attribute['lastPrizeInfo']
        amount = lastPrizeInfo['amount']
        lastPhaseId = attribute['lastActInfo']['lastPhaseId']
        if(lastPrizeInfo['lastUserStatus'] == 30):
            print("用户[{0}]可领取上期奖励：{1}豆豆".format(
                account['info']['mobile'], amount))
            enrollReward(account, lastPhaseId, amount)
        else:
            print("用户[{0}]已领取上期奖励：{1}豆豆".format(
                account['info']['mobile'], amount))


def enrollEnter(account, safeCode, phaseId):
    url = "https://h5.ele.me/restapi/biz.svip_scene/svip/engine/xSupply?asac={0}".format(
        safeCode)
    param = {
        "params": [
            {
                "tagCode": "381410",
                "extra": {
                    "solutionType": "ENROLL",
                    "phaseId": phaseId,
                    "actId": "20210826153802420194984542",
                    "sceneCode": "divide_chd_interact",
                    "client": "eleme"
                }
            }
        ],
        "bizCode": "biz_card_main",
        "longitude": '113.3617596348414',
        "latitude": '22.9190543405622'
    }
    body = json.dumps(param)
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": account['cookie']
    }
    rjson = post(url, body=body, header=header)
    if(not rjson['data'][0]['xmessage']):
        print("用户[{0}]报名瓜分豆豆成功".format(account['info']['mobile']))
    else:
        print("用户[{0}]报名瓜分豆豆失败".format(
            account['info']['mobile'], rjson['data'][0]['xmessage']))


def enrollReward(account, phaseId, amount):
    url = "https://h5.ele.me/restapi/biz.svip_scene/svip/engine/xSupply"
    param = {
        "params": [
            {"tagCode": "427048",
             "extra": {
                 "solutionType": "RECEIVE_PRIZE",
                 "phaseId": phaseId,
                 "actId": "20210826153802420194984542",
                 "sceneCode": "divide_chd_interact", "amount": amount}}],
        "bizCode": "biz_card_main",
        "longitude": '113.3617596348414',
        "latitude": '22.9190543405622'
    }
    body = json.dumps(param)
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": account['cookie']
    }
    rjson = post(url, header=header, body=body)
    if(rjson['data'][0]['xstatus'] == 1):
        print("用户[{0}]领取上期奖励成功".format(account['info']['mobile']))
    else:
        print("用户[{0}]领取上期奖励失败：{1}".format(account['info']
              ['mobile'], rjson['data'][0]['xmessage']))


def cashBack(account):
    url = "https://httpizza.ele.me/ele-fin-promotion-activity/bonus/queryTasks?welfareCode=cash_back-1"
    header = {
        "cookie": account['cookie']
    }
    rjson = get(url, header=header)
    if(not rjson):
        return
    if(rjson['data']):
        for task in rjson['data']:
            if(task['status'] != "unreceived"):
                print("用户[{0}]笔笔返[{1}]已完成".format(account['info']['mobile'],task['taskName']))
                continue
            print("用户[{0}]任务[{1}]：0.0{2}元".format(account['info']['mobile'], task['taskName'], task['bonusNum']))
            cashBackReward(account, task['taskId'])
    else:
        print("用户[{0}]笔笔返暂无任务".format(account['info']['mobile']))


def cashBackReward(account, taskId):
    url = "https://httpizza.ele.me/ele-fin-promotion-activity/bonus/receiveAndFinishTask"
    header = {"cookie": account['cookie']}
    body = {"taskId": taskId, "scene": "saving-pot","welfareCode": "cash_back-1"}
    rjson = post(url, body=json.dumps(body), header=header)
    if(not rjson):
        return




if __name__ == "__main__":
    initEnv()
    print("\n{0}活动信息{0}".format(8*'#'))
    getTaskBasic()
    for account in accounts:
        account['position'] = getPosition()

    print("\n{0}用户信息{0}".format(8*'#'))
    for account in accounts:
        getUserInfo(account)

    print("\n{0}瓜分吃豆{0}".format(8*'#'))
    for account in accounts:
        if(account['info']):
            enrollInfo(account)

    print("\n{0}笔笔返{0}".format(8*'#'))
    for account in accounts:
        if(account['info']):
            cashBack(account)
