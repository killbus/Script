import os
from time import sleep, time
import warnings
import requests
import json
from urllib import parse

API_URL = "http://192.168.3.33:8888/4399/sig/?str="
COOKIE_NAME = "4399Headers"
warnings.filterwarnings("ignore")

class User:
    def __init__(self, header, index) -> None:
        self.header = self.parseHeaders(header)
        self.index = index

    def get(self, url, header=None, isText=False):
        headers = self.header.copy()
        if(header):
            headers.update(header)
        try:
            res = requests.get(url, headers=headers,verify=False)
            if(isText):
                return res.text
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    def post(self, url, body='', header=None):
        headers = self.header.copy()
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(url, data=body, headers=headers,verify=False)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def parseHeaders(self, str):
        res = {}
        headers = str.split("\n")
        for hs in headers:
            hs = hs.split(":", 1)
            if(len(hs) == 2 and hs[1].strip()):
                res[hs[0]] = hs[1].strip()
        res.pop("Content-Length", "")
        return res

    # 获取Sign
    def getSign(self, param):
        url = API_URL+parse.quote(param)
        return self.get(url, isText=True)

    def buildSignValue(self,values):
        keys = sorted(values.keys())
        str = ""
        for key in keys:
            if(values[key] != ""):
                str += f"{values[key]}"
        return str

    def centerIndex(self):
        url = "https://mapi.yxhapi.com/user/task/box/android/v2.1/center-index.html"
        rjson = self.post(url)
        if(not rjson):
            self.valid = False
            return
        if(rjson['code'] == 100):
            self.valid = True
            self.centerUserInfo(rjson['result']['user_info'])
            self.centerSign(rjson['result']['sign'])
            self.centerTasks(rjson['result']['daily'])
        else:
            self.valid = False
            print("账号异常："+rjson['message'])

    def centerUserInfo(self,userInfo):
        self.usrInfo = userInfo
        print(f"用户ID：{userInfo['pt_uid']}")
        print(f"普通盒币：{userInfo['hebi']} ≈ {userInfo['hebi']/100}元")
        print(f"超级盒币：{userInfo['super_hebi']}")

    def centerTasks(self,daily):
        if(daily['unlock'] == 0):
            print("今日任务未解锁\n")
            self.unlockTask()
        else:
            print("今日任务已解锁\n")
        print(">>>>>>日常任务")
        for task in daily["data"]:
            if(task['finish']):
                print(f"任务[{task['title']}]已完成")
            else:
                print(f"任务[{task['title']}]未完成")
                taskParams = {}
                taskParams['ptUid'] = self.usrInfo['pt_uid']
                taskParams['mac'] = self.header['mdeviceId']
                taskParams['deviceId'] = self.header['mdeviceId']
                taskParams['androidId'] = self.header['mdeviceId'].replace(":","A")[0:15]        
                if(task['title'] != "开启微信提醒"):
                    taskParams['taskId'] = task['id']
                    taskParams['action'] = task['action']
                    self.acceptTask(taskParams)
                    sleep(3)

    def centerSign(self,sign):
        print(f"积累签到天数：{sign['total_signed']}")
        print(f"周期签到天数：{sign['signed_day']}\n")
        if(sign['today_signed']):
            print("今日已签到")
        else:
            print("今日未签到")
            #self.signIn(sign['signed_day'])

    #签到
    def signIn(self, day):
        url = "https://mapi.yxhapi.com/android/box/v3.0/sign-in.html"
        params = {
            "dateline":int(time()),
            "packages":[],
            "day":day,
            "deviceId":self.header['mdeviceId']
        }
        sign = self.getSign(self.buildSignValue(params))
        if(not sign):
            return
        params['sign'] = sign
        rjson = self.post(url, body=parse.urlencode(params))
        if(not rjson):
            return
        if(rjson['code'] == 100):
            print("签到成功")
        else:
            print("签到失败："+json.dumps(rjson))

    #解锁任务
    def unlockTask(self):
        sign = self.getSign(self.header['mdeviceId']+self.usrInfo['pt_uid'])
        if(not sign):
            return
        url = f"https://mapi.yxhapi.com/user/task/box/android/v1.0/daily-unlockList.html?sign={sign}&ptUid={self.usrInfo['pt_uid']}&deviceId={self.header['mdeviceId']}"
        rjson = self.get(url)
        if(rjson['code'] == 100):
            print("解锁任务成功")
        else:
            print("解锁任务失败："+rjson['message'])

    #完成任务
    def acceptTask(self,task):
        sign =  self.getSign(self.buildSignValue(task))
        if(not sign):
            return
        task['sign'] = sign
        url = "https://mapi.yxhapi.com/user/task/box/android/v1.2/daily-accept.html?"+parse.urlencode(task)
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 100):
            print(f"完成任务[{rjson['result']['title']}]成功：+{rjson['result']['hebi']}盒币")
        else:
            print(f"完成任务失败：{rjson['message']}")

    #动态、资讯获取
    def getArticle(self):
        url = "https://mapi.yxhapi.com/forums/box/android/v1.0/home-short.html"
        body = "startKey=&install_game_ids=105423%2C105794%2C105793&action=fresh&deviceName=P40"
        rjson = self.post(url, body=body)
        if(not rjson):
            return
        if(rjson['code'] == 100):
            popularList = rjson['result']['popularList']
            popular = popularList[0]
            # 动态类型
            if("feedId" in popular):
                article = {}
                article['id'] = popular['feedId']
                article['isFollow'] = popular['info']['rec']['is_follow']
                self.readArticle(article)
            ##article['quan_id'] = popular['info']['quan_info']['id']
        else:
            print("获取主页游戏动态失败："+rjson['message'])

    #动态详细
    def readArticle(self, article):
        url = f"https://mapi.yxhapi.com/feed/box/android/v4.2/detail.html?isFollow={article['isFollow']}&startKey=&id={article['id']}&n=20"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['code'] == 100):
            print(f"读取动态[{article['id']}]成功")
            self.followArticler(rjson['result']['user']['pt_uid'])
            self.declareArticle(article)
            comments = rjson['result']['comments']['data']
            if(comments and len(comments) > 0):
                sleep(1)
                article['commentId'] = comments[0]['id']
                self.declareArticleReply(article)
        else:
            print(f"读取动态[{article['id']}]失败："+rjson['message'])

    #动态用户关注
    def followArticler(self, id):
        url = "https://mapi.yxhapi.com/user/sns/box/android/v3.0/follow-add.html"
        body = f"startKey=&ids={id}&from=3&n=20"
        rjson = self.post(url, body=body)
        if(not rjson):
            return
        if(rjson['code'] == 100):
            print(f"关注动态用户[{id}]成功")
        else:
            print(f"点赞动态动态[{id}]失败："+rjson['message'])

    #动态点赞
    def declareArticle(self, article):
        url = "https://mapi.yxhapi.com/feed/box/android/v1.0/declare.html"
        body = f"feed_id={article['id']}"
        rjson = self.post(url, body=body)
        if(not rjson):
            return
        if(rjson['code'] == 100):
            print(f"点赞动态[{article['id']}]成功")
        else:
            print(f"点赞动态[{article['id']}]失败："+rjson['message'])

    #动态点赞评论
    def declareArticleReply(self, article):
        url = f"https://mapi.yxhapi.com/feed/box/android/v1.0/comment-declare.html"
        body = f"id={article['commentId']}&tid={article['id']}"
        rjson = self.post(url, body=body)
        if(not rjson):
            return
        if(rjson['code'] == 100):
            print(f"点赞动态评论[{article['id']}][{article['commentId']}]成功")
        else:
            print(
                f"点赞动态评论[{article['id']}][{article['commentId']}]失败："+rjson['message'])

    def run(self):
        print(f"======账号[{self.index}]======")
        self.centerIndex()
        if(self.valid):
            print("\n>>>>>游戏动态")
            self.getArticle()


