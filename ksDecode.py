
import hashlib
from urllib import parse


salt = "55ac69fd171e0ae6ec0c56ffbef1a803"
urlParams = "mod=HUAWEI%28P40%29&is_background=0&deviceBit=0&oc=JINGMEI_BAIDU_PINZHUAN%2C1&egid=DFP423EA189E48FB35150A91422F3E80E4E6691859B6BC1BBC18727641996F98&sbh=48&hotfix_ver=&appver=10.7.10.26854&grant_browse_type=AUTHORIZED&userRecoBit=0&socName=HiSilicon%20Kirin%20820&newOc=JINGMEI_BAIDU_PINZHUAN%2C1&max_memory=256&isp=&kcv=1474&boardPlatform=kirin820&did_tag=0&sys=ANDROID_7.1.2&sw=720&slh=0&oDid=ANDROID_BE7E829BAFDA06E5&rdid=ANDROID_908d6dab57d9a1cf&language=zh-cn&ver=10.7&country_code=CN&abi=arm32&kpn=KUAISHOU&cdid_tag=0&sh=1280&nbh=96&cold_launch_time_ms=1660172237410&androidApiLevel=25&earphoneMode=1&kpf=ANDROID_PHONE&browseType=4&did=ANDROID_BE7E829BAFDA06E5&ddpi=320&android_os=0&net=WIFI&app=0&is_app_prelaunching=1&device_abi=&ud=2920371133&c=JINGMEI_BAIDU_PINZHUAN%2C1&bottom_navigation=false&keyconfig_state=2&ftt=&is_app_prelaunch=0&darkMode=false&totalMemory=7567&iuid=&did_gt=1660153504577&__NS_sig3=66770724b08b4b57542e2d2c80702d434009c156333f3127&__NStokensig=e7a2228efaec3c5b75e394b8d716509681220fd2ab0a1de0c2ce8583566e088b&sig=29e70e5f79d5739282a6ae15f8f8924e"
bodyParams = "bizStr=%7B%22businessId%22%3A161%2C%22endTime%22%3A1660174198984%2C%22extParams%22%3A%2256dfe31594b858e69ef613f5e97227fbe816dba19bc273b16789f6a807954fd097d507cc7ddcc77b84401f1b9f69b20cdb89704a30f3845aed42dc6a070d5f3b9bbf908510d21ff0eda1c5dcd0bcf7872cf40e5a02d2cfcb361143dcd2be4b1ba5f91ed6f106bc8ece368ec78c1f360805597a7cb25c3770b2f2eae5bdb434a0b49f7943ca51f9a26283111288dd11453cf393fb154a11f2be9c042dc3289bbfd4981abc35d2799912c5a2816584e567f0a274329b7cceaf210981ba7ec825fd39fc99b645055c201031391b1af418ef65cd99679d6fcf97498161ab953522e6%22%2C%22mediaScene%22%3A%22video%22%2C%22neoInfos%22%3A%5B%7B%22creativeId%22%3A24901385875%2C%22extInfo%22%3A%22%22%2C%22llsid%22%3A2005327554565636385%2C%22taskType%22%3A1%7D%5D%2C%22pageId%22%3A100011251%2C%22posId%22%3A4687%2C%22reportType%22%3A0%2C%22startTime%22%3A1660174167535%2C%22subPageId%22%3A100013632%7D&kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHacXNU19mQ3uolkx-Tzg1ecv_Xh7nTfGbdLjfv5zaq0YinZVQyGWKMOM3CHgblFudCH_e3t5biLGyL2u8vMIBIWm8Xc1l-HkUiWb5zTS4NB4dmgPt1FSnJgrKE0c7GQw4Kr2_WCOydxRq1GNB8co7eCwScCnTn7pYjUhJYKTmdNHxT5Vy5Rfa3NgNECjG-D1AV_cZ-qA2R2zwvJI0zzlreGhJyESpTOl5I_JMcRn3Byf2u1vciIHZuJTJHMfHV76pkmIrO3wkm-TU1j-IkNSA4VWNk4ySsKAUwAQ&token=b49d0ffe2c2e44f8b8c64b3f5962df98-2920371133&client_key=3c2cd3f3&client_salt=55ac69fd171e0ae6ec0c56ffbef1a803&uQaTag=0&cs=false&os=android"

def parseParams(paramsA,paramsB):
    params = {}

    kvs = paramsA.split("&")
    for kv in kvs:
        k_v = kv.split("=")
        if(len(k_v) == 1):
            params[k_v[0]] = ""
        else:
            params[k_v[0]] = k_v[1]

    print(params)

    kvs = paramsB.split("&")
    for kv in kvs:
        k_v = kv.split("=")
        if(len(k_v) == 1):
            params[k_v[0]] = ""
        else:
            params[k_v[0]] = k_v[1]

    params.pop("sig","")
    params.pop("__NS_sig3")
    params.pop("__NStokensig")
    params.pop("client_salt")
    params.pop("sign","")
    print(params)

    ks = sorted(params.keys())
    str = ""
    for k in ks:
        if(not k):
            continue
        str += f"{k}={parse.unquote(params[k])}"
    return str

p = parseParams(urlParams,bodyParams)+salt
print(p)
md5 = hashlib.md5()
md5.update(p.encode("utf-8"))
print(md5.hexdigest())
