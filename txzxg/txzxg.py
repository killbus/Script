from email import header
import random
import sys
import os.path
import json
from time import sleep, time
import requests

projectNameCN = "腾讯自选股"
projectNameEN = "txzxg"
accounts = []


def initEnv():
    global accounts
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\{0}.json".format(projectNameEN)
    else:
        filePath += "/{0}.json".format(projectNameEN)

    projectConfig = {}
    # 配置文件存在
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
                accounts.append({"name": "", "openid": "","fskey":"","wzq_qlskey":"","wzq_qluin":""})
                count -= 1
            projectConfig = {
                "accounts": accounts, "projectNameCN": projectNameCN}
            file.write(json.dumps(projectConfig, indent=2))
            print("当前项目未配置账号，脚本关闭")
            file.close()
            exit()

        for account in tempCounts:
            # app或微信端设置参数即可
            if((account['wzq_qlskey'] and account['wzq_qluin']) or (account['openid'] and account['fskey'])):
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
            accounts.append({"name": "", "openid": "","fskey":"","wzq_qlskey":"","wzq_qluin":""})
            count -= 1
        projectConfig = {
            "accounts": accounts, "projectNameCN": projectNameCN}
        file.write(json.dumps(projectConfig, indent=2))
        print("当前项目未配置账号，脚本关闭")
        file.close()
        exit()


# 统一GET 额外header用字典传递
def get(account, url, header=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
        "Cookie": account['cookie']
    }
    if(header):
        for k, v in header.items():
            headers[k] = v
    # 捕获异常
    try:
        res = requests.get(url, headers=headers)
        return res.json()
    except Exception as e:
        print("用户[{0}]GET异常：{1}".format(account['name'], str(e)))
        return None

# 统一POST 额外header用字典传递
def post(account, url, body='', header=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;",
    }
    if(header):
        for k, v in header.items():
            headers[k] = v
    # 捕获异常
    try:
        res = requests.post(url, data=body, headers=headers)
        return res.json()
    except Exception as e:
        print("用户[{0}]POST异常：{1}".format(account['name'], str(e)))
        return None


def getUserName(account):
    url = "https://proxy.finance.qq.com/group/newstockgroup/RssService/getSightByUser2?g_openid={0}&openid={0}&fskey={1}".format(account['openid'],account['fskey'])
    body = "g_openid={0}&search_openid={0}".format(account['openid'])
    header = {"content-type":"application/x-www-from-urlencoded"}
    rjson = post(account,url)
    print(rjson)

if __name__ == "__main__":
    initEnv()
    getUserName(accounts[0])