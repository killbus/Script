import json
import os
from time import time
from urllib.parse import urlencode
from Crypto.Cipher import AES
from base64 import b64decode, b64encode

import requests

BLOCK_SIZE = AES.block_size
COOKIE_NAME = "jddjCookie"

class AESCipher:

    def __init__(self):
        self.key = "J@NcRfUjXn2r5u8x"
        self.iv = "t7w!z%C*F-JaNdRg"

    @staticmethod
    def pad(text):
        return text + (BLOCK_SIZE - len(text.encode()) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(text.encode()) % BLOCK_SIZE)

    @staticmethod
    def un_pad(text):
        return text[:-ord(text[len(text) - 1:])]

    # 加密
    def encrypt(self, text):
        text = self.pad(text).encode()
        cipher = AES.new(key=self.key.encode(),
                         mode=AES.MODE_CBC, IV=self.iv.encode())
        encrypted_text = cipher.encrypt(text)
        return b64encode(encrypted_text).decode('utf-8')

    # 解密
    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        cipher = AES.new(key=self.key.encode(),
                         mode=AES.MODE_CBC, IV=self.iv.encode())
        decrypted_text = cipher.decrypt(encrypted_text)
        return self.un_pad(decrypted_text).decode('utf-8')


class User:

    def __init__(self, cookie, index=1) -> None:
        if(not cookie or cookie.find("deviceid_pdj_jd") == -1):
            self.valid = False
        else:
            self.index = index
            self.valid = True
            self.cipher = AESCipher()
            self.cookie = cookie
            self.fruitAssitanceInfo = None
            self.cookieDict = {}
            kvs = cookie.split(";")
            for kv in kvs:
                k_v = kv.strip().split("=")
                if(len(k_v) == 2):
                    self.cookieDict[k_v[0]] = k_v[1]

    # 统一GET 额外header用字典传递
    def __get__(self, url, header=None):
        baseHeader = {
            "User-Agent": "Mozilla/5.0 (Linux; Android; )________appName=jdLocal&platform=android&djAppVersion=8.21.5&apppVersion=8.21.5&isElderEnable=0&isElderBigFont=0________", "Content-Type": "application/x-www-form-urlencoded;",
            "Referer": "https://daojia.jd.com/taroh5/h5dist/",
            "X-Requested-With": "com.jingdong.pdj",
            "Cookie": self.cookie
        }
        if(header):
            baseHeader.update(header)
        try:
            res = requests.get(url, headers=baseHeader)
            return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    # 统一POST 额外header用字典传递
    def __post__(self, url, body='', header=None):
        baseHeader = {
            "User-Agent": "Mozilla/5.0 (Linux; Android; )________appName=jdLocal&platform=android&djAppVersion=8.21.5&apppVersion=8.21.5&isElderEnable=0&isElderBigFont=0________", "Content-Type": "application/x-www-form-urlencoded;",
            "Referer": "https://daojia.jd.com/taroh5/h5dist/",
            "X-Requested-With": "com.jingdong.pdj",
            "Cookie": self.cookie
        }
        if(header):
            baseHeader.update(header)
        try:
            res = requests.post(url, data=body, headers=baseHeader)
            return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def __encrypt__(self, jdrandom, functionId, newDict=None):
        baseDict = {
            "lat": 20.910885,
            "lng": 110.10115,
            "lat_pos": 20.910885,
            "lng_pos": 110.10115,
            "city_id": 1677,
            "channel": "android",
            "platform": "8.11.0",
            "platCode": "h5",
            "appVersion": "8.15.0",
            "appName": "paidaojia",
            "deviceModel": "appmodel",
            "traceId": "{0}{1}".format(self.cookieDict["deviceid_pdj_jd"], jdrandom),
            "deviceToken": self.cookieDict["deviceid_pdj_jd"],
            "deviceId": self.cookieDict["deviceid_pdj_jd"],
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "isNeedDealError": True,
            "body": "{\"channel\":\"qiandao_baibaoxiang\",\"cityId\":\"\",\"wholeVersion\":1,\"ifCic\":0}",
            "signNeedBody": 1,
            "signKeyV1": "16cb0eebc3391fc14d9d8d3a9a270d4503cd26bfc44a3b2e62c9362cabdd4e9f"
        }
        if(newDict):
            baseDict.update(newDict)
        return self.cipher.encrypt(json.dumps(baseDict))

    def __signInMsg__(self):
        jdrandom = int(time())
        functionId = "signin/showSignInMsgNew"
        djencrypt = self.__encrypt__(jdrandom, functionId)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            self.valid = False
            return
        if(rjson['success']):
            result = rjson["result"]
            userInfoResponse = result["userInfoResponse"]
            sevenDaysRewardResponse = result["sevenDaysRewardResponse"]
            self.tomorrowPoints = sevenDaysRewardResponse["tomorrowPoints"]
            if("points" in userInfoResponse):
                print(f"当前鲜豆余额：{userInfoResponse['points']}")
            else:
                print(f"当前鲜豆余额：0")
            print(f"已签到天数：{userInfoResponse['alreadySignInDays']}")
            if(userInfoResponse["hasSign"]):
                self.hasSign = True
                print("今日签到状态：已签到")
            else:
                self.hasSign = False
                print("今日签到状态：未签到")
        else:
            self.valid = False
            print(f"登录失败：{rjson['msg']}")

    def __signIn__(self):
        jdrandom = int(time())
        functionId = "signin/userSigninNew"
        djencrypt = self.__encrypt__(jdrandom, functionId)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson["success"]):
            print(f"签到成功：+{rjson['result']['points']}鲜豆")
            print(f"明日签到奖励：+{self.tomorrowPoints}鲜豆")
        else:
            print(f"签到失败：{rjson['msg']}")

    def __carveJoin__(self):
        jdrandom = int(time())
        functionId = "signin/carveUp/joinCarveUp"
        newDict = {
            "body":'{\"encryptData\":\"FjWCrAcb0JVKDsrPyLDOIsFWzU94xCaXy7MyuNGsJG0B7S29RM+08PGJmDGVrPM2FIpVLmTftPzFXtsxKvWvYDWfDLZmOauXG3V0878dR3PsoiEG8pGIf8Yd2I8rB9nZYsVWg46LVhy45wqtiyoHgw8vZeTeMOD7iI/LGsSrUok=\",\"groupId\":\"217113296000074\",\"activityId\":\"22c8658cb51314a\",\"wcUnionId\":\"oCwKwuGiIKJncuRh0RXInTBiWa6c\",\"formId\":\"\",\"type\":1,\"traceId\":\"2022-07-17T17:51:41.692Z\"}',
            "Method":"GET"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict)
        url = f"https://daojia.jd.com/client?_jdrandom={jdrandom}&functionId={functionId}&{urlencode({'djencrypt':djencrypt})}"
        rjson = self.__get__(url)        
        if(not rjson):
            return
        if(rjson["success"]):
            print("加入组队成功")
        else:
            print(f"加入组队失败：{rjson['msg']}")        

    def __plantBeansGetActivityInfo__(self):
        jdrandom = int(time())
        functionId = "plantBeans/getActivityInfo"
        newDict = {
            "body":"{}",
            "Method":"POST"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict)
        body = urlencode({'djencrypt':djencrypt})
        url = f"https://daojia.jd.com/client?_jdrandom={jdrandom}&functionId={functionId}"
        rjson = self.__post__(url,body=body)        
        if(not rjson):
            self.plantBeansValid = False
            return
        if(rjson["success"]):
            self.plantBeansValid = True
            pre = rjson['result']['pre']
            cur = rjson['result']['cur']
            self.plantBeansInfo = cur
            print(f"当前等级：{cur['level']}")
            print(f"等级进度：{cur['levelProgress']}/{cur['totalProgress']}")
            print(f"水滴余量：{cur['water']}")
            print(f"今日浇水：{cur['dailyWater']}")
            print(f"水滴蓄量：{cur['waterCart']}")
            print("")
            if("buttonId" in pre):
                if(pre['buttonId'] == 1):
                    print(f"可领取上期奖励：{pre['points']}鲜豆")
                    self.__plantBeansReceive__(pre['activityId'])
                else:
                    print(f"已领取上期奖励：{pre['points']}鲜豆")
            else:
                print("上期未参与")
                
        else:
            print(f"获取种豆信息失败：{rjson['msg']}")

    def __plantBeansReceive__(self,activityId):
        jdrandom = int(time())
        functionId = "plantBeans/getPoints"
        newDict = {
            "body":f"{{\"activityId\":\"{activityId}\"}}",
            "Method":"POST"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict)
        body = urlencode({'djencrypt':djencrypt})
        url = f"https://daojia.jd.com/client?_jdrandom={jdrandom}&functionId={functionId}"
        rjson = self.__post__(url,body=body)        
        if(not rjson):
            return
        if(rjson["success"]):
            print("领取上期奖励成功")
        else:
            print(f"领取上期奖励失败：{rjson['msg']}")        

    def __plantBeansGetWater__(self):
        jdrandom = int(time())
        functionId = "plantBeans/getWater"
        newDict = {
            "body":json.dumps({"activityId":self.plantBeansInfo['activityId']}),
            "Method":"POST"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict)
        body = urlencode({'djencrypt':djencrypt})
        url = f"https://daojia.jd.com/client?_jdrandom={jdrandom}&functionId={functionId}"
        rjson = self.__post__(url,body=body)        
        if(not rjson):
            return        
        if(rjson["success"]):
            self.plantBeansInfo['water'] = rjson['result']['water']
            print(f"收集水滴成功：+{rjson['result']['addWater']}")
        else:
            print(f"收集水滴失败：{rjson['msg']}")

    def __plantBeansWater__(self):
        jdrandom = int(time())
        functionId = "plantBeans/watering"
        newDict = {
            "body":json.dumps({"activityId":self.plantBeansInfo['activityId'],"waterAmount":self.plantBeansInfo['water']}),
            "Method":"POST"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict)
        body = urlencode({'djencrypt':djencrypt})
        url = f"https://daojia.jd.com/client?_jdrandom={jdrandom}&functionId={functionId}"
        rjson = self.__post__(url,body=body)        
        if(not rjson):
            return  
        if(rjson['success']):
            result = rjson['result']
            print(f"浇水成功：{result['levelProgress']}/{result['totalProgress']}")    
        else:
            print(f"浇水失败：{rjson['msg']}")

    def __fruitInit__(self):
        jdrandom = int(time())
        functionId = "fruit/initFruit"
        newDict = {
            "body":"{\"cityId\":1677,\"longitude\":110.10147,\"latitude\":20.910877}",
            "Method":"POST"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict)
        body = urlencode({'djencrypt':djencrypt})
        url = f"https://daojia.jd.com/client?_jdrandom={jdrandom}&functionId={functionId}"
        rjson = self.__post__(url,body=body)        
        if(not rjson):
            self.fruitValid = False
            return
        if(rjson["success"]):
            self.fruitValid = True
            self.fruitInfo = {}
            self.fruitInfo['waterStorage'] = 0
            self.fruitInfo['userWaterBalance'] =rjson['result']['userResponse']['waterBalance']
            activityInfoResponse = rjson['result']['activityInfoResponse']
            print(f"果树品种：{activityInfoResponse['fruitName']}")
            print(f"剩余进度：{activityInfoResponse['curStageLeftProcess']}/{activityInfoResponse['curStageTotalProcess']}")
            print(f"水滴余量：{self.fruitInfo['userWaterBalance']}")
        else:
            self.fruitValid = False
            print(f"获取果树信息失败：{rjson['msg']}")       

    def __fruitBottleInfo__(self):
        jdrandom = int(time())
        functionId = "fruit/getWaterBottleInfo"
        djencrypt = self.__encrypt__(jdrandom, functionId)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson['success']):
            if(rjson['result']['receiveStatus'] == 0):
                self.__fruitBottleReceive__()
            else:
                print("水壶水滴已领取")
        else:
            print(f"获取果树水壶状态失败：{rjson['msg']}")

    def __fruitBottleReceive__(self):
        jdrandom = int(time())
        functionId = "fruit/receiveWaterBottle"
        djencrypt = self.__encrypt__(jdrandom, functionId)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson['success']):
            print("领取水壶水滴成功")
        else:
            print(f"领取水壶水滴失败：{rjson['msg']}")

    def __fruitWheelInfo__(self):
        jdrandom = int(time())
        functionId = "fruit/getWaterWheelInfo"
        djencrypt = self.__encrypt__(jdrandom, functionId)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson['success']):
            self.fruitInfo.update(rjson['result'])
            print(f"水车蓄量：{self.fruitInfo['waterStorage']}")
        else:
            print(f"获取果树水车蓄量失败：{rjson['msg']}")

    def __fruitWheelReceive__(self):
        jdrandom = int(time())
        functionId = "fruit/collectWater"
        djencrypt = self.__encrypt__(jdrandom, functionId)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson['success']):
            self.fruitInfo.update(rjson['result'])
            print("收集水车水滴成功")
        else:
            print(f"收集水滴失败：{rjson['msg']}")        

    def __fruitRedPackInfo__(self):
        jdrandom = int(time())
        functionId = "fruit/getWaterRedPackInfo"
        djencrypt = self.__encrypt__(jdrandom, functionId)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson['success']):
            result = rjson['result']
            if(result['status'] == 2):
                print(f"进度红包可领取")
                self.__fruitRedPackReceive__()
            elif("curProgress" in result):
                print(f"进度红包未满足领取条件：{result['curProgress']}/{result['targetProgress']}")
        else:
            print(f"获取果树进度红包信息失败：{rjson['msg']}")        

    def __fruitRedPackReceive__(self):
        jdrandom = int(time())
        functionId = "fruit/receiveWaterRedPack"
        djencrypt = self.__encrypt__(jdrandom, functionId)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson['success']):
            print(f"领取进度红包成功：+{rjson['result']['reward']}水滴")
        else:
            print(f"获取进度红包失败：{rjson['msg']}")

    def __fruitWatering__(self):
        jdrandom = int(time())
        functionId = "fruit/watering"
        newDict = {
            "body":f'{{\"waterTime\":{self.fruitInfo["userWaterBalance"]/10}}}',
            "Method":"POST"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict)
        body = urlencode({'djencrypt':djencrypt})
        url = f"https://daojia.jd.com/client?_jdrandom={jdrandom}&functionId={functionId}"
        rjson = self.__post__(url,body=body)        
        if(not rjson):
            return  
        if(rjson['success']):
            activityInfoResponse = rjson['result']['activityInfoResponse']
            print(f"浇水成功：{activityInfoResponse['curStageLeftProcess']}/{activityInfoResponse['curStageTotalProcess']}")    
        else:
            print(f"浇水失败：{rjson['msg']}")        

    def fruitAssitance(self,users):
        print("\n>>>>>果园助力")
        for user in users:
            if(not user.fruitAssitanceInfo):
                continue
            jdrandom = int(time())
            functionId = "task/finished"
            newDict = {
                "body":f"{{\"modelId\":\"M10007\",\"taskType\":1201,\"taskId\":\"23eee1c043c01bc\",\"plateCode\":5,\"assistTargetPin\":\"{user.cookieDict['PDJ_H5_PIN']}\",\"uniqueId\":\"{user.fruitAssitanceInfo['uniqueId']}\"}}"
            }
            djencrypt = self.__encrypt__(jdrandom, functionId,newDict=newDict)
            urlDict = {
                "_jdrandom": jdrandom,
                "functionId": functionId,
                "djencrypt": djencrypt
            }
            url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
            rjson = self.__get__(url=url)
            if(not rjson):
                return
            if(rjson['success']):
                print(f"{self.cookieDict['PDJ_H5_PIN']}->{user.cookieDict['PDJ_H5_PIN']}助力成功")
            else:
                print(f"{self.cookieDict['PDJ_H5_PIN']}->{user.cookieDict['PDJ_H5_PIN']}果园失败：{rjson['msg']}")        

    def __taskList__(self,modelId):
        jdrandom = int(time())
        functionId = "task/list"
        newDict = {
            "body":f"{{\"modelId\":\"{modelId}\",\"plateCode\":2}}"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict=newDict)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson['success']):
            taskInfoList = rjson['result']['taskInfoList']
            for task in taskInfoList:
                #果园助力任务
                if(task['modelId'] == "M10007" and task['taskId'] == "23eee1c043c01bc"):
                    if("fissionUserInfoList" not in task or len(task['fissionUserInfoList'])<5):
                        self.fruitAssitanceInfo = task
                
                if(task['status'] == 3):
                    print(f"{task['taskName']} --已完成")
                elif(task['status'] == 2):
                    print(f"{task['taskName']} --待领取奖励")
                    self.__taskPrize__(task)
                else:
                    print(f"{task['taskName']} --未完成")
                    if(task['unreceiveTaskJumpFlag']):
                        self.__taskFinish__(task)
                    else:
                        self.__taskReceive__(task)
        else:
            print(f"获取任务失败：{rjson['msg']}")        

    def __taskReceive__(self,task):
        jdrandom = int(time())
        functionId = "task/received"
        newDict = {
            "body":f"{{\"modelId\":\"{task['modelId']}\",\"taskId\":\"{task['taskId']}\",\"taskType\":{task['taskType']},\"plateCode\":2}}"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict=newDict)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson['success']):
            print(f"领取任务[{task['taskName']}]成功")
            self.__taskFinish__(task)
        else:
            print(f"领取任务[{task['taskName']}]失败：{rjson['msg']}")        

    def __taskFinish__(self,task):
        jdrandom = int(time())
        functionId = "task/finished"
        newDict = {
            "body":f"{{\"modelId\":\"{task['modelId']}\",\"taskId\":\"{task['taskId']}\",\"taskType\":{task['taskType']},\"plateCode\":2}}"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict=newDict)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson['success']):
            print(f"完成任务[{task['taskName']}]成功")
            self.__taskPrize__(task)
        else:
            print(f"完成任务[{task['taskName']}]失败：{rjson['msg']}")

    def __taskPrize__(self,task):
        jdrandom = int(time())
        functionId = "task/sendPrize"
        newDict = {
            "body":f"{{\"modelId\":\"{task['modelId']}\",\"taskId\":\"{task['taskId']}\",\"taskType\":{task['taskType']},\"plateCode\":2}}"
        }
        djencrypt = self.__encrypt__(jdrandom, functionId,newDict=newDict)
        urlDict = {
            "_jdrandom": jdrandom,
            "functionId": functionId,
            "djencrypt": djencrypt
        }
        url = f"https://daojia.jd.com/client?{urlencode(urlDict)}"
        rjson = self.__get__(url=url)
        if(not rjson):
            return
        if(rjson['success']):
            print(f"领取任务[{task['taskName']}]奖励成功")
        else:
            print(f"领取任务[{task['taskName']}]奖励失败：{rjson['msg']}")        

    def run(self):
        print(f"{8*'#'}账号[{self.index}]{8*'#'}")
        self.__signInMsg__()
        if(not self.valid):
            return
        if(not self.hasSign):
            print("")
            self.__signIn__()

        print("\n>>>>>鲜豆任务")
        self.__taskList__("M10001")
        
        print("\n>>>>>未知模块任务M10006")
        self.__taskList__("M10006")

        print("\n>>>>>瓜分鲜豆")
        self.__plantBeansGetActivityInfo__()
        if(self.plantBeansValid):
            if(self.plantBeansInfo["waterCart"]):
                print("")
                self.__plantBeansGetWater__()
            if(self.plantBeansInfo['water']>=100):
                print("")
                self.__plantBeansWater__()
            print("")
            self.__taskList__("M10003")

        print("\n>>>>>免费水果")
        self.__fruitInit__()
        if(self.fruitValid):
            self.__fruitWheelInfo__()
            if(self.fruitInfo['waterStorage'] >=1):
                print("")
                self.__fruitWheelReceive__()
            print("")
            self.__fruitBottleInfo__() 
            print("")
            self.__fruitRedPackInfo__()
            print("")
            self.__taskList__("M10007")

            if(self.fruitInfo['userWaterBalance']>=10):
                print("")
                self.__fruitWatering__()

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
        users.append(User(cookie,index))
        index +=1
    for user in users:
        user.run()
    for user in users:
        user.fruitAssitance(users)
