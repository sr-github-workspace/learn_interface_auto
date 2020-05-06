'''
课后作业5：
接口部署地址：http://49.235.92.12:9000
1.登陆接口
POST /api/v1/login
Content-Type: application/json
{"username":"test","password":"123456"}
2.获取个人信息
GET /api/v1/userinfo
Content-Type: application/json
Authorization: Token 63914bfa94c81c09c4c93354519924e3d32cb5bc
使用python登录后获取token，参数关联获取个人信息能关联成功
'''
import requests
import json
url="http://49.235.92.12:6009/api/v1/login"
h1={
    "Content-Type": "application/json"
}
body={
    "username":"test",
    "password":"123456"
}
print(type(body))
r1=requests.post(url,headers=h1,data=json.dumps(body))
# r1=requests.post(url,json=body)
print(r1.text)
token=r1.json()["token"]
print(token)

url2="http://49.235.92.12:6009/api/v1/userinfo"
h2={
    "Content-Type": "application/json",
    "Authorization":"Token %s" % token
}
r2=requests.get(url2,headers=h2)
print(r2.text)
mail=r2.json()["data"][0]["mail"]
print(mail)
assert mail=="56577309@qq.com"