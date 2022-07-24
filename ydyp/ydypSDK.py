#!/usr/bin/python
# -*-coding:utf-8 -*-

import hashlib
import sys
from time import sleep
import requests
import xmltodict
import requests


class SDK:
    def __init__(self, account) -> None:
        self.account = account

    def __get__(self, url, header=None, isXml=True, allow_redirects=True, onlyHeader=False):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; BRQ-AN00 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 MCloudApp/9.0.1",
                       "Authorization": self.account['authorization']}
            if(header):
                headers.update(header)
            res = requests.get(url, headers=headers,
                               allow_redirects=allow_redirects)
            res.encoding = "utf-8"
            if(onlyHeader):
                return res.headers
            if(isXml):
                return xmltodict.parse(res.text, encoding="utf-8")
            else:
                return res.json()
        except Exception as e:
            print("GET异常：{0}".format(str(e)))
            return None

    def __post__(self, url, data=None, file=None, header=None, isXml=True):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; BRQ-AN00 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 MCloudApp/9.0.1",
                       "Authorization": self.account['authorization']}
            if(header):
                headers.update(header)
            res = requests.post(url, headers=headers, data=data, files=file)
            res.encoding = "utf-8"
            if(isXml):
                return xmltodict.parse(res.text, encoding="utf-8")
            else:
                return res.json()
        except Exception as e:
            print("POST异常：{0}".format(str(e)))
            return None

    def __MD5__(self, s):
        hl = hashlib.md5()
        hl.update(s.encode(encoding='utf8'))
        md5 = hl.hexdigest()
        return str(md5).upper()

    def __getCurrentPath__(self):
        filePath = sys.path[0]
        if(filePath.find("\\") != -1):
            return filePath + "\\"
        else:
            return filePath + "/"

    def buildUpInfoBody(self, fName, fSize, catalogID):
        fDigest = self.__MD5__(fName)
        body = f'''
            <pcUploadFileRequest>
            <ownerMSISDN>{self.account['phone']}</ownerMSISDN>
            <fileCount>1</fileCount>
            <totalSize>{fSize}</totalSize>
            <uploadContentList length="1">
                <uploadContentInfo>
                    <comlexFlag>0</comlexFlag>
                    <contentDesc><![CDATA[]]></contentDesc>
                    <contentName><![CDATA[{fName}]]></contentName>
                    <contentSize>{fSize}</contentSize>
                    <contentTAGList></contentTAGList>
                    <digest>{fDigest}</digest>
                    <exif>
                        <createTime>20220628170733</createTime>
                    </exif>
                    <fileEtag>0</fileEtag>
                    <fileVersion>0</fileVersion>
                    <updateContentID></updateContentID>
                </uploadContentInfo>
            </uploadContentList>
            <newCatalogName></newCatalogName>
            <parentCatalogID>{catalogID}</parentCatalogID>
            <operation>0</operation>
            <path></path>
            <manualRename>2</manualRename>
            <autoCreatePath length="0"/>
            <tagID></tagID>
            <tagType></tagType>
            </pcUploadFileRequest>        
        '''
        return body

    def buildShareBody(self, contentID):
        body = f'''
            <getOutLinkV3>
            <getOutLinkReq>
                <account>{self.account['phone']}</account>
                <caIDLst length="0"/>
                <coIDLst length="1">
                    <item>{contentID}</item>
                </coIDLst>
                <dedicatedName><![CDATA[]]></dedicatedName>
                <desc><![CDATA[]]></desc>
                <encrypt>1</encrypt>
                <isUnlimitedTimes>0</isUnlimitedTimes>
                <linkType>0</linkType>
                <period>0</period>
                <periodUnit>0</periodUnit>
                <pubType>1</pubType>
                <subLinkType>0</subLinkType>
                <viewerLst length="1">
                    <item></item>
                </viewerLst>
            </getOutLinkReq>
            </getOutLinkV3>
        '''
        return body

    def buildCatalogBody(self, catalogID):
        body = f'''
            <getDisk>
            <catalogID>{catalogID}</catalogID>
            <catalogSortType>0</catalogSortType>
            <catalogType>-1</catalogType>
            <channelList></channelList>
            <contentSortType>0</contentSortType>
            <contentType>0</contentType>
            <endNumber>0</endNumber>
            <filterType>0</filterType>
            <MSISDN>{self.account['phone']}</MSISDN>
            <sortDirection>1</sortDirection>
            <startNumber>-1</startNumber>
            </getDisk>
        '''
        return body

    def getUpInfo(self):
        url = "https://ose.caiyun.feixin.10086.cn/richlifeApp/devapp/IUploadAndDownload"
        fName = "test.png"
        fSize = 1024
        catalogID = "00019700101000000001"
        body = self.buildUpInfoBody(fName, fSize, catalogID)
        headers = {
            "x-huawei-channelSrc":"10000023",
        }
        rjson = self.__post__(url, data=body,header=headers)
        if(not rjson):
            return None
        if(rjson['result']['@resultCode'] == "0"):
            if("redirectionUrl" in rjson['result']['uploadResult']):
                redirectionUrl = rjson['result']['uploadResult']['redirectionUrl']
                uploadTaskID = rjson['result']['uploadResult']['uploadTaskID']
                print("获取文件上传链接成功")
                return (redirectionUrl, uploadTaskID, fName)
            else:
                print("云盘上已存在此资源，无须上传")
                return None
        else:
            print(f"获取文件上传信息失败：{rjson}")
            return None

    def upFile(self, redirectionUrl, uploadtaskID, fName):
        headers = {
            "UploadtaskID": uploadtaskID,
            "contentSize": f"{1024}",
            "Range": f"bytes=0-{1023}",
            "rangeType": "0",
            "Content-Type": f"*/*;name={fName}"
        }
        upJson = self.__post__(
            redirectionUrl, data=10*redirectionUrl, header=headers)
        if(not upJson):
            print("上传文件失败")
        if(upJson['result']['resultCode'] == "0"):
            print("上传文件成功")
        else:
            print("上传文件失败")

    def upFileEnter(self):
        redirectionUrl, uploadtaskID, fName = self.getUpInfo()
        if(redirectionUrl and uploadtaskID):
            self.upFile(redirectionUrl, uploadtaskID, fName)

    def getCatalog(self, catalogID="00019700101000000001"):
        url = "https://ose.caiyun.feixin.10086.cn/richlifeApp/devapp/ICatalog"
        body = self.buildCatalogBody(catalogID)
        rjson = self.__post__(url, data=body)
        if(rjson['result']['@resultCode'] == "0"):
            catalogList = {"@length": "0", "catalogInfo": []}
            contentList = {"@length": "0", "contentInfo": []}
            if("contentList" in rjson['result']['getDiskResult']):
                if(rjson['result']['getDiskResult']['contentList']['@length'] == "1"):
                    contentList["@length"] == "1"
                    contentList["contentInfo"].append(
                        rjson['result']['getDiskResult']['contentList']['contentInfo'])
                else:
                    contentList = rjson['result']['getDiskResult']['contentList']
            if("catalogList" in rjson['result']['getDiskResult']):
                catalogList = rjson['result']['getDiskResult']['catalogList']
            if(contentList['contentInfo']):
                print("云盘存在文件，准备分享文件...")
                self.shareFile(contentList['contentInfo'][0]['contentID'])

    def shareFile(self, contentID):
        url = "https://ose.caiyun.feixin.10086.cn/richlifeApp/devapp/IOutLink"
        body = self.buildShareBody(contentID)
        rjson = self.__post__(url, data=body)
        if(rjson and rjson['result']['@resultCode'] == "0"):
            print("分享文件[{0}]成功".format(contentID))
        else:
            print("分享文件[{0}]失败".format(contentID))

    def receiveAndSave(self):
        files = [3863, 3864, 3865, 3866, 3867]
        for file in files:
            url = "https://h.139.com/ccopapi/content/like/receiveAndSave/{0}".format(
                file)
            header = {"Cookie": "cookieTokenKey=".format(
                self.account['authorization'].replace("Basic ", ""))}
            rjson = self.__get__(url, header=header, isXml=False)
            if(not rjson):
                return
            if(rjson['code'] == 200):
                print("转存文件夹[{0}]成功".format(file))
            else:
                print("转存文件夹[{0}]失败：{1}".format(file, rjson['message']))
            sleep(2)

    def run(self):
        self.upFileEnter()
        print("")
        self.getCatalog()
        print("")
        self.receiveAndSave()


if __name__ == "__main__":
    accounts = [
        {
            "phone": "13221491521",
            "authorization": "Basic bW9iaWxlOjEzMjIxNDkxNTIxOmpGVk5CMmlOfDF8UkNTfDE2NTg5MDY1NjAzMzR8U3NiODV6RDZTZGFNU295ZWdFY2dVRHhMM19mN3phU1NPcHQwQTRUQUZZRVhmMTJhQ1p1dzlLUm5ZUWpBOWhiYXRUVFB0Ti5yMTdGSkdfZFRfU2R4ckFiWkFkZEsuVl9nOGd5YVdFNTFsUDBjdlMuNDAxbkc2eVhIQjdGQWtMRzNMUW5qNGtGbVpsRFFXX3ltcjNGSFZfeVZIeUg0cWtsMTRZQjhUWlRMdXY0LQ==",
            "remark": "13221491521"
        }
    ]

    for account in accounts:
        sdk = SDK(account)
        sdk.run()
        print("")
