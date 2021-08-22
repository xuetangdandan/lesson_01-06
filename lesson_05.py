#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/9/2 19:40 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
"""
1：a=[1,2,'6','summer']  请用成员运算符判断 i是否在这个列表里面
2：dict_1={"class_id":45,'num':20}  请判断班级上课人数是否大于5
注：num表示课堂人数。如果大于5，输出人数。
3、list3 = ['飞羽', '路飞', '凉公子', '社会杨', '小书生', '凉夏']
列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。
方法1： 手动扩充--字典--存放在列表里面；{} --简单
方法2： 自动--dict（）--不强制 list.append()
"""
# a=[1,2,'6',"i",'summer']
# if "i" in a:
#     print("i是a列表的成员")
# else:
#     print("i不是a列表的成员")
# dict_1={"class_id":45,'num':20}
# num = dict_1.get("num")
# if num > 5:
#     print("班上的人数是：{}".format(num))
# else:
#     print("班上人数不足5人！")
# list3 = ['飞羽', '路飞', '凉公子', '社会杨', '小书生', '凉夏']
# dict1 = {"name":"飞羽","gender":"male","age":18,"city":"深圳"}
# dict2 = {"name":"路飞","gender":"male","age":18,"city":"深圳"}
# dict3 = {"name":"凉公子","gender":"male","age":18,"city":"深圳"}
# dict4 = {"name":"社会杨","gender":"male","age":18,"city":"深圳"}
# list4 = [dict1,dict2,dict3,dict4]
# list1 = [19,18,20,21,22,24]
# list2 = ["male","Female","male","Female","male","Female"]
# list5 = ["深圳","北京","程度","重庆","上海","杭州"]
# list4 = []
# for name in list3:
#     dict1 = dict(name=name,age=18,gender="male",city="深圳")
#     list4.append(dict1)
# print(list4)
# for i in range(len(list3)):
#     dict1 = dict(name=list3[i],gender=list2[i],age=list1[i],city=list5[i])
#     list4.append(dict1)
# print(list4)

"""
接口测试：第三方库--别人写好封装好，你可以直接拿来的用的功能  === requests  --参数传入用字典格式传入
两个步骤： 
1、安装 --pip 自动下载安装第三方库 == pip install requests --user
2、导入--Python文件里--范围内可以直接使用
"""
import requests   # 导入第三方库
import pprint  # 按照格式打印内容
import jsonpath   # 第三库--- pip  install jsonpath
# 注册接口
qcd_url = "http://120.78.128.25:8766/futureloan/member/register"   # 接口地址
qcd_data = {"mobile_phone": "13867888811","pwd": "123456789"}
qcd_headers = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
response = requests.post(url=qcd_url,json=qcd_data,headers=qcd_headers)  # 返回值 --响应消息
# print(response.json())   # 得到响应结果

# 登录接口
qcd_url = "http://120.78.128.25:8766/futureloan/member/login"   # 接口地址
qcd_data = {"mobile_phone": "13867888811","pwd": "123456789"}
qcd_headers = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
response = requests.post(url=qcd_url,json=qcd_data,headers=qcd_headers)  # 返回值 --响应消息
# pprint.pprint(response.json())   # 得到响应结果
"""
{'code': 0,
 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved',
 'data': {'id': 1139394,
          'leave_amount': 0.0,
          'mobile_phone': '13867888811',
          'reg_name': '小柠檬',
          'reg_time': '2020-09-02 20:52:14.0',
          'token_info': {'expires_in': '2020-09-02 21:00:36',
                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjExMzkzOTQsImV4cCI6MTU5OTA1MTYzNn0.XVLBnFIHYThfpebXFN3b7zC7RoT_Kaq6HLT556nITq-p9rP73mov40F-7d6w8RLg92QOfUKm59CXH6O-M829Pg',
                         'token_type': 'Bearer'},
          'type': 1},
 'msg': 'OK'
 }
"""
# 充值：
# id_login = response.json().get("data").get("id")
# token_login = response.json().get("data").get("token_info").get("token")
id_login = jsonpath.jsonpath(response.json(),"$..id")[0]   # 存在列表里 --- [0]--列表取值
token_login = jsonpath.jsonpath(response.json(),"$..token")[0]
qcd_url_recharge = "http://120.78.128.25:8766/futureloan/member/recharge"   # 接口地址
qcd_data_recharge = {"member_id":id_login, "amount": 6300}
qcd_headers_rec = {"X-Lemonban-Media-Type":"lemonban.v2",
               "Content-Type":"application/json",
               "Authorization":"Bearer "+token_login}
response = requests.post(url=qcd_url_recharge,json=qcd_data_recharge,headers=qcd_headers_rec)  # 返回值 --响应消息
# pprint.pprint(response.json())   # 得到响应结果

#  百度
# 1、 乱码
# 2、 页面内容不对  -- baidu服务器反爬机制--机器发过来===返回一个随便页面 -- Python
# baidu_url= "https://www.baidu.com/"
# baidu_headers = {"User-Agent":
#                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}
# res = requests.get(url=baidu_url,headers=baidu_headers)
# # print(res.text)   # 文本格式结果   ==  自动进行解码--大部分的页面 -80%
# print(res.content.decode("utf8"))   #手动指定 解码
# 带参数的百度请求
# baidu_url= "https://www.baidu.com/s"
# baidu_headers = {"User-Agent":
#                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}
# baidu_par = {"wd":"柠檬班"}
# res = requests.get(url=baidu_url,headers=baidu_headers,params=baidu_par)
# # print(res.text)   # 文本格式结果   ==  自动进行解码--大部分的页面 -80%
# print(res.content.decode("utf8"))   #手动指定 解码




