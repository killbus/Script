# -*- encoding: utf-8 -*-

import requests
import os.path
import json
from time import sleep

COOKIE_NAME = "ksptbCookie"

requests.packages.urllib3.disable_warnings()

class User:

    def __init__(self,cookie,index=1) -> None:
        self.cookie = cookie
        self.valid = True
        self.index = index

    # 统一GET 额外header用字典传递
    def get(self, url, header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; VCE-AL00 Build/HUAWEIVCE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.469 (rel;r) Mobile Safari/537.36 Yoda/2.8.1-rc3 Kwai/10.3.20.24977",
            "cookie": self.cookie
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.get(url, headers=headers,verify=False)
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    # 统一POST 额外header用字典传递
    def post(self, url, body='', header=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; VCE-AL00 Build/HUAWEIVCE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.469 (rel;r) Mobile Safari/537.36 Yoda/2.8.1-rc3 Kwai/10.3.20.24977",
            "cookie": self.cookie
        }
        if(header):
            headers.update(header)
        # 捕获异常
        try:
            res = requests.post(url, data=body, headers=headers,verify=False)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    # 主页
    def home(self):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/home"
        rjson = self.get(url)
        if(not rjson):
            self.valid = False
            return
        self.basicInfo = {}
        if(rjson['result'] == 1):
            self.valid = True
            self.basicInfo['cash'] = rjson['data']['cash']
            self.basicInfo['coin'] = rjson['data']['coin']
            print(f"金币余额：{rjson['data']['coin']}")
            print(f"现金余额：{rjson['data']['cash']}¥")
        else:
            self.valid = False
            print("登录失败：{0}".format(rjson['error_msg']))

    # 签到信息
    def signInfo(self):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/signIn/info"
        rjson = self.get(url)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            # 普通金币签到
            if("tasks" in rjson['data'] and not rjson['data']['todaySignInCompleted']):
                print("金币签到：未签到")
                self.sign(0)
            else:
                print("金币签到：已签到")
        else:
            print("获取签到信息失败：{0}".format(rjson['error_msg']))

    #签到
    def sign(self, id):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/signIn/report"
        body = {"signInBizId": id}
        header = {"content-type": "application/json"}
        rjson = self.post(url, body=json.dumps(body), header=header)
        if(not rjson):
            return
        if(rjson['result'] == 1):
            print("今日金币签到成功")
        else:
            print("今日金币签到失败：{0}".format(rjson['error_msg']))

    # 获取宝箱信息 如果可开启则开启 开启宝箱后还需查询一次宝箱信息来激活宝箱
    def getBoxInfo(self):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/treasureBox/info"
        rjson = self.get(url)
        if(not rjson or not rjson['data']):
            return
        if(rjson['result'] == 1):
            print(f"宝箱总额：{rjson['data']['treasureRewardAmountEveryDay']}")
            status = rjson['data']['status']
            # status 2领取中 3冷却完成 4次数已完
            if(status == 4):
                print("宝箱冷却时间：开启次数已满，明日再来!")
            elif(status == 3):
                print("宝箱冷却时间：{0}s".format(rjson['data']['treasureCurrentTaskRemainSeconds']))
                self.openBox(rjson['data']['token'])
                sleep(0.1)
                # 激活宝箱
                self.getBoxInfo()
            elif(status == 2):
                print(f"宝箱冷却时间：{rjson['data']['treasureCurrentTaskRemainSeconds']}s")
        else:
            print("获取宝箱信息失败：{0}".format(rjson['error_msg']))

    # 开启宝箱
    def openBox(self, token):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/treasureBox/report"
        body = {"taskToken": token}
        rjson = self.post(url, body=json.dumps(body))
        if(not rjson):
            return
        if(rjson['result'] == 1):
            print("开启宝箱成功：获得{0}金币".format(rjson['data']['rewardCount']))
        else:
            print("开启宝箱失败：{0}".format(rjson['error_msg']))

    def run(self):
        print(f"=====账号[{self.index}]=====")
        self.home()
        if(self.valid):
            self.signInfo()
            self.getBoxInfo()
            print("")

def initEnv():
    env = os.environ
    env[COOKIE_NAME] = "kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=2572784925; did=ANDROID_066bc9bcc33c8a9d; c=HUAWEI_KWAI; ver=10.3; appver=10.3.40.25268; language=zh-cn; countryCode=CN; sys=ANDROID_10; mod=HUAWEI%28CDY-AN00%29; net=WIFI; deviceName=HUAWEI%28CDY-AN00%29; isp=CMCC; ud=2572784925; did_tag=4; egid=DFPC45267EA7DC6FF2C949E5C0ABE88B20B9BE2CDC4039B568FD9A6A3D03E3FD; thermal=10000; kcv=1458; app=0; bottom_navigation=false; oDid=TEST_ANDROID_066ae88cc33c8a9d; android_os=1; boardPlatform=kirin820; androidApiLevel=29; newOc=HUAWEI; slh=0; country_code=cn; nbh=80; hotfix_ver=; did_gt=1651414698121; keyconfig_state=2; max_memory=384; sid=f552c23c-7690-4088-8914-7fb0c970347d; cold_launch_time_ms=1652015341184; oc=HUAWEI_KWAI; sh=1600; ddpi=320; deviceBit=0; browseType=4; power_mode=0; socName=HiSilicon+Kirin+820; is_background=0; sw=720; ftt=; is_app_prelaunch=0; abi=arm64; userRecoBit=0; device_abi=arm64; totalMemory=7567; grant_browse_type=AUTHORIZED; is_app_prelaunching=1; iuid=; rdid=ANDROID_4c59d1a1745f2975; sbh=72; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSsAEOysMrTlHLm114NIK8xykeHiZ3KXyhtYFM83LxlG4zb7l3xstfVLojZncT6ijdoX8p4ZDhEy6idH_FTmNXOLLerXdZMTViB_GZ-JpHqRs4bjjbkwxOX1ZQB6OOAdYjG_i5o4ntYs0s6zPMVNCPhOf54BuMcKfOHtloSxtjBlnffPzg5EVV4fP3Yw6xqJIkNfR3_slVph3dXZr2TYt3mIL04NmJPYP00pp_0qRro3YyMRoSO10xFXRwSIqcekHg3JqdJpRXIiBRNL-ZqV8Wdkx17AX9vT3QxT53RRJMIma5d-lqA70A1igFMAE; token=e38d110a460e42f190c1fd6e2f335a77-2572784925; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAdzBnN6yBX8ddVOKF437AOWARUGQ23kEjiwqK6ksFhKYBpt87M4pAO9YrwtTvjy2s6uL428rNrwiU5Q5QDbtBozKVmlksgEazLSlIcZu83I9JOvmKhRsUwlLvOkE5wRkUbBcOHRloLwqGcviqHSQE-pB0jxmPPK4lf31oFZ0lc_DBVvSLGTVlX87-MdvsCyQ_Kl8CbgpISmvm9B3CqaMwd8aEi0FTenUzzyakcPnzsVR98aTkSIgpYe9r5FrLlUDsO-_SLmAmoNns_GnT_f_uPhpKQJHLXooBTAB; cl=0; __NSWJ=CIN10AgGSrueIs0V7jySHXv8Km5OHLiqiMChVG8Vo%2Fltw8QohWals22JNWfpM6NgAAAABA%3D%3D"
    if(COOKIE_NAME in env):
        cookies = env[COOKIE_NAME]
        if(cookies.find("&")):
            return cookies.split("&")
    return []


if __name__ == "__main__":
    users = []
    cookies = initEnv()
    index = 1
    for cookie in cookies:
        users.append(User(cookie,index))
        index +=1
    for user in users:
        user.run()