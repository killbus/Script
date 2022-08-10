
import hashlib
from urllib import parse


salt = "65a69840f93db2d4658cdd516bfaa556"
urlParams = "mod=HUAWEI%28P40%29&is_background=0&deviceBit=0&oc=ANDROID_SHENMA_ZW_SSYQ_CPC&egid=DFPB5C9C46B0DC28BC8A50BD57F9FC55FA41C7BE2595B9D24831D75E86922430&sbh=48&hotfix_ver=&appver=9.11.50.23442&grant_browse_type=AUTHORIZED&userRecoBit=0&socName=HiSilicon%20Kirin%20820&newOc=ANDROID_SHENMA_ZW_SSYQ_CPC&max_memory=256&isp=&kcv=1474&boardPlatform=kirin820&did_tag=3&sys=ANDROID_7.1.2&sw=720&slh=0&oDid=TEST_ANDROID_610ABBFAC9A09BCD&rdid=ANDROID_690ba5a4e28dae1d&language=zh-cn&ver=9.11&country_code=CN&abi=arm32&kpn=KUAISHOU&sh=1280&app_status=3&nbh=96&cold_launch_time_ms=1660114410173&androidApiLevel=25&kpf=ANDROID_PHONE&browseType=4&did=ANDROID_A81C67B7443394E4&ddpi=320&android_os=0&power_mode=0&net=WIFI&app=0&is_app_prelaunching=1&device_abi=arm64&ud=2920371133&c=ANDROID_SHENMA_ZW_SSYQ_CPC&bottom_navigation=true&keyconfig_state=2&ftt=&is_app_prelaunch=0&darkMode=false&totalMemory=7567&iuid=&did_gt=1659889891151"
bodyParams = "bizStr=%7B%22businessId%22%3A100%2C%22endTime%22%3A1660114665941%2C%22extParams%22%3A%221aa7e80d47286277603b75aaeb2356552657bb780c67b9110581983c0de61e03b1ff700e7f0e3a08a95f7da20e59c90408b8b20ba905a5487a3e711ae933f4cf4798f6f063129200157d5cc3bf495db563489e16e80aa958700af9662da91880%22%2C%22mediaScene%22%3A%22video%22%2C%22neoInfos%22%3A%5B%7B%22creativeId%22%3A24901385878%2C%22extInfo%22%3A%22%22%2C%22llsid%22%3A2001517746532676050%2C%22taskType%22%3A1%7D%5D%2C%22pageId%22%3A100011251%2C%22posId%22%3A774%2C%22startTime%22%3A1660114635885%2C%22subPageId%22%3A100011252%7D&__NS_sig3=1607775493cb4e562d5e5d5c14235822ae10b626624f4157&__NStokensig=cc04b97695aa7ac7980242c730d391dbbbb63a361834fc38a5c6d76b96b2e576&kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAG4kNKIMq6o3eY-yEyDM4pZGzAJDR9Z-RVvKYTR67GOLZ0Wngoyb2TS5Vw1ISt6eHXhkzP0FTRIeotFE6IRKQUezeXwFF5FRJ9hSkHPIdGKETQDUZyXAwUkRNRwN9IIcU15Mun0icuy9gbx6XyS_Umn-ho26UJp-wIoAKewX06LvCXoSB0INU0UmakAlRuidiJBa5oYITyOLkkVCed_CnrFGhLZe8NH31JEM6ppJzAS6A8iBVUiIIn10CePu4iV9krKytxQItqpZn6CLqhoZcP_uObz4B5cKAUwAQ&token=1c766724883a4166b9c822eb23d3ee9d-2920371133&client_key=3c2cd3f3&uQaTag=0&cs=false&os=android&sig=ad6c1f3752fc0dcb40dd9508cea52c71"

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
