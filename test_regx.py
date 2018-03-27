#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
from pkg_resources._vendor.packaging.requirements import IDENTIFIER
## match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
print(re.match(r"^\d{3}\-\d{3,8}$", "010-12345"))
print(re.match(r"^\d{3}\-\d{3,8}$", "010 12345"))
'''
# 常见的判断方法:
test = "用户输入的字符串"
if re.match(r"正则表达式", test):
    print("ok")
else:
    print("failed")

# 上面的两个表达式可写为：
'''
print("\n使用if..else判断：")
if re.match(r"^\d{3}\-\d{3,8}$", "010-12345"):
    print("OK")
else:
    print("Failed")

if re.match(r"^\d{3}\-\d{3,8}$", "010 12345"):
    print("OK")
else:
    print("Failed")

## 正则处理切片 split
print("\n使用正则处理字符串切片：")
print("a b   c".split(" "))
print(re.split(r"\s+", "a b   c"))
print(re.split(r"[\s\,]+", "a,b,  c  d"))
print(re.split(r"[\s\,\;]+", "a,b;;  c  d"))

## 正则分组用 group
print("\n正则分组 result.group(n)")
# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来
m = re.match(r"^(\d{3})-(\d{3,8})$", "010-12345")
print(m.group(0))   # group（0）应该是贪婪匹配的最大长度，而不是原始字符串。
print(m.group(1))   # group(1)、group(2)……表示第1、2、……个子串。
print(m.group(2))
'''
group（0）应该是贪婪匹配的最大长度，而不是原始字符串。
group（0）应该是贪婪匹配的最大长度，而不是原始字符串。
group（0）应该是贪婪匹配的最大长度，而不是原始字符串。
'''

t = "17:47:55"
# ()标识分组，下面分为三组，第一组第一位第二位都是0-9范围，第二组第一位从最大为5，第三组第一位最大为5
m = re.match(r"^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$", t)
print(m.groups())

## 贪婪匹配
# 注意：正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print("\n贪婪匹配：")
print(re.match(r"^(\d+)(0*)$", "102300").groups())  # (\d+)贪婪匹配，把整个数字匹配上了,(0*)只能匹配空字符串
print(re.match(r"^(\d+?)(0*)$", "102300").groups()) # ?就可以让\d+采用非贪婪匹配

'''
编译

当我们在Python中使用正则表达式时，re模块内部会干两件事情：
    1. 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
    2. 用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''
print("\n先编译生成Regular Expression对象，该对象包含了正则表达式，调用时不用给出正则字符串：")
re_telephone = re.compile(r"^(\d{3})-(\d{3,8})$")
print(re_telephone.match("010-12345").groups())
print(re_telephone.match("010-8086").groups())
# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。

'''
练习

请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

someone@gmail.com
bill.gates@microsoft.com
'''
# import re
print("\n练习：\n1. 判断Email地址：")
def is_valid_email(addr):
    re_email = re.compile(r"^[\w]+?[\w.|-]+?@(\w+?)\.(\w+?)$")
    if re_email.match(addr):
        return True
    else:
        return False
print(is_valid_email("someone@gmail.com"))
print(is_valid_email("bill.gates@microsoft.com"))
print(is_valid_email("someone#example.com"))
print(is_valid_email("mr-bob@example.com"))
print(is_valid_email("mr_bob@example.com"))
print(is_valid_email(".mr_bob@example.com"))
print(is_valid_email("-mr_bob@example.com"))
print(is_valid_email("_mr_bob@example.com"))
print(is_valid_email("_mr_bob.@example.com"))
print(is_valid_email("_mr_bob-@example.com"))
print(is_valid_email("_mr_bob_@example.com"))
print(is_valid_email("_mr_bob_aaa@example.com"))

print("\n2. 提取出带名字的Email地址：")
def name_of_email(addr):
    regx1 = re.compile(r"^(\<[\w\s]+?\>)\s[\w]+?[\w.|-]+?@(\w+?)\.(\w+?)$")
    regx2 = re.compile(r"^([\w]+?[\w.|-]+?)@(\w+?)\.(\w+?)$")
    name = None
    if regx1.match(addr):
        name = regx1.match(addr).group(1)
    elif regx2.match(addr):
        name = regx2.match(addr).group(1)
    return name

print(name_of_email("<Tom Paris> tom@voyager.org") == 'Tom Paris')
print(name_of_email("tom@voyager.org") == 'tom')

print(name_of_email("<Tom Paris> tom@voyager.org"))
print(name_of_email("tom@voyager.org"))