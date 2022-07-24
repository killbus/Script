# -*- encoding: utf-8 -*-
'''
@项目名称：   ydyp.py
@项目地址：   
@创建时间：   2022/06/26 14:31:14
@创作者  ：   wsfsp4 
@版本号  ：   
@功能描述：   
@特别提醒：   
@更新时间：   2022/07/09 04:07:41
@更新内容：   加入邮箱果园任务
'''

import xmltodict
import json
import os
import sys
from time import sleep
import requests


class User:
    def __init__(self, account, index=1) -> None:
        self.account = account
        self.index = index
        self.authorizationValid = True
        self.gyValid = True
        self.cyValid = True

    def __get__(self, url, header=None, onlyCookie=False, isXml=False, allow_redirects=True):
        try:
            headers = {
                "X-Requested-With": "com.chinamobile.mcloud",
                "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; BRQ-AN00 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 MCloudApp/9.0.1"}
            if(header):
                headers.update(header)
            res = requests.get(url, headers=headers,
                               allow_redirects=allow_redirects)
            if(onlyCookie):
                return res.cookies.get_dict()
            else:
                if(isXml):
                    return xmltodict.parse(res.text)
                else:
                    return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    def __post__(self, url, body=None, header=None, isXml=False):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; BRQ-AN00 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 MCloudApp/9.0.1",
                       "Content-Type": "application/json",
                       "X-Requested-With": "com.chinamobile.mcloud"}
            if(header):
                headers.update(header)
            res = requests.post(url, data=body, headers=headers)
            if(isXml):
                return xmltodict.parse(res.text)
            else:
                return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def __getCurrentPath__(self):
        filePath = sys.path[0]
        if(filePath.find("\\") != -1):
            return filePath + "\\"
        else:
            return filePath + "/"

    def __querSpecToken__(self):
        url = "https://aas.caiyun.feixin.10086.cn/tellin/querySpecToken.do"
        body = "<root><account>{0}</account><toSourceId>001208</toSourceId></root>".format(
            self.account['phone'])
        header = {"Authorization": self.account['authorization'],
                  "Content-Type": "application/xml"}
        rjson = self.__post__(url=url, body=body, header=header, isXml=True)
        if(not rjson):
            self.authorizationValid = False
            return
        if(rjson["root"]['return'] == "0"):
            self.authorizationValid = True
            return rjson["root"]['token']
        else:
            print("请求Token失败：{0}".format(rjson['root']['desc']))
            self.authorizationValid = False
            return None

    def __getJwtToken__(self):
        url = "https://caiyun.feixin.10086.cn/portal/auth/tyrzLogin.action?ssoToken={0}".format(
            self.__querSpecToken__())
        rjson = self.__get__(url)
        if(not rjson):
            self.cyValid = False
            return
        if(rjson['code'] == 0):
            self.cyValid = True
            self.account['jwttoken'] = rjson['result']['token']
        else:
            self.cyValid = False
            print("获取jwttoken失败：{0}".format(rjson['msg']))

    # 获取果园Cookie
    def __getGyCookie__(self):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/login/caiyunsso.do?token={0}&account={1}&targetSourceId=001208&sourceid=1014".format(
            self.__querSpecToken__(), self.account['phone'])
        rCookie = self.__get__(url, onlyCookie=True, allow_redirects=False)
        if(not rCookie):
            self.gyValid = False
            return
        if("Os_SSo_Sid" in rCookie):
            cookie = ""
            for (k, v) in rCookie.items():
                cookie = cookie+k+"="+v+";"
            self.gyValid = True
            self.account['gyCookie'] = cookie
        else:
            self.gyValid = False
            print("获取gyCookie失败，请检查是否开通果园")

    # 果园获取果树信息
    def __gyGetTreeInfo__(self):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/user/treeInfo.do"
        header = {
            "Cookie": self.account['gyCookie']}
        rjson = self.__get__(url, header=header)
        if(not rjson):
            return
        if(rjson['success']):
            if(self.account['remark']):
                print("账号备注：{0}".format(self.account['remark']))
            print("账号昵称：{0}".format(rjson['result']['nickName']))
            print("账号手机：{0}".format(rjson['result']['userMobile']))
            print("果园等级：{0}".format(rjson['result']['treeLevel']))
            print("当前浇水：{0}".format(rjson['result']['treeWater']))
            print("剩余水滴：{0}".format(rjson['result']['collectWater']))
        else:
            print("获取云果园信息失败：{0}".format(rjson['msg']))

    # 果园获取签到信息
    def __gyCheckInfo__(self):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/task/checkinInfo.do"
        header = {
            "Cookie": self.account['gyCookie']}
        rjson = self.__get__(url, header)
        if(not rjson):
            return
        if(rjson['success']):
            if(rjson['result']['todayCheckin'] == 0):
                print("今日未签到")
                self.__gyCheckin__()
            else:
                print("今日已签到")
        else:
            print("获取签到信息失败：{0}".format(rjson['msg']))

    # 果园签到
    def __gyCheckin__(self):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/task/checkin.do"
        header = {
            "Cookie": self.account['gyCookie']}
        rjson = self.__get__(url, header)
        if(not rjson):
            return
        if(rjson['success']):
            if(rjson['result']['code'] == 1):
                print("签到成功")
            else:
                print("签到失败：{0}".format(rjson['result']['msg']))
        else:
            print("签到失败：{0}".format(rjson['msg']))

    # 果园获取任务状态
    def __gyGetTaskState__(self, header):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/task/taskState.do"
        rjson = self.__get__(url, header)
        if(not rjson):
            return
        if(rjson['success']):
            self.taskState = rjson['result']
        else:
            print("获取任务状态失败：{0}".format(rjson['msg']))

    # 果园获取任务列表
    def __gyGetTaskList__(self, header):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/task/taskList.do?clientType=PE"
        rjson = self.__get__(url, header)
        if(not rjson):
            return
        if(rjson['success']):
            tasks = rjson['result']
            for task in tasks:
                tastId = task['taskId']
                # 是否提交过标志 有些上传操作任务提交后状态为0 不能自动完成
                clickFlag = False
                for taskState in self.taskState:
                    if(taskState['taskId'] == tastId):
                        clickFlag = True
                        taskState = taskState['taskState']
                        if(taskState == 1):
                            print(
                                "任务[{0}][{1}]\t+{2}水滴 --待领取".format(task['taskName'], task['taskId'], task['waterNum']))
                            self.__gyReciveTaskAward__(task, header)
                            sleep(2)
                        elif(taskState == 2):
                            print(
                                "任务[{0}][{1}]\t+{2}水滴 --已领取".format(task['taskName'], task['taskId'], task['waterNum']))
                        elif(taskState == 0):
                            # 有些任务需要手动操作才能完成
                            print(
                                "任务[{0}][{1}]\t+{2}水滴 --未完成".format(task['taskName'], task['taskId'], task['waterNum']))
                if(not clickFlag):
                    self.__gyDoTask__(task, header)
                    sleep(3)
                    self.__gyReciveTaskAward__(task, header)
                    sleep(3)
        else:
            print("获取云果园任务列表失败：{0}".format(rjson['msg']))

    # 果园完成任务
    def __gyDoTask__(self, task, header):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/task/doTask.do?taskId={0}".format(
            task['taskId'])
        rjson = self.__get__(url, header)
        if(not rjson):
            return
        if(rjson['success']):
            if(rjson['result']['code'] == 1):
                print("参与任务[{0}][{1}]成功".format(
                    task['taskName'], task['taskId']))
            else:
                print("参与任务[{0}][{1}]失败：{2}".format(
                    task['taskName'], task['taskId'], rjson['result']['summary']))
        else:
            print("参与任务[{0}][{1}]失败：{2}".format(
                task['taskName'], task['taskId'], rjson['msg']))

    # 果园任务领取奖励
    def __gyReciveTaskAward__(self, task, header):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/task/givenWater.do?taskId={0}".format(
            task['taskId'])
        rjson = self.__get__(url, header)
        if(not rjson):
            return
        if(rjson['success']):
            if(rjson['result']['code'] == 1):
                print("任务[{0}][{1}]奖励领取成功：+{2}水滴".format(task['taskName'],
                      task['taskId'], rjson["result"]['water']))
            else:
                print("任务[{0}][{1}]奖励领取失败：{2}".format(
                    task['taskName'], task['taskId'], rjson['result']['msg']))
        else:
            print("任务[{0}][{1}]奖励领取失败：{2}".format(
                task['taskName'], task['taskId'], rjson['msg']))

    # 果园任务总入口
    def __gyTaskEnter__(self):
        yxHeader = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; P40 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36(139PE_WebView_Android_9.3.3)",
            "Cookie": self.account['gyCookie']}
        ypHeader = {
            "Cookie": self.account['gyCookie']
        }
        print("【邮箱果园任务】")
        self.__gyGetTaskState__(yxHeader)
        sleep(3)
        self.__gyGetTaskList__(yxHeader)
        sleep(3)
        print("【云盘果园任务】")
        self.__gyGetTaskState__(ypHeader)
        sleep(3)
        self.__gyGetTaskList__(ypHeader)
        sleep(3)

    # 果园获取点击奖励
    def __gyClickCartoon__(self):
        cartoonType = ["color", "widget"]
        for cartoon in cartoonType:
            url = "https://happy.mail.10086.cn/jsp/cn/garden/user/clickCartoon.do?cartoonType={0}".format(
                cartoon)
            header = {
                "Cookie": self.account['gyCookie']}
            rjson = self.__get__(url, header)
            if(not rjson):
                continue
            if(rjson['success']):
                if(rjson['result']["code"] == 1):
                    if("given" in rjson['result']):
                        print("获取场景[{0}]水滴成功：+{1}水滴".format(cartoon,
                              rjson['result']['given']))
                    else:
                        print("获取场景[{0}]水滴成功".format(cartoon))
                else:
                    print("获取场景[{0}]水滴失败：{1}".format(
                        cartoon, rjson['result']['msg']))
            else:
                print("获取场景[{0}]水滴失败：{1}".format(cartoon, rjson['msg']))

    # 果园开宝箱
    def __gyOpenBox__(self):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/prize/openBox.do"
        header = {
            "Cookie": self.account['gyCookie']}
        rjson = self.__get__(url, header)
        if(not rjson):
            return
        if(rjson['success']):
            if(rjson['result']['code'] == 1):
                print("开启宝箱成功：+{0}水滴".format(rjson['result']['water']))
            else:
                print("开启宝箱失败：{0}".format(rjson['result']['msg']))
        else:
            print("开启宝箱失败：{0}".format(rjson['msg']))

    # 果园浇水
    def __gyWatering__(self):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/user/watering.do?isFast=1"
        header = {
            "Cookie": self.account['gyCookie']}
        while(True):
            rjson = self.__get__(url, header)
            if(not rjson):
                return
            if(rjson['success']):
                if(rjson['result']['code'] == 1):
                    print("浇水成功：-{0}水滴".format(rjson['result']['water']))
                    if(rjson['result']['upgrade'] == 1):
                        print("果园升级！")
                    sleep(4)
                else:
                    print("浇水失败：{0}".format(rjson['result']['msg']))
                    return
            else:
                print("浇水失败：{0}".format(rjson['msg']))
                return

    # 果园邀请信息
    def __gyInviteInfo__(self):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/friend/backupUser.do"
        header = {
            "Cookie": self.account['gyCookie']}
        rjson = self.__get__(url, header)
        if(not rjson):
            return
        if(rjson['success']):
            inviteCount = len(rjson['result'])
            print("今日果园受助次数：{0}".format(inviteCount))
            if(inviteCount < 3):
                self.__gyInviteCode__()
        else:
            print("获取助力信息失败：{0}".format(rjson['msg']))

    # 果园邀请码获取
    def __gyInviteCode__(self):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/friend/inviteCode.do"
        header = {
            "Cookie": self.account['gyCookie']}
        rjson = self.__get__(url, header)
        if(not rjson):
            return
        if(rjson['result']):
            self.account['gyInviteCode'] = rjson['result']
            print("获取助力码成功：{0}".format(rjson['result']))
        else:
            print("获取邀请码失败：{0}".format(rjson['msg']))

    # 果园助力
    def gyInviteFriend(self, inviteCode, invitePhone):
        url = "https://happy.mail.10086.cn/jsp/cn/garden/wx/inviteFriend.do?inviteCode={0}&inviteType=backup&clientName=HCY".format(
            inviteCode)
        header = {
            "Cookie": self.account['gyCookie']}
        rjson = self.__get__(url, header)
        if(not rjson):
            return
        if(rjson['result']):
            if(rjson['result']['code'] == 1):
                print("[{0}]助力[{1}]成功".format(
                    self.account['phone'], invitePhone))
            else:
                print("[{0}]助力[{1}]失败：{2}".format(
                    self.account['phone'], invitePhone, rjson['result']['msg']))
        else:
            print("[{0}]助力[{1}]失败：{2}".format(
                self.account['phone'], invitePhone, rjson['msg']))

    # 云朵作战信息
    def __hcInfo__(self):
        url = "https://caiyun.feixin.10086.cn/market/signin/hecheng1T/info?op=info"
        header = {"jwttoken": self.account['jwttoken']}
        rjson = self.__get__(url, header=header)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            history = rjson['result']['history']
            info = rjson['result']['info']
            curr = info['curr']
            if(self.account['remark']):
                print("账号备注：{0}".format(self.account['remark']))
            print("账号手机：{0}".format(info['phone']))
            print("合成次数：{0}".format(info['succ']))
            print("可用次数：{0}".format(curr))
            if("0" in history):
                print("本月排名：{0}".format(history['0']['rank']))
            elif("-1" in history):
                print("上月排名：{0}".format(history['-1']['rank']))
            if(curr > 0):
                print("")
            while(curr > 0):
                self.__hcBeinvite__()
                sleep(5)
                curr -= 1
        else:
            print("获取信息失败：{0}".format(rjson['msg']))

    # 云朵作战邀请
    def __hcBeinvite__(self):
        url = "https://caiyun.feixin.10086.cn/market/signin/hecheng1T/beinvite"
        header = {"jwttoken": self.account['jwttoken']}
        rjson = self.__get__(url, header=header)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print("开始合成游戏，等待5s...")
            sleep(5)
            self.__hcFinish__()
        else:
            print("开始合成游戏失败：{0}".format(rjson['msg']))

    # 云朵作战完成游戏
    def __hcFinish__(self):
        url = "https://caiyun.feixin.10086.cn/market/signin/hecheng1T/finish?flag=true"
        header = {"jwttoken": self.account['jwttoken']}
        rjson = self.__get__(url, header=header)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print("合成成功！")
        else:
            print("合成失败：{0}".format(rjson['msg']))

    # 云朵作战开始游戏
    def __hcRecord__(self):
        url = "https://caiyun.feixin.10086.cn/market/signin/public/cloudRecord?marketname=hecheng1T&type=1&pageNumber=1&pageSize=1000"
        header = {"jwttoken": self.account['jwttoken']}
        rjson = self.__get__(url, header=header)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            records = rjson['result']['records']
            if(len(records) == 0):
                print("暂无中奖记录")
            else:
                print("奖励记录：")
                for record in records:
                    print(
                        "{0}\t +{1}云朵".format(record['inserttime'], record['num']))
        else:
            print("获取中奖记录失败：{0}".format(rjson['msg']))

    # 彩云中心信息
    def __cyInfo__(self):
        url = "https://caiyun.feixin.10086.cn/market/signin/page/info"
        header = {"jwttoken": self.account['jwttoken']}
        rjson = self.__get__(url, header=header)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            result = rjson['result']
            print("当前云朵：{0}".format(result['total']))
            print("待收云朵：{0}".format(result['toReceive']))
            print("签到次数：{0}".format(result['monthDays']))
            print("")
            if(result['todaySignIn']):
                print("今日已签到")
            else:
                print("今日未签到")
        else:
            print("获取云朵中心信息失败：{0}".format(rjson['msg']))

    # 彩云中心任务列表
    def __cyTaskList__(self):
        url = "https://caiyun.feixin.10086.cn/market/signin/task/taskList?marketname=sign_in_3"
        header = {"jwttoken": self.account['jwttoken']}
        rjson = self.__get__(url, header=header)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            taskType = ["new", "month", "day"]
            taskTypeDict = {"new": "新手任务", "month": "月任务", "day": "每日任务"}
            for type in taskType:
                if(type in rjson['result']):
                    print("【{0}】".format(taskTypeDict[type]))
                    newTask = rjson['result'][type]
                    for task in newTask:
                        state = task['state']
                        if(state == "FINISH"):
                            print("[{0}] --已完成".format(task['name']))
                        elif(state == "WAIT"):
                            print("[{0}] --未完成".format(task['name']))
                            self.__cyTaskClick__(task['id'])
        else:
            print("获取任务列表失败：{0}".format(rjson['msg']))

    # 彩云中心任务点击
    def __cyTaskClick__(self, taskId):
        url = "https://caiyun.feixin.10086.cn/market/signin/task/click?key=task&id={0}".format(
            taskId)
        header = {"jwttoken": self.account['jwttoken']}
        rjson = self.__get__(url, header=header)

    # 彩云中心收奖励
    def __cyReceive__(self):
        url = "https://caiyun.feixin.10086.cn/market/signin/page/receive"
        header = {"jwttoken": self.account['jwttoken']}
        rjson = self.__get__(url, header=header)
        if(not rjson):
            return
        if(rjson['code'] == 0):
            print("本次收取云朵：{0}".format(rjson['result']['receive']))
            print("当前拥有云朵：{0}".format(rjson['result']['total']))
        else:
            print("收取云朵失败：{0}".format(rjson['msg']))
    
    def invite(users):
        print("》》》》果园助力")
        for userA in users:
            for userB in users:
                if(userA.account['phone'] == userB.account['phone'] or "gyInviteCode" not in userB.account):
                    continue
                else:
                    userA.gyInviteFriend(
                        userB.account['gyInviteCode'], userB.account['phone'])
                    sleep(10)

    def run(self):
        print("{0}账号[{1}]{0}".format(10*"=", self.index))
        print("》》》》云盘")
        if(os.path.isfile(self.__getCurrentPath__()+"ydypSDK.py")):
            from ydypSDK import SDK
            sdk = SDK(self.account)
            sdk.run()
        else:
            print("当前目录未发现SDK，无法执行任务\n")
        print("")
        self.__querSpecToken__()
        if(not self.authorizationValid):
            return
        self.__getGyCookie__()
        if(self.gyValid):
            print("》》》》云果园")
            self.__gyGetTreeInfo__()
            sleep(3)
            print("")
            self.__gyCheckInfo__()
            sleep(3)
            print("")
            self.__gyTaskEnter__()
            print("")
            self.__gyClickCartoon__()
            sleep(3)
            print("")
            self.__gyWatering__()
            sleep(3)
            print("")
            self.__gyOpenBox__()
            sleep(3)
            print("")
            self.__gyInviteInfo__()
            print("")
        self.__getJwtToken__()
        if(self.cyValid):
            print("》》》》云朵大作战")
            self.__hcInfo__()
            print("")
            sleep(3)
            self.__hcRecord__()
            print("")
            print("》》》》云朵中心")
            self.__cyInfo__()
            sleep(3)
            print("")
            self.__cyTaskList__()
            sleep(3)
            print("")
            self.__cyReceive__()
            print("")


def initEnv() -> list:
    accountList = []
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\{0}.json".format("ydyp")
    else:
        filePath += "/{0}.json".format("ydyp")
    # 读写配置
    if(os.path.isfile(filePath)):
        file = open(filePath, "r", encoding="utf-8")
        content = file.read()
        file.close()
        accountList = json.loads(content)['accounts']
    else:
        file = open(filePath, "w+", encoding="utf-8")
        newContent = {"accounts": [
            {"gyCookie": "", "session": "", "remark": ""}]}
        file.write(json.dumps(newContent, indent=2))
        file.close()
    return accountList


if __name__ == "__main__":
    accountList = initEnv()
    users = []
    index = 1
    for account in accountList:
        if(account['authorization'] and account['phone']):
            users.append(User(account, index))
            index += 1
    for user in users:
        user.run()
        print("\n")
    User.invite(users)

