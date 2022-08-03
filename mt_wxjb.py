# -*- encoding: utf-8 -*-
'''
@项目名称：   meituan.py
@更新时间：   2022/07/31 10:15:12
@版本号  ：   
@环境变量：   
@更新内容：   
'''

import json
import os
import sys
from time import sleep
import requests


PROJECT_NAME = "mt_wxjb"


class User:
    def __init__(self, cookie, index=1) -> None:
        self.index = index
        self.valid = True
        self.cookie = cookie

    def get(self, url, header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; TAS-AL00 Build/N2G48C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 MMWEBID/4561 MicroMessenger/8.0.2.1860(0x28000234) Process/appbrand0 WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 MiniProgramEnv/android",
            "m-appkey": "wxmp_mt-weapp",
            "accept-encoding": "gzip, deflate, br",
            "connection": "keep-alive",
            "token": self.cookie['token'],
            "uuid": self.cookie['uuid']
        }
        if(header):
            headers.update(header)
        try:
            res = requests.get(url, headers=headers)
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    def post(self, url, body='', header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; TAS-AL00 Build/N2G48C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 MMWEBID/4561 MicroMessenger/8.0.2.1860(0x29000234) Process/appbrand0 WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 MiniProgramEnv/android",
            "m-appkey": "wxmp_mt-weapp",
            "accept-encoding": "gzip, deflate, br",
            "connection": "keep-alive",
            "token": self.cookie['token'],
            "uuid": self.cookie['uuid'],
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(url, data=body, headers=headers)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def getLoginedUserInfo(self):
        url = f"https://i.meituan.com/wrapapi/getLoginedUserInfo?token={self.cookie['token']}"
        rjson = self.get(url=url, header=None)
        if(not rjson):
            self.valid = False
            return
        if("error" not in rjson):
            self.valid = True
            self.info = rjson
            print("用户昵称：", rjson['nickName'])
            print("用户号码：", rjson['mobile'])
            print("用户ID：", rjson['userId'])
        else:
            self.valid = False
            print("账号失效")

    def wxCoinInfo(self):
        url = f"https://web.meituan.com/web/user/points?token={self.cookie['token']}&userId={self.cookie['userId']}"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['success']):
            self.info.update(rjson['data'])
            print("金币余额：", rjson['data']['count'])
        else:
            print("获取微信金币信息失败：", rjson['message'])

    def wxCoinTasks(self):
        url = "https://cube.meituan.com/topcube/api/toc/task/getUserTasks"
        body = {
            "userId": self.cookie['userId'],
            "userType": "MEI_TUAN",
            "uuid": self.cookie['uuid'],
            "cityId": 934,
            "taskIdKeys": ["176f400a8f", "67bd2e0988", "672129ff6d", "6696ff7825", "7ceb1c14a7", "46ebba5312", "f5e2218b18", "c6026478e4", "7ceb1c14a7", "075eb403be", "cdb75f714d", "6f70050a62", "b6bfd8c1bc"],
            "sourceType": "MEI_TUAN",
            "mini_program_token": self.cookie['token'],
            "inviter": "",
            "inviterTaskIdKey": ""}
        rjson = self.post(url=url, body=json.dumps(body))
        if(not rjson):
            return
        if(rjson['code'] == 0):
            tasks = rjson['data']
            for task in tasks:
                # 异常任务
                if(task['code'] != 0):
                    print(f"任务[{task['title']}]：{task['msg']}")
                    continue
                # 可执行任务
                taskRuleVos = task['taskRuleVos'][0]
                if(taskRuleVos['status'] == "PRIZE_SUCC"):
                    print(f"任务[{task['title']}]：已完成")
                elif(taskRuleVos['status'] == "INIT"):
                    print(f"任务[{task['title']}]：未完成")
                    if(task['actionType'] in [12, 27]):
                        taskInfo = {}
                        taskInfo['taskIdKey'] = taskRuleVos['taskIdKey']
                        taskInfo['taskRuleIdKey'] = taskRuleVos['taskRuleIdKey']
                        taskInfo['taskRuleNo'] = taskRuleVos['taskRuleNo']
                        self.wxCoinTaskStart(taskInfo)
                        sleep(1)
        else:
            print("获取任务失败：", rjson['msg'])

    def wxCoinTaskStart(self, task):
        url = "https://cube.meituan.com/topcube/api/toc/task/startUserTask"
        body = {
            "userId": f"{self.cookie['userId']}",
            "cityId": "934",
            "mini_program_token": f"{self.cookie['token']}",
            "uuid": f"{self.cookie['uuid']}",
            "userType": "MEI_TUAN",
            "sourceType": "MEI_TUAN",
            "riskForm": self.cookie['riskForm']
        }
        body.update(task)  # 任务信息体
        rjson = self.post(url=url, body=json.dumps(body))
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print("开始任务成功")
            body['taskNo'] = rjson['taskNo']
            body['taskRuleNo'] = rjson['taskRuleNo']
            body['actionNo'] = rjson['actionNo']
            self.wxCoinTaskUpdate(body)
        else:
            print("开始任务失败：", rjson['msg'])

    def wxCoinTaskUpdate(self, task):
        url = "https://cube.meituan.com/topcube/api/toc/task/updateUserTask"
        rjson = self.post(url=url, body=json.dumps(task))
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print("完成任务成功,准备领取奖励")
            self.wxCoinTaskPrize(task)
        else:
            print("完成任务失败：", rjson['msg'])

    def wxCoinTaskPrize(self, task):
        url = "https://cube.meituan.com/topcube/api/toc/task/sendTaskPrize"
        rjson = self.post(url=url, body=json.dumps(task))
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print("领取奖励成功")
        else:
            print("领取奖励失败：", rjson['msg'])

    def wxCoinSignInfo(self):
        url = "https://cube.meituan.com/topcube/api/toc/task/getUserTasks"
        body = {
            "userId": self.cookie['userId'],
            "userType": "MEI_TUAN",
            "uuid": self.cookie['uuid'],
            "cityId": 934,
            "taskIdKeys": ["1fff834702"],
            "sourceType": "MEI_TUAN",
            "mini_program_token": self.cookie['token'],
            "inviter": "",
            "inviterTaskIdKey": ""}
        rjson = self.post(url=url, body=json.dumps(body))
        if(not rjson):
            return
        if(rjson['code'] == 0):
            data = rjson['data'][0]
            if(data['code'] == 0):
                if(data['extend']['isSignInToday'] == "1"):
                    print("今日已签到")
                else:
                    print("今日未签到")
                    taskRuleVos = data['taskRuleVos']
                    for taskRule in taskRuleVos:
                        if(taskRule['status'] == "INIT"):
                            task = {
                                "taskIdKey": taskRule['taskIdKey'],
                                "taskRuleIdKey": taskRule['taskRuleIdKey'],
                                "cubePageId": 0
                            }
                            self.wxCoinTaskStart(task)
                            break
            else:
                print("签到活动异常：", data['msg'])
        else:
            print("获取签到信息失败：", rjson['msg'])

    def wxCoinLotteryConfig(self):
        url = "https://web.meituan.com/web/user/points/lottery/config?openId=oJVP50DyvpezrN4uCDyKOzrCFnPo"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            lotteryConfig = rjson['data']['lotteryConfig']
            if(lotteryConfig['cost'] > 0):
                print("今日已参与抽奖")
            else:
                print("今日未参与抽奖")
                self.wxCoinLotteryDraw()
        else:
            print("获取抽奖信息失败：", rjson['msg'])

    def wxCoinLotteryDraw(self):
        url = "https://web.meituan.com/web/user/points/lottery/draw"
        body = {
            "uuid": self.cookie['uuid'],
            "openId": "oJVP50DyvpezrN4uCDyKOzrCFnPo",
            "expoId": "AwQAAABJAgAAAAEAAAAyAAAAPLgC95WH3MyqngAoyM/hf1hEoKrGdo0pJ5DI44e1wGF9AT3PH7Wes03actC2n/GVnwfURonD78PewMUppAAAADiXjA8/qPLUvGejBO05Yidm5pmafLNbeKDMJqd/MHRuscj3PE66t6ZEl8WXnfr0TdHWadlIygE8vw==",
            "cityId": 934,
            "appletsFingerprint": "WX__ver1.2.0_CCCC_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"}
        header = {
            "mtgsig": '{"a1":"1.1","a2":1659295379293,"a3":"1v8622uv7zu852vvy69x91u0v7299y2w817448v200y77978y3v0vw35","a4":"f6c7840d74c3cf5a0d84c7f65acfc37450ab71a30a64b2d7","a5":"kAY9EwenOakpTjR4M3KO8XZLM9ygUIydN8QERaQ0rNp8+FNPoUYrvWXJLe3uYZTIpymKenVKKWuYvTpAMdR+3kiUA1zk8n3peQr0CpdEjc7ndl+npm0LbH/NnLSph3OR+MCBd3UDzeotenZaCtzI4Do2xk9fLj6rssQZksW9HlOs7VPpGa6YwIM5W4zGGaOF+VLh3MYfjVScOSeXihJ36ThZq3OFy0ScF8agCmTyV68u","a6":"w1.1ssi/GIBHn4kzTKvcTWYWvB2n2jHBcd9eC6mDneAW9OdpifkaH4UqEYHEyS/orGr6TO2djYsl1xOxoLrWjhrSG28Jgxayp/UQ43qgYw8csY94W1abB1S/Ga3q5SNRbgkjBqak+cm0QTyiD4XfNPDMmChjimkMj0XCK3gUkx6h5HSpbpIvp9FkRO4hZMvMw2Y5S09zh6c3uHmgjm4j/u7mmRC4zbATSeeZ+uBBREHlMb+rIbM+R562EuFcW7hc6QIEEyyl0W23lI8GF3VlLcp16AxeM9ZqekZruqTKwUTI/0NLe9zqxkyhZigykxPHrTvE0oJvmBEEZhHX8IJJi7COdvd0x9niFqGMtJiyv0ok36AEX6dX92pMS1rEWY47u3PCrsgaEkHXzj0OFeiWQ5LF8N7Q7HdGzYLDgAin291S0TNk3EdbGqDPoL1uv+JKW9Ke3uQ89JjRt5S/08kZ4JfUCdoqycGMzsv6eXXEHMfYnHECqmskhCsHuXmpaRynxHvUkzY2tiXn7r0UEor2/X1DmgnjCNUERjjlyfS6YI8tV2hqCQvOMzRtZo1w3sqBNBeh90JhKaaw0rm5Wrxle9w6YW0+N9ItSr6BqMwwSbsBpwTl+lTdRBRev9N1szrO2kupI/AfTp0TP3aW7u7zaLhKxRG3jGWlbmnKsTUEF/nGBevj2wK2ONDITm7byxHoXd1K5oDzYXfm1TfMO+awAjhXFaEfKKI2FTITuNB/Y1waFka5lJBz9lSSMwTdGFzLtgu8Drkb+3lLiE/TZbwotWzQOiegVgIDGruDa+2dMW3TWON6O4JLXAEBIyoEQm0Wi1fkW/CQDSA/ERs4JkJk11DvgQ==","a7":"wxde8ac0a21135c07d","x0":3,"d1":"c2516728eb1f85c4abfdba2648116625"}'}
        rjson = self.post(url=url, body=json.dumps(body), header=header)
        print(rjson)
        if(not rjson or 'code' not in rjson):
            return
        if(rjson['code'] == 0):
            print("抽奖成功：", rjson['data']['prize']['desc'])
        else:
            print("抽奖失败：", rjson['msg'])

    def run(self):
        print(f"\n======账号[{self.index}]======")
        self.getLoginedUserInfo()
        if(not self.valid):
            return
        print("\n>>>>微信金币")
        self.wxCoinInfo()
        print("")
        self.wxCoinSignInfo()
        print("")
        self.wxCoinLotteryConfig()
        print("")
        self.wxCoinTasks()


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
            {"token": "", "userId": "", "uuid": "", "riskForm": "", "remark": ""}]}
        file.write(json.dumps(newContent, indent=2))
        file.close()
    return accountList


if __name__ == "__main__":
    cookies = initEnv()
    users = []
    index = 1
    for cookie in cookies:
        if(cookie['token'] and cookie['userId']):
            users.append(User(cookie, index=index))
            index += 1

    for user in users:
        try:
            user.run()
        except Exception as e:
            print("运行异常：", str(e))