def initEnv():
    env = os.environ
    env[COOKIE_NAME] = '''mauth: 0b4538bf7a9dc3f083ee0e1575b7e55e
mareacode: 440100
zxaid: A01-itPJ%2B%2Bg%2FgN855oceHJm1Odpg%2FYk%2FT6ZS
mauthcode: 12b8da274|6be278bc780caca6f886c6c34f5ccccb|3303007075
SM-DEVICEID: 20220809141325e003faf6ef8c79d35d70564e67ae6d74010942b021997e03
m-id: B0%3A12%3A69%3A69%3A25%3A9E
a-id: 7A962E41866879B2
e-id: 
User-Agent: 4399GameCenter/6.8.0.59(android;P40;7.1.2;720x1184;WIFI;1791.840;baidu)
mdeviceId: B0:12:69:69:25:9E
pauth: 3303007075%7C14767929623%7Cc17e20c7129f7c4b162fe4580b546ac5%7C1660032882%7C10001%7Cc942ee14b99db8674b5c3dd9d261ba8d%7C0
s-id: 
mudid: 1103gKwPpiHUAcWIdHsXeee3b
Content-Type: application/x-www-form-urlencoded
Content-Length: 140
Host: mapi.yxhapi.com
Connection: Keep-Alive
Accept-Encoding: gzip
'''
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
        user.run()
