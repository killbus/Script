import json
from operator import index
import os
from random import randint
from time import sleep
import requests


COOKIE_NAME = "gqslAccount"


class User:
    def __init__(self, data, index) -> None:
        self.data = data
        self.index = index
        self.authorization = ""

    def get(self, url, header=None):
        headers = {
            "Content-Type": "application/json",
            "appversion": "2.3.0",
            "operatesystem": "android",
            "dataencrypt": "false",
            "authorization": self.authorization
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
            "appversion": "2.3.0",
            "operatesystem": "android",
            "dataencrypt": "false",
            "authorization": self.authorization
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

    def login(self):
        url = "https://mspace.gmmc.com.cn/user-soa/user/account/sign-in"
        rjson = self.post(url=url, body=self.data)
        if(not rjson):
            self.valid = False
            return
        if(rjson['code'] == "0000"):
            self.valid = True
            data = rjson['data']
            self.authorization = data['token']
            print("用户昵称：", data['userInfo']['nickname'])
            print("用户号码：", data['userInfo']['mobile'])
            print("用户ID：", data['userInfo']['userId'])
        else:
            self.valid = False
            print("登录失败：", rjson['msg'])

    def getTasks(self):
        url = "https://mspace.gmmc.com.cn/customer-app/task-mapi/sign-in/detail?noLoad=true"
        body = {"taskTypeCode": "TASK-INTEGRAL-SIGN-IN",
                "appVersion": "2.3.0", "operateSystem": "android"}
        rjson = self.post(url, json.dumps(body))
        if(not rjson):
            return
        if(rjson['code'] == "0000"):
            data = rjson['data']
            print(f"现有积分：{data['totalIntegral']}")
            print(f"签到天数：{data['signInDays']}\n")
            banners = data['pageInfo']['banners']
            for banner in banners:
                if(banner['type'] == -3):
                    print("【连续签到奖励】")
                    print(
                        f"盲盒进度：{banner['contents']['progress']}/{banner['contents']['currentTotalProgress']}")
                elif(banner['type'] == -1):
                    print("【今日任务】")
                    tasks = banner['contents']
                    for task in tasks:
                        print(f"任务[{task['title']}]  {task['subTitle']}")
                        if(task['buttonTip'] == "已完成"):
                            continue
                        if(task['taskId'] == 19):
                            self.dynamicLikeEnter(5)
                        elif(task['taskId'] == 2):
                            self.addDynamics()
                        elif(task['taskId'] == 8):
                            self.dynamicComment()
                        elif(task['taskId'] in [4, 5]):
                            self.shareDynamics()
                        sleep(2)
                elif(banner['type'] == -2):
                    print("【新手任务】")
                    tasks = banner['contents']
                    for task in tasks:
                        print(f"任务[{task['title']}]  {task['subTitle']}")
        else:
            print(f"获取任务列表失败：{rjson['msg']}")

    # 获取随机名言
    def getRandomWord(self):
        url = "https://v1.hitokoto.cn/"
        rjson = self.get(url)
        if(not rjson):
            return "越是困难，越要抬起头，地上可找不到任何希望！"
        else:
            return rjson['hitokoto']

    # 获取动态列表
    def getDynamics(self):
        url = "https://mspace.gmmc.com.cn/social-cms-app/frontend/dynamic/queryByPage?pageNo=1&pageSize=20&type=2&dimensionType=1"
        rjson = self.get(url)
        if(not rjson):
            return []
        if(rjson['code'] == "0000"):
            return rjson['data']['list']
        else:
            print("获取动态列表失败：", rjson['msg'])
            return []

    # 分享动态
    def shareDynamics(self):
        url = "https://mspace.gmmc.com.cn/customer-app/integral-task/complete/share?noLoad=true"
        for type in [4, 5]:
            body = {"taskType": type}
            rjson = self.post(url, json.dumps(body))
            if(not rjson):
                continue
            if(rjson['code'] == "0000"):
                print(f"执行分享任务[{type}]成功")
            else:
                print(f"执行分享任务[{type}]失败：", rjson['msg'])

    # 发布动态
    def addDynamics(self):
        url = "https://mspace.gmmc.com.cn/social-cms-app/frontend/dynamic/add"
        content = ""
        for i in range(10):
            content = self.getRandomWord()
            if(len(content) >= 15):
                break
        body = {"activityId": 0, "backgroundContent": content,
                "btype": 0, "content": content, "lat": 0.0, "lng": 0.0}
        rjson = self.post(url, body=json.dumps(body))
        if(not rjson):
            return
        if(rjson['code'] == "0000"):
            print("发布动态成功")
        else:
            print("发布动态失败：", rjson['msg'])

    # 动态评论
    def dynamicComment(self):
        dynamiics = self.getDynamics()
        if(len(dynamiics) == 0):
            return
        dynamiic = dynamiics[randint(0, len(dynamiics))]
        url = "https://mspace.gmmc.com.cn/social-cms-app/frontend/comment/add"
        content = ""
        for i in range(10):
            content = self.getRandomWord()
            if(len(content) >= 15):
                break
        body = {
            "commentContent": content,
            "commentType": 2,
            "commentTypeBusinessId": f"{dynamiic['dynamicId']}"
        }
        rjson = self.post(url, body=json.dumps(body))
        if(not rjson):
            return
        if(rjson['code'] == "0000"):
            print(f"评论动态[{dynamiic['dynamicId']}]成功")
        else:
            print(f"评论动态[{dynamiic['dynamicId']}]失败：{rjson['msg']}")

    # 动态点赞入口
    def dynamicLikeEnter(self, count):
        dynamiics = self.getDynamics()
        if(len(dynamiics) > 0 and count > 0):
            for index in range(count):
                if(index > len(dynamiics) or index >= count):
                    break
                dynamiic = dynamiics[index]
                print(f"动态[{dynamiic['dynamicId']}]:准备点赞")
                self.dynamicLike(dynamiic['dynamicId'], 1)
                sleep(2)

    # 动态点赞
    def dynamicLike(self, dynamicId, status):
        url = "https://mspace.gmmc.com.cn/social-cms-app/frontend/dynamic/liked"
        body = {
            "dynamicId": dynamicId,
            "status": status
        }
        rjson = self.post(url, json.dumps(body))
        if(not rjson):
            return
        if(rjson['code'] == "0000"):
            print(f"动态[{dynamicId}]:点赞成功")
        else:
            print(f"动态[{dynamicId}]:点赞失败，{rjson['msg']}")

    # 签到信息
    def signInfo(self):
        url = "https://mspace.gmmc.com.cn/customer-app/task-mapi/sign-count?noLoad=true"
        body = {"taskTypeCode": "TASK-INTEGRAL-SIGN-IN"}
        rjson = self.post(url, json.dumps(body))
        if(not rjson):
            return
        if(rjson['code'] == "0000"):
            if(rjson['data']['isSignIn']):
                print("今日已签到")
            else:
                print("今日未签到")
                self.signIn()
        else:
            print(f"获取签到信息失败：{rjson['msg']}")

    # 签到
    def signIn(self):
        url = "https://mspace.gmmc.com.cn/customer-app/task-mapi/sign-in?noLoad=true"
        body = {
            "taskTypeCode": "TASK-INTEGRAL-SIGN-IN",
            "appversion": "2.3.0",
            "operatesystem": "android",
            "step": 1}
        rjson = self.post(url, json.dumps(body))
        if(not rjson):
            return
        if(rjson['code'] == "0000"):
            print("签到成功")
        else:
            print(f"签到失败：{rjson['msg']}")

    def run(self):
        print(f"======账号[{self.index}]======")
        self.login()
        if(not self.valid):
            return
        self.getTasks()
        print("")
        self.signInfo()
        print("\n")


def initEnv():
    env = os.environ
    if(COOKIE_NAME in env):
        cookies = env[COOKIE_NAME]
        if(cookies.find("&")):
            return cookies.split("&")
    return []


if __name__ == "__main__":
    accounts = initEnv()
    users = []
    index = 1
    for account in accounts:
        users.append(User(account, index))
        index += 1
    for user in users:
        try:
            user.run()
        except Exception as e:
            print("运行异常：", str(e))
