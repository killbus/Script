# -*- encoding: utf-8 -*-
'''
@项目名称：   ydhb.py
@项目地址：   
@创建时间：   2022/06/24 13:43:37
@创作者  ：   wsfsp4 
@版本号  ：   1.0
@功能描述：   每日签到，每月积分任务
@特别提醒：   
@更新时间：   
@更新内容：   
'''

import os
import sys
import json
import requests


class User:

    def __init__(self, cookie) -> None:
        self.cookie = cookie
        self.valid = True

    # 统一GET 额外header用字典传递
    def __get__(self, url, header=None):
        try:
            headers = {"user-agent": "Mozilla/5.0 (Linux; Android 10; CDY-AN00 Build/HUAWEICDY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko)",
                       "Cookie": self.cookie['cookie'],
                       "referer": "https://www.cmpay.com/info/version3/marketing_2022/signin/signin.html?"}
            if(header):
                headers.update(header)
            res = requests.get(url, headers=headers)
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    # 统一POST 额外header用字典传递
    def __post__(self, url, body=None, header=None):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; CDY-AN00 Build/HUAWEICDY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko)",
                       "Content-Type": "application/json",
                       "Cookie": self.cookie['cookie'],
                       "Referer": "https://www.cmpay.com/info/version3/marketing_2022/signin/signin.html?"}
            if(header):
                headers.update(header)
            res = requests.post(url, data=body, headers=headers)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def __getUserPoint__(self):
        print("\n\n{0}账号信息{0}".format(10*"#"))
        url = "https://www.cmpay.com/activities/v1/signAwardPoint/getUserPoint"
        rjson = self.__get__(url)
        if(not rjson):
            return
        if(not rjson['msgInfo']):
            if(self.cookie['name']):
                print("备注：{0}".format(self.cookie['name']))
                print("积分：{0}".format(rjson['body']['userPoint']))
        else:
            self.valid = False
            print("获取账号信息失败：{0}".format(rjson['msgInfo']))

    def __getInfo__(self):
        url = "https://www.cmpay.com/activities/v1/signAwardPoint/index"
        body = {"isClient": "0"}
        rjson = self.__post__(url, json.dumps(body))
        if(not rjson):
            return
        if(not rjson['msgInfo']):
            self.info = rjson['body']
        else:
            self.valid = False
            print("获取任务信息失败：{0}".format(rjson['msgInfo']))

    def __signInfo__(self):
        todaySignStatus = self.info['todaySignStatus']
        signDateList = self.info['signDateList']
        print("\n{0}日签到{0}".format(10*"-"))
        for signDate in signDateList:
            awardAmt = signDate['awardAmt']
            dateInfo = signDate['dateInfo']
            signStatus = signDate['signStatus']
            signDesc = ""
            if(signStatus == "0"):
                signDesc = "未签"
            elif(signStatus == "1"):
                signDesc = "已签"
            elif(signStatus == "2"):
                signDesc = "漏签"
            else:
                signDesc = "待签"
            print("{0}\t+{1}\t{2}".format(dateInfo, awardAmt, signDesc))
        if(not todaySignStatus):
            self.__sign__()
        print("\n{0}月签到{0}".format(10*"-"))
        ##monthlySignAwardFlag = self.info['monthlySignAwardFlag']
        signMonthList = self.info['signMonthList']
        for signMonth in signMonthList:
            if(signMonth['signFlag']):
                print("{0}\t已签".format(signMonth['signMonth']))
            else:
                print("{0}\t未签".format(signMonth['signMonth']))

    def __sign__(self):
        url = "https://www.cmpay.com/activities/v1/signAwardPoint/sign"
        body = {"isClient": "0"}
        rjson = self.__post__(url, json.dumps(body))
        if(not rjson):
            return
        if(not rjson['msgInfo']):
            signResultList = rjson['body']['signResultList']
            for signResult in signResultList:
                print("签到成功：\t+{0}".format(signResult['signAmt']))
        else:
            print("签到失败：{0}".format(rjson['msgInfo']))

    def __monthTask__(self):
        print("\n{0}月任务{0}".format(10*"-"))
        taskList = self.info['taskList']
        for task in taskList:
            taskStatusDesc = ""
            if(task['taskStatus'] == "0"):
                taskStatusDesc = "未完成"
            elif(task['taskStatus'] == "1"):
                taskStatusDesc = "待领取"
            else:
                taskStatusDesc = "已完成"
            print(
                "{0}\t +{1} --{2}".format(task['taskName'], task['taskPrizeAmt'], taskStatusDesc))
        print("")
        for task in taskList:
            if(task['taskStatus'] == "0"):
                print("执行任务[{0}]".format(task['taskName']))
                self.__doTask__(task)
        for task in taskList:
            if(task['taskStatus'] == "1"):
                self.__getTaskAward__(task)

    def __doTask__(self, task):
        url = "https://www.cmpay.com/activities/v1/signAwardPoint/finishTask"
        body = {"taskNo": task['taskNo']}
        self.__post__(url, json.dumps(body))

    def __getTaskAward__(self, task):
        url = "https://www.cmpay.com/activities/v1/signAwardPoint/awardFinishTask"
        body = {"taskNo": task['taskNo']}
        rjson = self.__post__(url, json.dumps(body))
        if(not rjson):
            return
        if(not rjson['msgInfo']):
            print("领取任务[{0}]奖励成功：+{1}".format(task['taskName'],
                  rjson['body']['awardPoint']))
        else:
            print("领取任务[{0}]奖励失败：{1}".format(
                task['taskName'], rjson['msgInfo']))

    def __getActivityDetail__(self):
        url = "https://m.jf.10086.cn/cmcc-hepay-shop/taskActivity/portalDetail"
        body = "activityId=%5B200000000001972%2C200000000001971%2C200000000002132%2C200000000001967%2C200000000001998%2C200000000002002%2C200000000001994%5D&userId=&userPhoneNo="
        header = {"Content-Type": "application/x-www-form-urlencoded",
                  "Origin": "https://m.jf.10086.cn"}
        rjson = self.__post__(url, body=body, header=header)
        if(not rjson):
            return
        if(rjson['resultCode'] ==200):
            taskList = rjson['resultJson']
            for task in taskList:
                if("joinCount" not in task or task['joinCount']<task['joinLimit']):
                    self.__activityGrant__(task)
        else:
            print("获取活动列表失败：{0}".format(rjson['resultMessage']))

    def __activityGrant__(self,task):
        url = "https://m.jf.10086.cn/cmcc-hepay-shop/taskActivity/grant"
        body = "activityId={0}&province=gd&realLoginChannel=CMPAY".format(task['activityId'])
        header = {"Content-Type": "application/x-www-form-urlencoded",
                  "Origin": "https://m.jf.10086.cn"}
        rjson = self.__post__(url, body=body, header=header)
        if(not rjson):
            return
        if(rjson['resultCode']  == 200):
            print("任务[{0}]参与成功".format(task['activityId']))
        else:
            print("任务[{0}]参与成功失败：{1}".format(task['activityId'],rjson['resultMessage']))

    def run(self):
        self.__getUserPoint__()
        if(not self.valid):
            return
        print("\n>>>限时活动A")
        self.__getInfo__()
        if(self.valid):
            self.__signInfo__()
            self.__monthTask__()
        print("\n>>>限时活动B")
        self.__getActivityDetail__()


def initEnv() -> list:
    cookieList = []
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\{0}.json".format("ydhb")
    else:
        filePath += "/{0}.json".format("ydhb")
    # 读写配置
    if(os.path.isfile(filePath)):
        file = open(filePath, "r", encoding="utf-8")
        content = file.read()
        file.close()
        cookieList = json.loads(content)['cookies']
    else:
        file = open(filePath, "w+", encoding="utf-8")
        newContent = {"cookies": [{"cookie": "", "name": ""}, {"cookie": "", "name": ""}, {
            "cookie": "", "name": ""}, {"cookie": "", "name": ""}]}
        file.write(json.dumps(newContent, indent=2))
        file.close()
    return cookieList


if __name__ == "__main__":
    cookies = initEnv()
    users = []
    for cookie in cookies:
        if(cookie['cookie']):
            users.append(User(cookie))
    for user in users:
        user.run()
