import hashlib
import urllib.parse

def getTokensig(sig,salt):
    v = sig+salt
    return hashlib.sha256(v.encode("utf-8")).hexdigest()

def getSig(params,salt):    
    dict_sort_res = sorted(params.items(),key=lambda x:x[0])
    ss = ""
    for k,v in dict_sort_res:
            ss += f"{k}={(v)}"
    ss += salt
    return hashlib.md5(ss.encode("utf-8")).hexdigest()

def getDict(params):
    if(params):
        d = {}
        ds = params.split("&")
        for kv in ds:
            k_v = kv.strip().split("=")
            if(len(k_v)==2):
                d[k_v[0]] = (k_v[1])
            else:
                d[k_v[0]] = ""
        return d
    else:
        return {}

salt = "100cf1f37bf81f0ab5b61d353f280778"
sig="485b247c03c841bf4b0db14d51ab5641"
data = "activityId=203&__NS_sig3=3a2b5b7803782f0c4e7271700b26b24e7470b00a6d636d7b&__NStokensig=0d9e5bb141cd8ff14d4c306f18172609abf981320a43de31ff7812b0b12f06af&kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHQumDrQXLHX7PXVUimDJwMIyRl9iSJVrH60uHP2EbVIw26gM29cU1jtVF28xrna9Cx0Sb7z4GWe4vxt3GIKzabSX34uPdOJKMtjsx-K2kRsmabzsQ0AT7Affuv2BMm1vCp_5MMREwW8nDWd1jkaknbIvB9qULt_5l0jiAODbyMvirEaZc71ga93ItkwQJV2ZiKikIPcQQ9nR0jJBBAvaDHGhJmtLHvm4BGCob9TuUwQR1Z_BoiIERMj__ln_VMNI-dJvNQssAl5nNNpgNr_tTB4Lj0QtBhKAUwAQ&token=07d3e257d7b543a19ace423e63941783-2920371133&client_key=3c2cd3f3&uQaTag=0&cs=false&os=android&sig=485b247c03c841bf4b0db14d51ab5641"
params = "mod=HUAWEI%28BRQ-AN00%29&abi=arm64&country_code=CN&kpn=KUAISHOU&is_background=0&deviceBit=0&oc=HUAWEI&egid=DFP099D72C55E19059991AAF33223EAA8CC26FB74B9715E2BAA1D04A1F5DF5F8&sbh=48&hotfix_ver=&appver=10.4.41.25925&sh=1280&grant_browse_type=AUTHORIZED&userRecoBit=0&cold_launch_time_ms=1658394766110&nbh=96&socName=HiSilicon%20Kirin%20820&newOc=HUAWEI&androidApiLevel=25&max_memory=256&isp=&kcv=1474&browseType=4&kpf=ANDROID_PHONE&ddpi=320&did=ANDROID_45890FE4706E577D&android_os=0&boardPlatform=kirin820&is_app_prelaunching=1&app=0&net=WIFI&device_abi=&did_tag=3&ud=2920371133&c=HUAWEI&sys=ANDROID_7.1.2&bottom_navigation=false&slh=0&sw=720&oDid=TEST_ANDROID_FBC46ED4918CA258&ftt=&keyconfig_state=2&rdid=ANDROID_4a4c88b01945cd43&is_app_prelaunch=0&language=zh-cn&darkMode=false&totalMemory=7567&iuid=&did_gt=1657440449407&ver=10.4"
print("salt:",salt)
print("sig:",sig)
print("sig Check:",getSig(getDict(params),salt))
print("tokenSig:",getTokensig(sig,salt))