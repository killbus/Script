import requests

url = "https://api.m.jd.com/"
cookie = '__jdc=122270672;unpl=;pt_pin=jd_6c2a072d41c27;pwdt_id=jd_6c2a072d41c27;pt_key=app_openAAJi9jumADBxJACWyqBnYUqzzhMw1TWf8_vWGn-k6MnX-ellThvM_6cfcMycFw3yfxXshnDu6-k;sid=28d4d6883cd62acf3a918181bf6b936w;__jdv=122270672%7Ciosapp%7Ct_335139774%7Cliteshare%7CCopyURL%7C1660304341688;shshshfpb=oVRLVC9r2lihpEJz9dD6ojA;b_dw=360;b_dh=715;b_dpr=2;b_webp=1;b_avif=0;cid=8;shshshfp=a6e306e50269eae5735a785030a11cb3;shshshfpa=95ded20d-6bc1-fe16-c107-5f567eb93940-1660304432;_gia_s_local_fingerprint=9f979a9047a066255262c5e3a4c3d133;_gia_s_e_joint={"eid":"5AUSUIHJYT42XWTNOJHUY7K3S5NWDCVM63VK7WVSILQFG7DYN4CKT7UEQRCKTODP7AD7IL5GVRGLJQ5FWFEY4LBWBI","ma":"","im":"","ip":"120.231.37.182","ia":"","uu":"","at":"100"};3AB9D23F7A4B3C9B=5AUSUIHJYT42XWTNOJHUY7K3S5NWDCVM63VK7WVSILQFG7DYN4CKT7UEQRCKTODP7AD7IL5GVRGLJQ5FWFEY4LBWBI;joyya=1660304420.1660304434.29.1tyo0jr;__jda=122270672.16574517410511561683527.1657451741.1660307377.1660316283.10;pre_session=Wre/QW5Q5Nv9t91ZMaVOgWGdW3drIOAr|16;pre_seq=8;__jdb=122270672.4.16574517410511561683527|10.1660316283;mba_sid=10.23;mba_muid=16574517410511561683527.10.1660316548828'
header = {
    "Content-type": "application/x-www-form-urlencoded",
    "Cookie": cookie,
    "User-Agent": 'jdltapp;android;3.9.2;;;appBuild/2335;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1660316538202%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22CJcnYzcmZtOmYJuzCNG3Cq%3D%3D%22%2C%22od%22%3A%22CNC2CtDtDzcjCNczEI00DNCnBJqyEWSjCtHuZtOzZQGnENc3%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22CJcnYzcmZtOmYJuzCNG3Cq%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jd.jdlite%22%7D;Mozilla/5.0 (Linux; Android 10; CDY-AN00 Build/HUAWEICDY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36',
    "origin": "https://joypark.jd.com"
}
body = 'functionId=joyBaseInfo&body={"taskId":"","inviteType":"","inviterPin":"","linkId":"LsQNxL7iWDlXUs6cFl-AAg"}&t=1660316549246&appid=activities_platform&h5st=20220812230229253%3B4267080193408768%3B4abce%3Btk02waeed1bee18n5joqwqCHFF2uij569RoxTYiByOOjM2M1GGngfftdBxIV61Sy1yBw2naPyDnrGP1NuFJrL6DCcAPE%3B2de448c7d15665dbdfef37902ddac218a1b69f54a5bf5c7bcd590d1e592233c9%3B3.1%3B1660316549253%3B62f4d401ae05799f14989d31956d3c5f4d78385f3f4feb3b7242c97f22593b9892f7a15c58d08b62eb4a7a884947070a35946a2cdbc2997ab5ad5d68d2ddd2f04a9621f66b1e87426d8aa2ce1635cfa8bd8b1fac944a1a1d570cddff231a73ebb945f88ce66165e6eed9026832f57022eca1fc2b32209acb7eff4e30995996c448f08a62c6d3101efa48afa1594dd96f&cthr=1'

res = requests.post(url,headers=header,data=body)
print(res.text)