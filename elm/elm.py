# -*- encoding: utf-8 -*-
'''
@项目名称：   elm.py
@项目地址：   
@创建时间：   2022/05/01 18:33:18
@创作者  ：   wsfsp4 
@版本号  ：   2.0
@功能描述：   
@特别提醒：   
@更新时间：   2022/05/05 17:56:04
@更新内容：   修复单账号失效导致脚本异常退出问题
'''
from operator import index
import random
import sys
import os.path
import json
from time import sleep
import requests
from torch import t

projectNameCN = "饿了么"
projectNameEN = "elm"


def initEnv():
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
            content = json.loads(content)
            file.close()
        return content['accounts']
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


class User:

    def __init__(self,cookie,index,remark="") -> None:
        if(not cookie):
            self.valid = False
            return
        self.valid = True
        self.cookie = cookie
        self.index = index    #序号
        self.remark = remark    #备注
        self.longitude = "113.3871{0}".format(random.randint(1000, 2000))
        self.latitude = "22.931{0}".format(random.randint(1000, 2000))

    def __get__(self,url):
        try:
            headers = {
                "cookie": self.cookie,
                "UA": 'Rajax/1 Apple/iPhone13,2 iOS/15.0 Eleme/10.7.15 ID/76C6E983-2F91-B1F7-593D-12661C12B59B; IsJailbroken/0 Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 AliApp(ELMC/10.7.15) UT4Aplus/ltracker-0.0.6 WindVane/8.7.2 1170x2532 WK',
                "XUA": 'RenderWay/H5 AppName/elmc DeviceId/76C6E983-2F91-B1F7-593D-12661C12B59B AppExtraInfo/%7B%22miniWua%22%3A%22838eb602%22%2C%22umidToken%22%3A%22a73c50d9%22%2C%22ttid%22%3A%22201200%40eleme_iphone_10.7.15%22%2C%22deviceUUID%22%3A%2276C6E983-2F91-B1F7-593D-12661C12B59B%22%2C%22utdid%22%3A%2257f6440b%22%7D',
                "x_shard": 'loc={0},{1}'.format(self.longitude,self.latitude),
                "longitude": self.longitude,
                "latitude": self.latitude
            }
            res = requests.get(url, headers=headers)
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
        return None

    def __post__(self,url,body=None):
        try:
            headers = {
                "cookie": self.cookie,
                "Content-Type": "application/json;charset=UTF-8",
                "UA": 'Rajax/1 Apple/iPhone13,2 iOS/15.0 Eleme/10.7.15 ID/76C6E983-2F91-B1F7-593D-12661C12B59B; IsJailbroken/0 Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 AliApp(ELMC/10.7.15) UT4Aplus/ltracker-0.0.6 WindVane/8.7.2 1170x2532 WK',
                "XUA": 'RenderWay/H5 AppName/elmc DeviceId/76C6E983-2F91-B1F7-593D-12661C12B59B AppExtraInfo/%7B%22miniWua%22%3A%22838eb602%22%2C%22umidToken%22%3A%22a73c50d9%22%2C%22ttid%22%3A%22201200%40eleme_iphone_10.7.15%22%2C%22deviceUUID%22%3A%2276C6E983-2F91-B1F7-593D-12661C12B59B%22%2C%22utdid%22%3A%2257f6440b%22%7D',
                "x_shard": 'loc={0},{1}'.format(self.longitude,self.latitude),
                "longitude": self.longitude,
                "latitude": self.latitude
            }
            res = requests.post(url, data=body, headers=headers)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def __getUserInfo__(self):
        url = "https://restapi.ele.me/eus/v4/user_mini"
        rjson = self.__get__(url)
        if(rjson and "message" not in rjson):
            if(self.remark):
                 print("账号备注：{0}".format(self.remark))
            print("用户昵称：{0}".format(rjson['username']))
            print("用户ID：{0}".format(rjson['id']))
            print("手机号：{0}".format(rjson['mobile']))
        else:
            self.valid = False
            print("获取用户信息失败：{0}".format(rjson['message']))

    def __getBlance__(self):
        url = 'https://h5.ele.me/restapi/biz.svip_bonus/v1/users/supervip/pea/queryAccountBalance?types=["PEA_ACCOUNT"]&longitude={0}&latitude={1}'.format(
            self.longitude, self.latitude)
        rjson = self.__get__(url)
        if(not rjson):
            return
        if("success" in rjson):
            print("豆豆余额：{0}".format(rjson['accountInfos'][0]['count']))
        else:
            print("查询豆豆失败：{0}".format(rjson))

    def __enrollInfo__(self):
        url = 'https://h5.ele.me/restapi/biz.svip_scene/svip/engine/queryTrafficSupply?tagParams=[{{"tagCode":"347079","extra":{{"solutionType":"QUERY","actId":"20210826153802420194984542","sceneCode":"divide_chd_interact","client":"eleme"}}}}]&bizCode=biz_card_main&longitude={0}&latitude={1}'.format(
            self.longitude, self.latitude)
        rjson = self.__get__(url)
        if(not rjson):
            return
        attribute = rjson['data'][0]['data'][0]['attribute']
        safeCode = attribute['safeCode']
        phaseId = attribute['curPhaseId']
        if(attribute['userStatus'] == 10):
            print("已报名[{0}]期瓜分豆豆".format(phaseId))
        else:
            print("未报名[{0}]期瓜分豆豆".format(phaseId))
            self.__enrollEnter__(safeCode, phaseId)

        if("lastPrizeInfo" in attribute and "amount" in attribute['lastPrizeInfo']):
            lastPrizeInfo = attribute['lastPrizeInfo']
            amount = lastPrizeInfo['amount']
            lastPhaseId = attribute['lastActInfo']['lastPhaseId']
            if(lastPrizeInfo['lastUserStatus'] == 30):
                print("可领取上期奖励：{0}豆豆".format(amount))
                self.__enrollReward__(lastPhaseId, amount)
            else:
                print("已领取上期奖励：{0}豆豆".format(amount))

    def __enrollEnter__(self,safeCode, phaseId):
        url = "https://h5.ele.me/restapi/biz.svip_scene/svip/engine/xSupply?asac={0}".format(safeCode)
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
            "longitude": self.longitude,
            "latitude": self.latitude
        }
        body = json.dumps(param)
        rjson = self.__post__(url, body=body,)
        if(not rjson):
            return
        if(not rjson['data'][0]['xmessage']):
            print("报名[{0}]期瓜分豆豆成功".format(phaseId))
        else:
            print("报名[{0}]期瓜分豆豆失败：{1}".format(phaseId,rjson['data'][0]['xmessage']))

    def __enrollReward__(self, phaseId, amount):
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
            "longitude": self.longitude,
            "latitude": self.latitude
        }
        body = json.dumps(param)
        rjson = self.__post__(url,body=body)
        if(not rjson):
            return
        if(rjson['data'][0]['xstatus'] == 1):
            print("领取[{0}]期奖励成功".format(phaseId))
        else:
            print("领取[{0}]期奖励失败：{1}".format(phaseId,rjson['data'][0]['xmessage']))

    def __cashBackInfo(self):
        url = "https://httpizza.ele.me/ele-fin-promotion-activity/bonus/queryTasks?welfareCode=cash_back-1"
        rjson = self.__get__(url)
        if(not rjson):
            return
        if(rjson["data"]):
            tasks = rjson['data']
            for task in tasks:
                status = task['status']
                if(status == "unreceived"):
                    print("任务[{0}] +{1}元 --未完成".format(task['taskName'],task['bonusNum']/100))
                else:
                    print("任务[{0}] +{1}元 --已完成".format(task['taskName'],task['bonusNum']/100,))
        else:
            print("空任务列表")

    #任务执行入口
    def run(self):
            print("{0}账号[{1}]{0}".format(10*"=",self.index))
            self.__getUserInfo__()
            if(not self.valid):
                return
            self.__getBlance__()
            #print("\n{0}瓜分豆豆{0}".format(10*"-"))
            #self.__enrollInfo__()
            #print("\n{0}笔笔返{0}".format(10*"-"))
            self.__cashBackInfo()
            print("\n")

