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

    def __init__(self, cookie, index=1) -> None:
        self.cookie = cookie
        self.valid = True
        self.index = index

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
    env[COOKIE_NAME] = "appid=wxca942bbff22e0e51; app_ver=8.6.25.25668; app_ver_all=8.6.25.25668; qimei36=f9c43204a22b2de027f7097871efddf2d3c8; vuserid=169689331; vusession=V2YzYFrdCfKUEFm47GKZFg..; video_omgid=3f7f04aa47dfc931a02e9a8b7115169cc8700010115b03; main_login=wx; vdevice_qimei36=f9c43204a22b2de027f7097871efddf2d3c8; video_platform=5; openid=e54b36882d6a8e5bad5f048af800;"
    env[COOKIE_NAME] += "&"+"video_omgid=3e3fbbacf7dfcf49f2d9528ee1bdc72938bf001021751a;guid=4b7dd462f4a411ec89cd6c92bf48bcb2;vuserid=2593638306;usid=1656184829655444;us_stamp=1656184829655;ussn=1656174691964003;vusession=2h_LPDU7ehvHxSFy49mxwA.N;video_platform=3;video_appid=1000005;vdevice_qimei36=bfd24e458b90636deeadbadf10001231490f;vcuid=;vqq_appid=101795054;vqq_openid=F0B53ABA4341CA38D7A75B44E12DE17F;vqq_access_token=F0F96B87A4D3BA94651F7690E4DDD6E7;vqq_vuserid=2593638306;vqq_vusession=2h_LPDU7ehvHxSFy49mxwA.N;main_login=qq;plat_bucketid=1001;teenGuardSessionCode=142BCFE26B01788857559A3774BF30CD8EC77C6987F2D58AE232F401832C9C3A1EDEF216C24EFA1915642898640E3E8FC57FCF492C20F8C17D8FA1F0ECD6FF2FD64BCC095E8534E5A1E02E0476F42745325DD3F41CE4271EB8F4F63045BF4ADB47EA9BBEF065487842BA1539;recommend_switch_value=1;call_type=1;recommend_setting_code=31;ip=223.104.72.140;isDarkMode=0;ptag=cygn;video_bucketid=4;avatar=https%3A%2F%2Ftvpic.gtimg.cn%2Fhead%2F9555e017430827def8f2278228c4f27eb643dd219560b36be2a454ecc5ba32aeb57c72c7%2F259;nickname=%E5%A6%82%E9%A3%8E;app_ver_all=8.6.15.26745;deviceName=P40;webCore=sys;systemVersion=7.1.2;omgid=3e3fbbacf7dfcf49f2d9528ee1bdc72938bf001021751a;omgbizid=7bd463578b893f47a1e9626b383b9137f2a1003021751a;hasNotchInScreen=0;screenWidth=360;screenHeight=640;manufacturer=HUAWEI;qimei36=bfd24e458b90636deeadbadf10001231490f;turing_ticket=0101A7BECCA41C30479C9E34C9F3D439ECDC3F2F2F266EDE1478AED26BEA58526056BCEECB2037D31B29D043;qua=QQLiveBrowser_8.6.15.26745_123;platform=Android;vip_status=0;ctime=1656184964941;zdtime=1656184963748;vversion_name=8.6.15;app_ver=8.6.15.26745"
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