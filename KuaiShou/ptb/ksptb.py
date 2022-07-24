# -*- encoding: utf-8 -*-

import random
import requests
import sys
import os.path
import json
from time import sleep, time

projectNameCN = "快手普通版"
projectNameEN = "ksptb"
accounts = []
adList = []


COOKIE_NAME = "ksptbCookie"


def initEnv():
    global accounts
    global config
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\{0}.json".format(projectNameEN)
    else:
        filePath += "/{0}.json".format(projectNameEN)

    projectConfig = {}
    if(os.path.isfile(filePath)):
        # 只读打开
        file = open(filePath, "r", encoding="utf-8")
        content = file.read()
        if(content):
            projectConfig = json.loads(content)

        file.close()
        tempCounts = []
        if("accounts" in projectConfig):
            tempCounts = projectConfig['accounts']
        else:
            # 改为覆盖写模式
            file = open(filePath, "w", encoding="utf-8")
            accounts = []
            count = 5
            while(count):
                accounts.append({"name": "", "cookie": ""})
                count -= 1
            projectConfig = {"accounts": accounts,
                             "projectNameCN": projectNameCN}
            file.write(json.dumps(projectConfig, indent=2))
            print("当前项目未配置账号，脚本关闭")
            file.close()
            exit()

        for account in tempCounts:
            # 设置了名称和密钥的账号才算有效
            if(account['name'] and account['cookie']):
                accounts.append(account)

        if(len(accounts) > 0):
            print("账号个数：{0}".format(len(accounts)))
        else:
            print("未发现有效账号，脚本结束")
            exit()

    else:
        # 创建配置文件
        file = open(filePath, "w", encoding="utf-8")
        accounts = []
        count = 5
        while(count):
            accounts.append({"name": "", "cookie": ""})
            count -= 1
        projectConfig = {"accounts": accounts, "projectNameCN": projectNameCN}
        file.write(json.dumps(projectConfig, indent=2))
        print("当前项目未配置账号，脚本关闭")
        file.close()
        exit()


class User:

    def __init__(self,cookie,index=1) -> None:
        self.cookie = cookie
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
            res = requests.get(url, headers=headers)
            return res.json()
        except Exception as e:
            print("GET异常：{1}".format(str(e)))
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
            res = requests.post(url, data=body, headers=headers)
            return res.json()
        except Exception as e:
            print("POST异常：{1}".format(str(e)))
            return None

    # 主页
    def home(self):
        url = "https://encourage.kuaishou.com/rest/wd/encourage/home"
        rjson = self.get(url)
        if(not rjson):
            return
        self.basicInfo = {}
        if(rjson['result'] == 1):
            self.basicInfo['cash'] = rjson['data']['cash']
            self.basicInfo['coin'] = rjson['data']['coin']
            self.valid = True
            print("登录成功：{0}金币\t{1}现金".format(
                rjson['data']['coin'], rjson['data']['cash']))
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
                print("今日金币未签到")
                self.sign(0)
            else:
                print("今日金币已签到")
        else:
            print("获取签到信息失败：{0}".format(rjson['error_msg']))

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
                print("宝箱冷却时间：{0}s".format(
                    rjson['data']['treasureCurrentTaskRemainSeconds']))
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
    #env[COOKIE_NAME] = "kpn=KUAISHOU; kpf=ANDROID_PHONE; c=HUAWEI; ver=10.4; appver=10.4.41.25925; language=zh-cn; countryCode=CN; sys=ANDROID_7.1.2; mod=HUAWEI%28BRQ-AN00%29; net=WIFI; deviceName=HUAWEI%28BRQ-AN00%29; is_background=0; deviceBit=0; oc=HUAWEI; sbh=48; hotfix_ver=; grant_browse_type=AUTHORIZED; userRecoBit=0; socName=HiSilicon+Kirin+820; newOc=HUAWEI; max_memory=256; isp=; kcv=1474; boardPlatform=kirin820; did_tag=3; sw=720; slh=0; rdid=ANDROID_4a4c88b01945cd43; oDid=TEST_ANDROID_FBC46ED4918CA258; country_code=CN; abi=arm64; sh=1280; nbh=96; androidApiLevel=25; browseType=4; ddpi=320; android_os=0; app=0; is_app_prelaunching=1; device_abi=; cl=0; bottom_navigation=false; keyconfig_state=2; ftt=; is_app_prelaunch=0; darkMode=false; totalMemory=7567; iuid=; did_gt=1657440449407; client_key=3c2cd3f3; userId=2920371133; ud=2920371133; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHQumDrQXLHX7PXVUimDJwMIyRl9iSJVrH60uHP2EbVIw26gM29cU1jtVF28xrna9Cx0Sb7z4GWe4vxt3GIKzabSX34uPdOJKMtjsx-K2kRsmabzsQ0AT7Affuv2BMm1vCp_5MMREwW8nDWd1jkaknbIvB9qULt_5l0jiAODbyMvirEaZc71ga93ItkwQJV2ZiKikIPcQQ9nR0jJBBAvaDHGhJmtLHvm4BGCob9TuUwQR1Z_BoiIERMj__ln_VMNI-dJvNQssAl5nNNpgNr_tTB4Lj0QtBhKAUwAQ; token=07d3e257d7b543a19ace423e63941783-2920371133; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAQirP3FrxkT-LLW0mz7eQ28hwyoYDT9PsqId7F2UaAx1xq6gOzXK2A_SZ1m7H3SHHT7uJhgGch8dNR1LBT6ExTXEloAa8qXkkpdFQXkAvd0_MtU02nm5QXBnV8JbI_kj2inQn2Rp4I1JQy3BtvW5EpYUUw_6zYy7tFqxV9nbS5uP6PqdRuGl70lQW9wWPMm642cR-mQdVRb53RuPoTVKT3IaEgduzxS3De8OcL6wm9oIlLYepiIgS1FNgQjNOrfrC48QcXmGAKe31YfVHItKqmnLUeQcKS4oBTAB; didv=1658157873000; did=ANDROID_45890FE4706E577D; egid=DFP099D72C55E19059991AAF33223EAA8CC26FB74B9715E2BAA1D04A1F5DF5F8; sid=93b746ac-0fa3-4767-b8d7-8d121d19a26c; cold_launch_time_ms=1658410031362; __NSWJ=qWu%2BgoB8K0SjrW80A5lv%2BKGFACulLZBMc5%2BF61EUll3864xJ9prSFeM2Iwury71PAAAAAQ%3D%3D"
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