#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/29 9:09 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
"""
列表：list []---list()
1、元素-可以是任意的数据类型：int ,float,bool,str,list，tuple，字典，元素之间用逗号（英文）隔开
2、取值 --索引取值  ==字符串取值一样  ==list嵌套取值
取多个值：切片 --- [索引头:索引尾:步长]  --- 取头不取尾 --一定掌握！！！
3、list的元素可以被改变！！ 操作：增加，删除，修改
4、元素可以被重复，统计元素的个数 -- count（）
5、统计所有元素的个数  len()
"""
# list1 = [12,3.14,True,"社会杨",[1,2,3,4,5]] # 空列表
# print(list1[4][3])
# # 增加元素
# list1.append("小书生")   # 可以追加元素到列表--- 最后位置
# list1.insert(3,"凉公子")  # 可以指定位置进行元素添加
# list1.extend(["凉夏","一些"])  # 可以同时添加多个元素
# # list1.append(["凉夏","一些"]) #区别
# print(list1)
# 删除元素
# list1.pop(5) # 1、默认删除最后一个元素  2、指定索引进行删除
# print(list1)
# list1.remove(True) # 指定元素本身进行删除
# print(list1)
# list1.clear()  # 清除 之后空列表
# print(list1)
# del list1  # 把列表本身删除
# print(list1)
# 修改   =取值  后 重新赋值
# list1[0] = "飞羽"
# list1[1] = "路飞"
# print(list1)
# list1.append("路飞")
# print(list1)
# print(list1.count("路飞"))
# print(len(list1))
"""
元组：tuple ()
['飞羽', '路飞', '凉公子', '社会杨', '小书生', '凉夏', '一些', '路飞']
1、元素-可以是任意的数据类型：int ,float,bool,str,list，元素之间用逗号（英文）隔开
2、取值 --索引取值  ==字符串取值一样  ==list嵌套取值
取多个值：切片 --- [索引头:索引尾:步长]  --- 取头不取尾 --一定掌握！！！
3、元素是不可以被改变的
4、元素可以被重复，统计元素的个数 -- count（）
5、统计所有元素的个数  len()
"""
# tuple1 = ('飞羽', '路飞', '凉公子', '社会杨', '小书生', '凉夏', '一些', '路飞') # 空元组
# print(tuple1[0])
# list2 = list(tuple1)  # 把元组转化为 列表
# tuple1[0] = "墨"
# print(list2)
# list2[0] = "墨"
# print(list2)
# tuple2 = tuple(list2) # 列表 --> 元组
# print(tuple2)
"""
字典：dict  {}
1、 元素一对键值对： {key：value，key1：value}，key--键， value：值
2、字典使用场景：描述一个物体的属性 -- name：唯一，age：18，city：深圳  -
3、取值：value
4、字典没有索引 -- Python3.6之前字典都是没有顺序的 --不能通过索引取值 ！！！ 
通过key取value
5、key， value规则：key唯一的，不可变，不能重复 == 不能是列表和字典，最常用字符串
value：没有任何限制
6、字典操作：增加  删除 修改
7、len（） --- 统计个数
"""
dict1 = {"name":"唯一","age":"18","city":"深圳"} #空字典
print(dict1["name"]) # key取value
print(dict1.get("name")) # key取value
# 增加 --- 通过添加键值对-字典加元素 ==如果key是不存在的--增加
dict1["height"] = "180"
dict1["weight"] = "160"
print(dict1)
dict1.update({"gender":"Male","hobby":"女"}) # 添加多个字典的元素
print(dict1)
# 修改   -- 如果key是存在的--修改
# dict1["city"] = "北京"
# print(dict1)
# # 删除
# dict1.pop("city")  # 指定key进行元素的删除
# print(dict1)
"""
集合：set {} --元素和字典的格式不一样
1、元素不能重复的 == 使用场景：用来给列表去重
2、元素无序的
"""
# set1 = {11,22,22,33,33,33,44}
# # print(set1)
# list3 = [11,22,22,33,33,33,44]
# # 去重 --集合
# set2 = set(list3)
# print(set2)
# list4 = list(set2)
# print(list4)
"""
控制流：控制代码走向 == 判断 ，循环
判断：if 
if 判断条件：--- 冒号-4个空格缩进（tab键）
    执行语句
elif 判断条件： --- 可以有一个、多个，没有
    执行语句
elif 判断条件：
     执行语句
else：
    执行语句
True == 1, False == 0 
"""
# money = int(input("请输入你的存款金额："))  # input达到的是字符串
# if  money >= 200:  # 运算符计算结果-- True==才会进入到这个分支进行语句执行；False== 下一个分支的判断
#     print("来柠檬学习Java")  # 缩进== 分支的子代码
# elif money >= 100:
#     print("来柠檬学习Python")
# elif money >= 50:
#     print("来柠檬学习性能")
# else:  # 以上所有条件都不满足（True），进入else分支
#     print("买个碗，乞讨！")

"""
For: 循环 -- 遍历 数据类型的所有元素 ： 字符串，列表，元组，字典
1、循环的次数 ？？--元素个数
2、跳出循环 
1) break  --- 跳出循环，后面的代码都不会再执行 --中断
2）continue --- 跳出本次循环，后面的代码继续执行 --跳出

"""
# str5 = "hello lemon!"
# count = 0  # 计算器
# for i in str5:
#     if i == "h" or i == "e":  # True
#         # break
#         continue
#     print(i)
#     print("**" * 20)
#     count += 1
# print(count)  # 循环次数
# print(len(str5))

# range() --- 内置函数：生成一个整数序列  - 经常跟for循环一起使用
# start：   stop    step  ==切片 --- 可以有默认值： start -0，stop -必填，step = 1
# 取头不取尾
# for num in range(10):
#     print(num)

dict2 = {"name":"tricy","age":18}
dict3 = dict(name="tricy",age="18")
print(dict2,dict3)