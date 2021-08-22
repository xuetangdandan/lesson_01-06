#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/26 20:35 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
python 里面凡是自己取的名字-- 标识符：命名规则 --- 变量 ，函数
1、只能包含数字 字母 下划线
2、不能数字开头
3、不能包含关键字  --Python自己定义的  有特殊意义的名词  ==pycharm 自动识别 -报错
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
'try', 'while', 'with', 'yield']
4、建议：数字字母之间用下划线隔开,方便阅读  class_01_01  大驼峰 ClassLemon

Python语法：
1、 缩进  --- 顶格编写
除了需要有缩进的时候--- 后面--同等级：对其，不同等级-缩进来区别 === 判断，循环 函数
2、注释
三种： 为什么需要加注释？？
1） #-单行注释： # 后面的内容都会被注释掉
2） 多行注释：  三引号 括起来的内容  被注释掉内容
3） 快捷键： ctrl + /  --注释 和反注释

注释原因：
1）解释你的代码--别人，自己看，方便阅读 --码农优秀品质
2） 修改代码，需求改了== 注释掉 ，不删除，备用

'''
# print('tricy是大家最喜欢的老师！')  # 注释
# print('蘑菇菌是71期最美！')
# print('飞羽是71期最帅！')
# 打印内容到控制台---- 调试代码的时候

# 常用数据类型： 整形（int）, 浮点型（float），布尔型（bool），字符串（str），列表，元组，字典，集合
# 判断数据类型内置函数：type（）--
print(type(True))
print(isinstance("xiaoluo",int))  #  布尔值--真
# 变量：--保险柜  存储数据的容器 --- 标识符--命名规则 1,2,3,4
# 5、见名之意
# 6、变量名--声明，再引用

'''
字符串（str）: 用成对引号括起来的内容 -- '',"", ''' '''
1) 引号嵌套 
2）三引号 ： 保持格式输出--所见即所得
'''
# name = '''hello lemon!'''   # 赋值操作：把右边的内容分赋值给左边的内容   ===声明--初始化过程
# print(type(name))
# print('"tricy"是大家'
#       '最喜欢的老师！')
# print('''------小骆的基本信息-------
# name：小骆
#     age：18
#         hobby：男
# ''')
'''
字符串常用操作：
1、取值 --位置= 索引 从0开始，依次往右排序  -- [索引]
2、取多个值 == 切片  [索引头:索引尾:步长]  --- 取头不取尾 --一定掌握！！！
默认值：索引头--- 默认0；尾-- 最后，步长--1
3、取最后一个元素 == -1  ， 逆序输出  --步长-1
4、计算长度--元素个数 len()  ---所有数据类型通用
5、元素--位置 ：find -- 输出元素的索引，index
6、帮我 把lemon  --替换 world   --- replace()  --替换字符串的字段
'''
str1 = "hello lemon!"  # 定义了一个字符串
#       01234567891011
# print(len(str1))
# print(str1[6:len(str1):1])
# print(str1.find("z"))   # 元素不存在 -- -1，没有报错--中断代码执行
# print(str1.index("z")) # 元素不存在 -- 直接报错--代码会中断
# print(str1.replace("lemon","world"))

# find = 10
print1 = 11   #  print-不再是一个函数了，只是变量--- 原本的内置函数不能再使用了
print(str1)

