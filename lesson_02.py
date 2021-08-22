#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/28 19:50 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
1. 下面哪些不能作为标识符？
1、find 2、 _num 3、7val 4、add. 5、def 6、pan 7、-print 8、open_file 9、FileName
10、print 11、INPUT 12、ls 13、user^name 14、list1 15、str_
答案：
1、find ----ok
2、_num ----ok
3、7val ----no,不能以数字开头
4、add. ----no,只能由字母,数字或下划线组成,不能包含.
5、def ----no,python关键字/保留字
6、pan ----ok
7、-print ----no,只能由字母,数字或下划线组成
8、open_file ----ok
9、FileName ----ok,一般变量名用蛇形小写,类名用大驼峰,模块名用小驼峰
10、print ----ok,但不推荐,这是python封装的一个函数,用了或导致print()用不了，list  str tuple
11、INPUT ----ok,python区分大小写,input!=INPUT
12、ls ----ok
13、user^name----no,只能由字母,数字或下划线组成
14、list1 ----ok
15、str_ ----ok
'''
'''
1、格式化输出： 
第一种：字符串里传入变量值的时候，.format()--函数  --- 重点掌握
1） 占位符--{}
2）后面.format()
3）可以默认按照位置变量的传入，也可以指定位置传入 === 不能混用
第二种：% --- 占位符 ---了解
%s ---字符串 ===匹配所有数据类型
%d --- 数字
%f  -- 浮点型
'''
name = "蘑菇菌"
age = "18"
hobby = "周杰伦"
# print('''------{0}的基本信息-------
# name：{3}
# age：{2}
# hobby：{1}
# '''.format(name,name,age,hobby))
# print('''------%s的基本信息-------
# name：%s
# age：%s
# hobby：%s
# '''%(name,name,age,hobby))
'''
1 + 1 = 2  运算符， 运算数
Python运算符
1）算术运算符 ： + - * / %  ** 
2）赋值运算符 ： = 左边的赋值给右边的变量  +=  -=
3) 比较运算符 ： > >=  < <= == !=   (<>python2里的不等于)  ==结果是bool，True  False
4）逻辑运算符： and == 真真为真  or == 假假为假  not     ==结果是bool，True  False
5）成员运算符： in , not in   ==结果是bool，True  False
'''
# 加号： 1、 数字相加  2、两个字符串拼接==== str()--数据类型强制转化为字符串,int(),float(),bool()
# print(1 + 2)
# print(str(123) + "sunset")  # 123sunset
# 减号 - 数字减法 --不能用字符串相减
# print(5 - 3)
# print("123abc" - "123")
# 乘法 * 1、 两个数字相关  2、字符串的重复输入* 重复的次数
# print(2 * 3)
# print("我爱你" * 100)
# # 除法 /   --结果是浮点型
# print(10 / 3)

# a = 10
# a += 5 #a = a + 5
# a -= 10 # a = a - 10
# # b = 20
# print(a)
# print(10 > 20)
# print("手机号码不能为空" == "注册成功")  # 比较字符串 ==执行结果 vs  预期结果

# print(not 5 < 6)
#      False       True

# str1 = "hello lemon!"
# print("h" in str1)
# 从控制台进输入  -- input()   == 注意： input输入的内容 数据类型是 字符串-- 数字？？ int()
name1 = int(input("请输入你的名字："))
print(type(name1))
'''
列表，元组 ，字典，集合
控制流： for循环   if判断
'''
ste = "abc"
ste.