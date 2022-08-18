import requests

header = {
    "Cookie":"CSESSIONID=9B1AFE3A0D226ABCF16A5F79C0F618F6; Domain=vsc46.hw.gmcc.net; Path=/; Secure; HttpOnly; SameSite=None;XSESSIONID=03GKLZNCJWL9IX485E4VUIXS55O0B6OP; Domain=vsc46.hw.gmcc.net; Path=/; Secure; HttpOnly; SameSite=None;JSESSIONID=03GKLZNCJWL9IX485E4VUIXS55O0B6OP; Domain=vsc46.hw.gmcc.net; Path=/; HttpOnly",
    "Content-type":"application/json",
    "User-Agent":"okhttp/3.12.0"
}

url = "https://vsc46.hw.gmcc.net/VSP/V3/CreateBookmark"
body = '{"bookmarks":[{"bookmarkType":"VOD","itemID":"385887933","rangeTime":1120}]}'

res = requests.get(url=url,headers=header,data=body)
print(res.text)