def get(account, url, header=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
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
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "Cookie": account['cookie']
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


def getBlance(account):
    url = 'https://h5.ele.me/restapi/biz.svip_bonus/v1/users/supervip/pea/queryAccountBalance?types=["PEA_ACCOUNT"]&longitude={0}&latitude={1}'.format(
        account['position']['longitude'], account['position']['latitude'])
    rjson = get(account, url)

    if(not rjson):
        return
    if("success" in rjson):
        account['isNormal'] = True
        return rjson['accountInfos'][0]['count']
    else:
        account['isNormal'] = False
        print("用户[{0}]查询豆豆失败：{1}".format(account['name'], rjson))
        return


def getTagCode(account):
    url = 'https://h5.ele.me/restapi/biz.growth_finetune/v1/finetune/operate?bizScenarioCode=home_ch_tasklist&longitude={0}&latitude={1}'.format(
        account['position']['longitude'], account['position']['latitude'])
    rjson = get(account, url)

    if(not rjson):
        return
    attr = rjson['outputJson']["moduleList"][-1]['content']['$attr']
    if(attr):
        return {"acceptTagCode": attr['acceptTagCode'], "queryTagCode": attr['queryTagCode']}
    else:
        print("用户[{0}]获取tagCode失败".format(account['name']))
        return None


def getTaskList(account):
    url = 'https://h5.ele.me/restapi/biz.svip_scene/svip/engine/queryTrafficSupply?tagParams[]={{"tagCode":"{0}"}}&bizCode=biz_card_main&longitude={1}&latitude={2}'.format(
        account['tagCode']['queryTagCode'], account['position']['longitude'], account['position']['latitude'])
    rjson = get(account, url)

    if(not rjson):
        return
    return rjson['data'][0]['data']


def doTasks(account):
    tasksList = getTaskList(account)
    if(not tasksList):
        print("用户[{0}]获取任务列表失败")

    for task in tasksList:
        if(task["attribute"]["receiveStatus"] == "TORECEIVE"):
            missionType = task["attribute"]['missionType']
            if(missionType == "SIMPLESIGNIN"):
                missionDefId = task["attribute"]['missionDefId']
                missionCollectionId = task["attribute"]['missionCollectionId']
                print("执行任务[{0}]".format(task["attribute"]["subTitle"]))
                doTask(account, missionDefId, missionCollectionId, missionType)
                print("--->休息15秒")
                sleep(15)


def doTask(account, missionDefId, missionCollectionId, missionType):
    url = 'https://h5.ele.me/restapi/biz.svip_scene/svip/engine/xSupply?params[]={{"tagCode":"{0}","extra":{{"missionDefId":{1},"missionCollectionId":{2},"missionType":"{3}"}}}}&bizCode=biz_code_main&longitude={4}&latitude={5}'.format(
        account['tagCode']['acceptTagCode'], missionDefId, missionCollectionId, missionType, account['position']['longitude'], account['position']['latitude'])
    rjson = get(account, url)
    print("任务完成")


def enrollInfo(account):
    url = 'https://h5.ele.me/restapi/biz.svip_scene/svip/engine/queryTrafficSupply?tagParams=[{{"tagCode":"347079","extra":{{"solutionType":"QUERY","actId":"20210826153802420194984542","sceneCode":"divide_chd_interact","client":"eleme"}}}}]&bizCode=biz_card_main&longitude={0}&latitude={1}'.format(
        account['position']['longitude'], account['position']['latitude'])
    rjson = get(account, url)
    attribute = rjson['data'][0]['data'][0]['attribute']
    if(attribute['userStatus'] == 10):
        print("用户[{0}]已报名瓜分豆豆".format(account['name']))
    else:
        print("用户[{0}]未报名瓜分豆豆".format(account['name']))
        safeCode = attribute['safeCode']
        phaseId = attribute['curPhaseId']
        enrollEnter(account, safeCode, phaseId)

    if("lastPrizeInfo" in attribute and "amount" in attribute['lastPrizeInfo']):
        lastPrizeInfo = attribute['lastPrizeInfo']
        amount = lastPrizeInfo['amount']
        lastPhaseId = attribute['lastActInfo']['lastPhaseId']
        if(lastPrizeInfo['lastUserStatus'] == 30):
            print("用户[{0}]可领取上期奖励：{1}豆豆".format(account['name'], amount))
            enrollReward(account, lastPhaseId, amount)
        else:
            print("用户[{0}]已领取上期奖励：{1}豆豆".format(account['name'], amount))


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
        "longitude": float(account['position']['longitude']),
        "latitude": float(account['position']['latitude'])
    }
    body = json.dumps(param)
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-ua": 'RenderWay/H5 AppName/elmc DeviceId/ce654633-e958-32f6-98a2-fc402c9dcd54 AppExtraInfo/%7B%22utdid%22%3A%22YmhvBUBuKX8DACPCOi9XELPB%22%2C%22umidToken%22%3A%22iGlLZThLOg9SHzWAkTjTtjd01jL7W3Dc%22%2C%22ttid%22%3A%221601274963112%40eleme_android_10.7.15%22%2C%22deviceUUID%22%3A%22ce654633-e958-32f6-98a2-fc402c9dcd54%22%2C%22miniWua%22%3A%22HHnB_YI5ABAFggW1%2Fu8m7kb%2FCV3OtQZ3kflzMfJ1fNoWOVUdmldpu7p3Jjr3AuvTWfHBbQYpt5zvc9rpKTsJFdo5swug%2BXzRIxBl6I4Ag4rX2N%2B6ex5tYq6wkSO1Ff0EQu4tJwmbLKeHwVsgCDaxkM%2FWdnyIImNjpV4uas%2Fhh7HA7NSo%3D%22%7D'
    }

    rjson = post(account, url, body=body, header=header)
    if(not rjson['data'][0]['xmessage']):
        print("用户[{0}]报名瓜分豆豆成功".format(account['name']))
    else:
        print("用户[{0}]报名瓜分豆豆失败".format(
            account['name'], rjson['data'][0]['xmessage']))


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
        "longitude": float(account['position']['longitude']),
        "latitude": float(account['position']['latitude'])
    }
    body = json.dumps(param)
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-ua": 'RenderWay/H5 AppName/elmc DeviceId/ce654633-e958-32f6-98a2-fc402c9dcd54 AppExtraInfo/%7B%22utdid%22%3A%22YmhvBUBuKX8DACPCOi9XELPB%22%2C%22umidToken%22%3A%22iGlLZThLOg9SHzWAkTjTtjd01jL7W3Dc%22%2C%22ttid%22%3A%221601274963112%40eleme_android_10.7.15%22%2C%22deviceUUID%22%3A%22ce654633-e958-32f6-98a2-fc402c9dcd54%22%2C%22miniWua%22%3A%22HHnB_YI5ABAFggW1%2Fu8m7kb%2FCV3OtQZ3kflzMfJ1fNoWOVUdmldpu7p3Jjr3AuvTWfHBbQYpt5zvc9rpKTsJFdo5swug%2BXzRIxBl6I4Ag4rX2N%2B6ex5tYq6wkSO1Ff0EQu4tJwmbLKeHwVsgCDaxkM%2FWdnyIImNjpV4uas%2Fhh7HA7NSo%3D%22%7D'
    }
    rjson = post(account, url, header=header, body=body)
    if(rjson['data'][0]['xstatus'] == 1):
        print("用户[{0}]领取上期奖励成功".format(account['name']))
    else:
        print("用户[{0}]领取上期奖励失败：{1}".format(
            account['name'], rjson['data'][0]['xmessage']))


if __name__ == "__main__":
    print("{0}{1}{0}".format(10*'*', projectNameCN))
    accounts = initEnv()
    users = []
    index = 1 #账号序号
    for account in accounts:
        account['position'] = getPosition()
        account['tagCode'] = getTagCode(account)
        doTasks(account)
    #     if(account['cookie']):
    #         users.append(User(account['cookie'],index,account['name']))
    #         index +=1
    # for user in users:
    #     user.run()
