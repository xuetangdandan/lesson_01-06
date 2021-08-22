#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/31 17:47 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
"""
第二次作业：
1、在pycharm的控制台里输入以下内容，并且以如下格式输出到控制台
# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")
# gender = input("请输入你的性别：")
# print('''********************
# 姓名：{}
# 年龄：{}
# 性别：{}
# ********************'''.format(name,age,gender)
#       )
2、现在有字符串：str1 = 'python hello aaa 123123aabb'
1）请取出并打印字符串中的'python'。
2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？
3）替换python为 “lemon”.
4) 找到aaa的起始位置
str1 = 'python hello aaa 123123aabb'
print(str1[0:6:1])
print("o a" in str1)
print("he" in str1)
print(str1.replace("python","lemon"))
print(str1.find("aaa"))
print(str1.index("aaa"))
"""
'''
函数:同样的代码，重复使用--封装成函数，重复调用=== 提高代码复用率
语法：
1、定义：
def 函数名():  ===  标识符 ？？---命名规则：1~5
    函数体 （实现具体功能的代码段）
2、函数的调用：不调用 函数是不会执行的
调试代码--debug  1、 断点 2、点击debug按钮  3、 单步执行 -F8  == 一步一步调试，检查哪一步执行的时候出错了 === 课外扩展
3、 封装的代码里可能会变化的值-- 定义成函数的参数（变量） == 写在括号里
函数参数：
3.1 定义函数的三种参数类型： 
1） 必备参数：定义了必须要传入的参数  == 没有传入报错
2） 默认参数（缺省参数）：如果大部分的情况都是这个值== 设置为参数的默认值-- 传入参数的时候就可以不传(默认值),可传入--为准
注意：位置一定要在必备后面
3） 不定长参数：不传，可以传入一个或多个；
 *args： 前面的参数都接收完了，剩下的参数都会被这个不定长参数接收，并以元组格式保存。== 位置传参方式
 **kwargs：前面的参数都接收完了，剩下的参数都会被这个不定长参数接收，并以字典格式保存。== 关键字传参方式
3.2 参数的传入方式：
1、位置传参： 按照位置顺序传入参数
2、关键字传参：指定参数名进行参数传入 --不会管参数顺序 --可靠
3、混合传参：关键传参 要在 位置传参后面
'''
# def good_job(salary,bonus,subsidy=500,*args,**kwargs):   # 定义参数--形参
#     sum_all = salary + bonus + subsidy
    # print("salary的值：{}".format(salary))
    # print("bonus的值：{}".format(bonus))
    # print("subsidy的值：{}".format(subsidy))
    # print("args的值：{}".format(args))
    # print("kwargs的值：{}".format(kwargs))
    # for item in args:
    #     sum_all += item
    # for j in kwargs:
    #     # sum_all += kwargs[j]   # 通过key取value
    #     sum_all += kwargs.get(j)
    # # print("我的工资总和是：{}".format(sum_all))
    # return sum_all,salary  # 定义函数的返回值  ==1，多个
    # print("这个函数执行完了么?")

# 函数调用-- 函数名
# result = good_job(12000,12500,400,100,200,300,aa=100,bb=200,cc=300,dd=400)   # 传入参数：实参
# 用变量来接收函数的返回值  == 掌握！！！
# print("我的工资总和是：{}".format(result))
# if result > 20000:
#     print("这是个好工作！")
# else:
#     print("这不是个好工作！")
"""
返回值： 需要给到别人用去做后续的事情-- 从函数里抛出去 == 定义为函数的返回值  ，调用函数的时候就可以得到这个返回值
return  - 定义返回值
1、可以没有返回值--- None （空）
2、可以定义一个  == 变量接受函数的调用 ==返回值、
3、可以定义多个，中间用逗号隔开  == 接受的结果是个元组 
注意点： 函数的返回值一定要在函数末尾
"""

"""
内置函数：
print()
input()
type()
isinstance()
len()
str(),int(),list(),tuple(),dict(),float() bool()
format()
range()
append, insert，remove, extend，count,get，index  find， replace 等  == 列表 字典  字符串里的内置函数
"""
"""
函数作业：
2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套
"""
# def add_func(num):  # 参数
#     sum = 0
#     for i in range(num):
#         sum += i
#     return sum  # 返回值
# res = add_func(101)  # 接受函数返回值
# print(res)
# def judge_len(object):
#     # if type(object) == str or type(object) == list or type(object) == dict:
#     if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):
#         if len(object) >= 5:
#             print("True")
#         else:
#             print("False")
#     else:
#         print("你输入的数据类型错误！")
# judge_len([1,2,3,4])














