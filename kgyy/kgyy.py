import hashlib
import json
import os
import sys
import requests
from time import sleep, time


class User:

    def __init__(self, cookie, remark=None, index=1) -> None:
        self.index = index
        self.remark = remark
        self.md5Extra = "OIlwieks28dk2k092lksi2UIkp"
        self.baseCookie = []
        self.baseCookie.append("appid=1005")
        self.baseCookie.append("clientver=11109")
        self.baseCookie.append("from=client")
        self.valid = True

        # 关键字段：dfid mid token userid uuid
        checkFlag = cookie and cookie.find("dfid=") != -1 and cookie.find("mid=") != -1 and cookie.find(
            "token=") != -1 and cookie.find("userid=") != -1 and cookie.find("uuid=") != -1
        # 提取字段
        if(checkFlag):
            kvList = cookie.split("&")
            for kv in kvList:
                k_v = kv.split("=")
                if(len(k_v) == 2 and k_v[0] in ["dfid", "mid", "token", "userid", "uuid"]):
                    self.baseCookie.append(kv)
        else:
            self.valid = False
            print("用户cookie格式错误：未包含关键字段 dfid mid token userid uuid")

    # 统一GET 额外header用字典传递
    def __get__(self, url, header=None):
        try:
            res = requests.get(url, headers=header)
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    # 统一POST 额外header用字典传递
    def __post__(self, url, body='', header=None):
        try:
            res = requests.post(url, data=body, headers=header)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    # 获取参数
    def __getParam__(self, paramLsit, body=""):
        params = ""
        for param in paramLsit:
            if(params):
                params = params+"&"+param
            else:
                params = param
        params = params + "&signature="+self.__getSign__(paramLsit, body)
        return params

    # 获取签名
    def __getSign__(self, paramList, body=''):
        paramList.sort()
        signFrom = self.md5Extra
        for kv in paramList:
            signFrom = signFrom + kv
        signFrom = signFrom+body+self.md5Extra
        return self.__sign__(signFrom)

    # MD5签名函数
    def __sign__(self, s):
        hl = hashlib.md5()
        hl.update(s.encode(encoding='utf8'))
        res = hl.hexdigest()
        return str(res)

    # 获取用户基本信息
    def getUserInfo(self):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/user/info?{0}".format(
            self.__getParam__(tempCookie))
        rjson = self.__get__(url)
        if(not rjson):
            self.valid = False
            return
        if(self.remark):
            print("用户备注：{0}".format(self.remark))
        if(rjson and rjson['status'] == 1):
            print("用户昵称：{0}".format(rjson['data']['base']['nickname']))
            print("用户ID：{0}".format(rjson['data']['base']['userid']))
            print("积累金币：{0}".format(rjson['data']['account']['total_coins']))
            print("当前金币：{0}".format(rjson['data']['account']['balance_coins']))
        else:
            self.valid = False
            print("获取用户信息失败：{0}".format(rjson['error']))

    # 获取签到信息
    def getSignInfo(self):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/task/sign_state?{0}".format(
            self.__getParam__(tempCookie))
        rjson = self.__get__(url)
        if(rjson and rjson['status'] == 1):
            dayList = rjson['data']['list']
            for day in dayList:
                rewardType = day['type']
                if(day['today'] == 1 and day['state'] == 0):
                    if(rewardType == "coin"):
                        self.signOn(day['code'])
                    else:
                        print("签到奖励为VIP,跳过")
                elif(day['today'] == 1):
                    if(rewardType == "coin"):
                        print("今日已签到：+{}金币".format(day['award_coins']))
                    else:
                        print("今日已签到：+{}天VIP".format(day['award_vips']))
        else:
            print("获取签到信息失败：{0}".format(rjson['error']))

    # 签到
    def signOn(self, code):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        body = '{{"code":"{0}"}}'.format(code)
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/task/signon?{0}".format(
            self.__getParam__(tempCookie, body=body))
        rjson = self.__post__(url, body=body)
        if(rjson and rjson['status'] == 1):
            awards = rjson["data"]['awards']
            awardType = awards['type']
            if(awardType == "coin"):
                print("签到成功：+{0}金币".format(awards['coins']))
            else:
                print("签到成功：+{0}天VIP".format(awards['vips']))
        else:
            print("签到失败：{0}".format(rjson['error']))

    # 每日30抽奖信息
    def getLotteryInfo(self):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/lottery/info?{0}".format(
            self.__getParam__(tempCookie))
        rjson = self.__get__(url)
        if(rjson and rjson['status'] == 1):
            max_done_count = rjson['data']['state']['max_done_count']
            done_count = rjson['data']['state']['done_count']
            chances = rjson['data']['state']['lottery']['chances']
            print("今日已抽奖次数：{0}".format(done_count))
            print("今日剩余抽奖次数：{0}".format(max_done_count-done_count))
            if(chances):
                self.lotterySubmit()
            elif(max_done_count > done_count):
                self.getLotteryChance()
        else:
            print("获取抽奖信息失败：{0}".format(rjson['error']))

    # 每日30抽奖机会+1
    def getLotteryChance(self):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        body = '{"way":"ad"}'
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/lottery/exchange?{0}".format(
            self.__getParam__(tempCookie, body=body))
        rjson = self.__post__(url, body=body)
        if(rjson and rjson['status'] == 1):
            self.lotterySubmit()
        else:
            print("获取抽奖次数失败：{0}".format(rjson['error']))

    # 每日30抽奖
    def lotterySubmit(self):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        body = '{"taskid":1107,"user_label":{"val8":2097152,"val7":0,"val6":134221696,"val5":4,"val4":0,"val3":0,"val2":1073741825,"val1":0}}'
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/task/submit?{0}".format(
            self.__getParam__(tempCookie, body=body))
        rjson = self.__post__(url, body=body)
        if(rjson and rjson['status'] == 1):
            print("抽奖成功：+{0}{1}".format(rjson['data']['awards']['extra']['lottery_gift']
                  ['num'], rjson['data']['awards']['extra']['lottery_gift']['type']))
        else:
            print("抽奖失败：{0}".format(rjson['error']))

    # 每日81定时奖励
    def getTimeReward(self):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        body = '{"taskid":1105,"user_label":{"val8":2097152,"val7":0,"val6":134221696,"val5":4,"val4":0,"val3":0,"val2":1073741825,"val1":0}}'
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/task/submit?{0}".format(
            self.__getParam__(tempCookie, body=body))
        rjson = self.__post__(url, body=body)
        if(rjson and rjson['status'] == 1):
            print("领取定时奖励成功：+{0}金币".format(rjson['data']['awards']['coins']))
            sleep(7)
            if("double_code" in rjson['data']):
                self.getTimeRewardDouble(rjson['data']['double_code'])
            else:
                print("未发现double_code")
        else:
            print("领取定时奖励失败：{0}".format(rjson['error']))

    # 每日81定时奖励翻倍
    def getTimeRewardDouble(self, doubleCode):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        body = '{{"taskid":1105,"double_code":"{0}","double_award_type":2,"user_label":{{"val8":2097152,"val7":0,"val6":134221696,"val5":4,"val4":0,"val3":0,"val2":1073741825,"val1":0}}}}'.format(
            doubleCode)
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/task/submit?{0}".format(
            self.__getParam__(tempCookie, body=body))
        rjson = self.__post__(url, body=body)
        if(rjson and rjson['status'] == 1):
            print("领取定时翻倍奖励成功：+{0}金币".format(rjson['data']['awards']['coins']))
        else:
            print("领取定时翻倍奖励失败：{0}".format(rjson['error']))

    # 吃饭补贴信息
    def getReturnInfo(self):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        tempCookie.append("taskid=1108")
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/task/info?{0}".format(
            self.__getParam__(tempCookie))
        rjson = self.__get__(url)
        if(rjson and rjson["status"] == 1):
            if(not rjson['data']):
                print("无法获取任务信息")
                return
            meals = rjson['data']['state']['meals']
            for meal in meals:
                if(meal['state'] == 0):
                    print("{0}补贴：可领取".format(meal['name']))
                    self.getReturnAwards(meal['id'])
                elif(meal['state'] == 1):
                    print("{0}补贴：已领取".format(meal['name']))
                elif(meal['state'] == 2):
                    print("{0}补贴：未到时间".format(meal['name']))
        else:
            print("获取吃饭补贴信息失败：{0}".format(rjson['error']))

    # 领取吃饭补贴奖励
    def getReturnAwards(self, id):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        body = '{{"taskid":1108,"meal_id":{0},"user_label":{{"val8":2097152,"val7":0,"val6":134221696,"val5":4,"val4":0,"val3":0,"val2":1073741825,"val1":0}}}}'.format(
            id)
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/task/submit?{0}".format(
            self.__getParam__(tempCookie, body=body))
        rjson = self.__post__(url, body=body)
        if(rjson and rjson['status'] == 1):
            print("领取吃饭补贴成功：+{0}金币".format(rjson['data']['awards']['coins']))
            sleep(7)
            self.getReturnAwardsDouble(id, rjson['data']['double_code'])
        else:
            print("领取吃饭补贴失败：{0}".format(rjson['error']))

    # 领取吃饭补贴翻倍奖励
    def getReturnAwardsDouble(self, id, doubleCode):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        body = '{{"taskid":1108,"meal_id":{0},"double_code":"{1}","double_award_type":2,"user_label":{{"val8":2097152,"val7":0,"val6":134221696,"val5":4,"val4":0,"val3":0,"val2":1073741825,"val1":0}}}}'.format(
            id, doubleCode)
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/task/submit?{0}".format(
            self.__getParam__(tempCookie, body=body))
        rjson = self.__post__(url, body=body)
        if(rjson and rjson['status'] == 1):
            print(
                "领取吃饭补贴翻倍奖励成功：+{0}金币".format(rjson['data']['awards']['coins']))
        else:
            print("领取吃饭补贴翻倍奖励失败：{0}".format(rjson['error']))

    # 获取日常任务列表
    def getTaskList(self):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/system/infos?{0}".format(
            self.__getParam__(tempCookie))
        rjson = self.__get__(url)
        if(rjson and rjson['status'] == 1):
            tasks = rjson['data']['tasks']
            for task in tasks:
                state = task['state']
                if(state['max_done_count'] > state['done_count']):
                    self.submitTask(task['profile']['taskid'])
                sleep(1)
        else:
            print("获取日常任务列表失败：{0}".format(rjson['error']))

    # 提交任务(排除定时、抽奖和补贴)
    def submitTask(self, taskId):
        if(taskId in [1107, 1105, 1108]):
            return
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        body = '{{"taskid":{0},"user_label":{{"val8":2097152,"val7":0,"val6":134221696,"val5":4,"val4":0,"val3":0,"val2":1073741825,"val1":0}}}}'.format(
            taskId)
        url = "https://gateway.kugou.com/mstc/musicsymbol/v1/task/submit?{0}".format(
            self.__getParam__(tempCookie, body=body))
        rjson = self.__post__(url, body=body)
        if(rjson and rjson['status'] == 1):
            print("领取任务[{0}]奖励成功：+{1}金币".format(taskId,
                  rjson['data']['awards']['coins']))
        elif("error" in rjson):
            print("领取任务[{0}]奖励失败：{1}".format(taskId, rjson['error']))
        elif("errcode" in rjson):
            print("领取任务[{0}]奖励失败：{1}".format(taskId, rjson['errcode']))

    # 执行入口
    def run(self):
        print("{0}用户[{1}]信息{0}".format(10*"#",self.index))
        self.getUserInfo()
        if(not self.valid):
            return
        print("{0}每日签到{0}".format(10*"—"))
        self.getSignInfo()
        print("{0}每日抽奖{0}".format(10*"—"))
        self.getLotteryInfo()
        sleep(1)
        print("{0}定时奖励{0}".format(10*"—"))
        self.getTimeReward()
        print("{0}吃饭补贴{0}".format(10*"—"))
        self.getReturnInfo()
        print("{0}日常任务{0}".format(10*"—"))
        self.getTaskList()
        print("\n")


def initEnv() -> list:
    accountList = []
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\{0}.json".format("kgyy")
    else:
        filePath += "/{0}.json".format("kgyy")
    # 读写配置
    if(os.path.isfile(filePath)):
        file = open(filePath, "r", encoding="utf-8")
        content = file.read()
        file.close()
        accountList = json.loads(content)['accounts']
    else:
        file = open(filePath, "w+", encoding="utf-8")
        newContent = {"accounts": [{"cookie": "", "name": ""}, {"cookie": "", "name": ""}, {
            "cookie": "", "name": ""}, {"cookie": "", "name": ""}]}
        file.write(json.dumps(newContent, indent=2))
        file.close()
    return accountList


if __name__ == "__main__":
    accountList = initEnv()
    users = []
    index = 1
    for cookie in accountList:
        if(cookie['cookie']):
            users.append(
                User(cookie['cookie'], remark=cookie['name'], index=index))
            index += 1

    for user in users:
        user.run()
