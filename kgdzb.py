import hashlib
import json
import os
import sys
import requests
from time import sleep, time


class User:

    def __init__(self, cookie) -> None:
        self.md5Extra = "OdwECfmgDSiXVrkR3JURLNDhvhZF4w6f"
        self.baseCookie = []
        self.baseCookie.append("appid=3166")
        self.baseCookie.append("clientver=22206")
        self.baseCookie.append("from=client")
        self.baseCookie.append("channel=56")
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
            header = {"user-agent": "Android712-1080-22206-56-0-kugou-wifi",
                      "x-router": "elder.kugou.com"}
            res = requests.get(url, headers=header)
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    # 统一POST 额外header用字典传递
    def __post__(self, url, body=None, header=None):
        try:
            header = {"user-agent": "Android712-1080-22206-56-0-kugou-wifi",
                      "x-router": "elder.kugou.com"}
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
        url = "https://gateway.kugou.com/v1/incentive/user_info?{0}".format(
            self.__getParam__(tempCookie))
        rjson = self.__get__(url)
        # print(json.dumps(rjson,indent=2))
        if(not rjson):
            self.valid = False
            return
        if(rjson and rjson['status'] == 1):
            print("用户昵称：{0}".format(rjson['data']['nickname']))
            print("用户ID：{0}".format(rjson['data']['userid']))
            print("积累金额：{0}".format(rjson['data']['money_total']))
            print("当前金额：{0}".format(rjson['data']['money']))
            print("积累金币：{0}".format(rjson['data']['total']))
            print("当前金币：{0}".format(rjson['data']['coins']))
            print("今日金币：{0}".format(rjson['data']['day_coins']))
        else:
            self.valid = False
            print("获取用户信息失败：{0}".format(rjson['error']))

    def __getTaskList__(self):
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        url = "https://gateway.kugou.com/v1/incentive/tasks_state_list?{0}".format(
            self.__getParam__(tempCookie))
        rjson = self.__get__(url)
        if(not rjson):
            return
        if(rjson and rjson['status'] == 1):
            taskList = rjson['data']['list']
            for task in taskList:
                if(task['state'] == 0):
                    self.__submitTask__(task['taskid'])
                    sleep(1)
        else:
            print("获取任务列表失败：{0}".format(rjson['error']))    

    # 提交任务
    def __submitTask__(self, taskId):
        if(taskId in [1107, 1105, 1108]):
            return
        tempCookie = self.baseCookie.copy()
        tempCookie.append("clienttime={0}".format(int(time())))
        tempCookie.append("taskid={0}".format(taskId))
        tempCookie.append("source=client")
        tempCookie.append("is_hit_new_coins_logic=0")
        tempCookie.append("time_length=0")
        url = "https://gateway.kugou.com/v1/incentive/task_submit?{0}".format(
            self.__getParam__(tempCookie))
        rjson = self.__get__(url)
        if(not rjson):
            return
        if(rjson and rjson['status'] == 1):
            print("领取任务[{0}]奖励成功：+{1}金币".format(taskId,
                  rjson['data']['awards']['coins']))
        elif("error" in rjson):
            print("领取任务[{0}]奖励失败：{1}".format(taskId, rjson['error']))
        elif("errcode" in rjson):
            print("领取任务[{0}]奖励失败：{1}".format(taskId, rjson['errcode']))

    # 执行入口
    def run(self):
        print("{0}用户信息{0}".format(10*"—"))
        self.getUserInfo()
        if(not self.valid):
            return
        print("\n{0}任务列表{0}".format(10*"—"))
        self.__getTaskList__()

def initEnv() -> list:
    cookieList = []
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\{0}.json".format("kgdzb")
    else:
        filePath += "/{0}.json".format("kgdzb")
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
    cookieList = initEnv()
    users = []
    for cookie in cookieList:
        if(cookie['cookie']):
            users.append(User(cookie['cookie']))

    for user in users:
        user.run()
