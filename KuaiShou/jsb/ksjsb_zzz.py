# -*- encoding: utf-8 -*-
'''
@项目名称：   ksjsb_zzz.py
@项目地址：   
@创建时间：   2022/05/15 16:34:24
@创作者  ：   wsfsp4 
@版本号  ：   1.0
@功能描述：   快手极速版周周赚助力
@特别提醒：   轮流助力,每个账号都会被助力到,一个账号一周可被助力7次;配置文件中设置name和cookie字段即可;新账号请添加到末尾，否则助力顺序会被打乱导致重复无效助力
@更新时间：   
@更新内容：   
'''

import datetime
import sys
import os.path
import json
from time import sleep
import requests

projectNameCN = "快手极速版周周赚"
projectNameEN = "ksjsb_zzz"
accounts = []
adList = []
config = {} 

# 初始化配置
def initEnv():
    global accounts
    global config
    filePath = sys.path[0]
    if(filePath.find("\\") != -1):
        filePath += "\\{0}.json".format(projectNameEN)
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

        # 账号配置
        tempAccounts = []
        if('accounts' in projectConfig):
            tempAccounts = projectConfig['accounts']
        else:
            # 改为覆盖写模式
            file = open(filePath, "w", encoding="utf-8")
            accounts = []
            count = 5
            while(count):
                accounts.append({"name": "", "cookie": ""})
                count -= 1
            projectConfig = {
                "accounts": accounts, "projectNameCN": projectNameCN, "config": {"log": False}}
            file.write(json.dumps(projectConfig, indent=2))
            print("当前项目未配置账号，脚本关闭")
            file.close()
            exit()
        position = 0
        for account in tempAccounts:
            # 设置了名称和密钥的账号才算有效
            if(account['name'] and account['cookie']):
                # 用户序号，用于运行过程修改用户信息
                account['index'] = position
                position += 1
                accounts.append(account)
        if(len(accounts) > 0):
            print("账号个数：{0}".format(len(accounts)))
        else:
            print("未发现有效账号，脚本结束")
            exit()
        # 其他配置
        if("config" in projectConfig):
            config = projectConfig['config']

    else:
        # 创建配置文件
        file = open(filePath, "w", encoding="utf-8")
        accounts = []
        count = 5
        while(count):
            accounts.append({"name": "", "cookie": ""})
            count -= 1
        projectConfig = {
            "accounts": accounts, "projectNameCN": projectNameCN, "config": {}}
        file.write(json.dumps(projectConfig, indent=2))
        print("当前项目未配置账号，脚本关闭")
        file.close()
        exit()


# 统一GET 额外header用字典传递
def get(account, url, header=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10);",
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
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;)",
        "cookie": account['cookie']
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


# 获取用户基本信息
def getBasicInfo(account):
    url = "https://nebula.kuaishou.com/rest/n/nebula/activity/earn/overview/basicInfo"
    rjson = get(account, url)
    if(not rjson):
        return {"normal": False}

    if(rjson['result'] == 1):
        data = rjson['data']
        print("用户[{0}]：{1}金币\t{2}元\t待审核{3}元".format(data['userData']['nickname'],
              data['totalCoin'], data['totalCash'], float(data['allCash'])-float(data['totalCash'])))
        return {"normal": True, "nickname": data['userData']['nickname'], 'avatar': data['userData']['avatar'], "totalCoin": data['totalCoin'], 'totalCash': data['totalCash'], 'allCash': data['allCash']}
    else:
        print("用户[{0}]登录失败".format(account['name']))
        return {"normal": False}


# 周周赚-获取助力码
def getAssistCode(account):
    url = "https://nebula.kuaishou.com/rest/zt/encourage/assistance/detail?assistanceMetaId=2"
    rjson = get(account, url)
    if(not rjson):
        return
    if(rjson['result'] == 1):
        print("用户[{0}]获取周周赚助力码成功：{1}".format(account['basicInfo']
              ['nickname'], rjson['assistanceInfo']['assistanceId']))
        account['basicInfo']['assistanceId'] = rjson['assistanceInfo']['assistanceId']
    else:
        print("用户[{0}]获取周周赚助力码失败：{1}".format(
            account['basicInfo']['nickname'], rjson['error_msg']))


# 周周赚-助力
def assist(fromAccount, toAccount):
    url = "https://nebula.kuaishou.com/rest/zt/encourage/assistance/friendAssist"
    if(not toAccount['basicInfo']['assistanceId']):
        print("用户[{0}]助力码不存在，助力失败".format(toAccount['basicInfo']['nickname']))
        return
    body = {"assistanceId": toAccount['basicInfo']['assistanceId']}
    header = {"Content-Type": "application/json"}
    rjson = post(fromAccount, url, header=header, body=json.dumps(body))
    if(not rjson):
        return
    if("msg" in rjson):
        print("[{0}]-->[{1}]：{2}".format(fromAccount['basicInfo']
              ['nickname'], toAccount['basicInfo']['nickname'], rjson['msg']))
    else:
        print("[{0}]-->[{1}]：{2}".format(fromAccount['basicInfo']['nickname'],
              toAccount['basicInfo']['nickname'], rjson['error_msg']))


# 周周赚-助力详细
def assistDetail(account):
    url = "https://nebula.kuaishou.com/rest/zt/encourage/assistance/detail?assistanceMetaId=2"
    rjson = get(account, url)
    if(not rjson):
        return
    if(not rjson or "assistanceInfo" not in rjson):
        return
    print("用户[{0}]受助次数：{1}".format(account['basicInfo']
          ['nickname'], rjson['assistanceInfo']['assistedCount']))
    print("用户[{0}]积累金币：{1}".format(account['basicInfo']['nickname'],
          rjson['assistanceInfo']['accumulatedAmount']))
    print("用户[{0}]兑换金币：{1}".format(account['basicInfo']['nickname'],
          rjson['assistanceInfo']['accumulatedWithdraw']))
    stageAmount = rjson['assistanceInfo']['withdrawRule']['stageAmount']
    for amount in stageAmount:
        if(amount > rjson['assistanceInfo']['accumulatedWithdraw']):
            print("用户[{0}]当前阶段：{1}".format(
                account['basicInfo']['nickname'], amount))
            break


if __name__ == "__main__":
    initEnv()

    print("\n\n{0}登录{0}".format(9*'='))
    for account in accounts:
        basicInfo = getBasicInfo(account)
        account['basicInfo'] = basicInfo

    print("\n\n{0}获取助力码{0}".format(9*'='))
    for account in accounts:
        if(not account['basicInfo']["normal"]):
            continue
        getAssistCode(account)
    
    #剔除无效账号
    temps = []
    for account in accounts:
        if(account['basicInfo']['normal'] and "assistanceId" in account['basicInfo']):
            temps.append(account)
    accounts = temps

    print("\n\n{0}助力{0}".format(9*'='))
    len = len(accounts)
    if(len<2):
        print("账号个数少于2，脚本退出")
        exit()
    #偏移量
    div = 0
    if(len <=7):
        div = datetime.datetime.now().day%(len-1)+1 #生成1-(len-1)的偏移量
    else:
        div = datetime.datetime.now().day%7+2 #生成1-7的偏移量

    for index in range(len):
        assist(accounts[index],accounts[(index+div)%len])
        sleep(10)

    print("\n\n{0}助力统计{0}".format(9*'='))
    for account in accounts:
         assistDetail(account)
         print("\n")