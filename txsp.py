# -*- encoding: utf-8 -*-
'''
@项目名称：   txsp.py
@更新时间：   2022/07/29 21:42:49
@版本号  ：   1.0
@环境变量：   txspCookie 福利中心抓取Cookie
@更新内容：   福利中心任务
'''

import json
import os
from time import sleep
import requests


COOKIE_NAME = "txspCookie"


class User:


    def __init__(self, cookie, index=1) -> None:
        self.cookie = cookie
        self.valid = True
        self.index = index

    def get(self, url, header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A465 QQLiveBrowser/8.5.95 AppType/UN WebKitCore/WKWebView iOS GDTTangramMobSDK/4.370.6 GDTMobSDK/4.370.6 cellPhone/iPhone 12",
            "referer": "https://fuli.v.qq.com/",
            "origin": "https://fuli.v.qq.com/", 
            "cookie": self.cookie
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
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A465 QQLiveBrowser/8.5.95 AppType/UN WebKitCore/WKWebView iOS GDTTangramMobSDK/4.370.6 GDTMobSDK/4.370.6 cellPhone/iPhone 12",
            "referer": "https://fuli.v.qq.com/",
            "origin": "https://fuli.v.qq.com/", 
            "accept-encoding":"gzip, deflate, br",
            "connection":"keep-alive",
            "cookie": self.cookie
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


    def vipInfo(self):
        url = "https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_SVipInfo&cmd=1&source_scene=4&otype=xjson"
        rjson = self.get(url=url)
        if(not rjson):
            self.valid = False
            return
        if("msg" not in rjson):
            self.valid = True
            self.nickname = rjson['nick']
            self.vipInfo = rjson["hlw"]
            print("用户昵称：",self.nickname)
            if(self.vipInfo['vip']):
                print("VIP状态：有效")
            else:
                print("VIP状态：过期")
            print("VIP等级：",self.vipInfo['level'])
            print("VIP经验：",self.vipInfo['score'])
        else:
            self.valid = False
            print("获取账号信息失败：",rjson["msg"])

    def welfareCenter(self,onlyCoin = False):
        url = "https://pbaccess.video.qq.com/activity/welfare_center/v2/queryUserActivityNew"
        body = {"activity_id":1001}
        rjson = self.post(url=url,body=json.dumps(body))
        if(not rjson):
            return
        if("msg" not in rjson):
            self.coin = rjson['data']['asset_info']['coin']
            if(onlyCoin):
                print(f"账号[{self.nickname}]：{self.coin}")
                return
            print("福利金币：",self.coin)

            tasks = rjson['data']['task_info']
            print("")
            if(len(tasks['watch_video_info']['watch_video_record'])>=2):
                print("任务[播放视频]已完成")
            else:
                print("任务[播放视频]未完成")
                self.taskWatch()
            if(len(tasks['browse_info']['browse_record'])>=2):
                print("任务[浏览商店]已完成")
            else:
                print("任务[浏览商店]未完成")
                self.taskBrowse()
            print(f"任务[好友助力]进度：{tasks['help_share_info']['help_share_count']}/{tasks['help_share_info']['help_share_limit']}")
            if(tasks['help_share_info']['help_share_count'] != tasks['help_share_info']['help_share_limit']):
                self.needHelp = True
                self.shareCode = rjson['data']['vuid_encoded']
            else:
                self.needHelp = False
        else:
            print("获取福利中心信息失败：",rjson['msg'])

    def taskBrowse(self):
        url = "https://pbaccess.video.qq.com/activity/platform/gateway/v2/browse"
        body = {"activity_id":"1001","browse_page":"caochangdi","task_group_id":"4"}
        rjson = self.post(url,body=json.dumps(body))

        if(rjson['err_msg'] == "success"):
            print("任务[浏览商店]执行成功")
        else:
            print("任务[浏览商店]执行失败：",rjson['err_msg'])

    def taskWatch(self):
        url = "https://pbaccess.video.qq.com/activity/platform/gateway/v2/WatchVideo"
        body = {"activity_id":"1001","vid":"mzc00200p51jpn7","task_group_id":"1"}
        rjson = self.post(url,body=json.dumps(body))

        if(rjson['err_msg'] == "success"):
            print("任务[播放视频]执行成功")
        else:
            print("任务[播放视频]执行失败：",rjson['err_msg'])        

    def signInfo(self):
        url = "https://pbaccess.video.qq.com/activity/platform/gateway/v2/querySignInfo"
        body = {"activity_id":"1001","task_group_id":5}
        rjson = self.post(url=url,body=json.dumps(body))
        if(not rjson):
            return
        if(not rjson['err_msg']):
            if(rjson['data']['is_sign']):
                print("今日已签到")
            else:
                print("今日未签到")
                self.signIn()
        else:
            print("获取签到信息失败：",rjson['err_msg'])

    def signIn(self):
        url = "https://pbaccess.video.qq.com/activity/platform/gateway/v2/signPlay"
        body = {"activity_id":"1001","task_group_id":5}
        rjson = self.post(url=url,body=json.dumps(body))
        if(not rjson):
            return
        if(rjson['err_msg'] == "success"):
            print(f"签到成功：+{rjson['data']['reward_count']}金币")
        else:
            print("签到失败：",rjson['err_msg'])

    def shareHelp(self, users):
        if(not self.valid):
            return
        for user in users:
            if(user.cookie == self.cookie):
                continue
            if(not user.valid or not user.needHelp):
                continue
            url = "https://pbaccess.video.qq.com/activity/platform/gateway/v2/helpShare"
            body = {"activity_id":"1001","task_group_id":2,"sponsor_id":user.shareCode}
            rjson = self.post(url=url,body=json.dumps(body))
            if(not rjson):
                continue
            if(rjson['err_msg'] == "success"):
                print(f"[{self.nickname}]->[{user.nickname}]助力成功")
            else:
                print(f"[{self.nickname}]->[{user.nickname}]助力失败：{rjson['err_msg']}")
            sleep(2)

    def run(self):
        print(f"======账号[{self.index}]======")
        self.vipInfo()
        if(self.valid):
            print("\n>>>福利中心")
            self.welfareCenter()
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
    cookies = initEnv()
    users = []
    index = 1
    for cookie in cookies:
        users.append(User(cookie, index))
        index +=1
    for user in users:
        try:
            user.run()
        except Exception as e:
            print("运行异常：", str(e))

    print("\n======福利助力======")
    for user in users:
        user.shareHelp(users)

    print("\n======账号总览======")
    for user in users:
        if(user.valid):
            user.welfareCenter(True)