#!/usr/bin/env python3
# -*- coding:utf-8 -*-
########################################################
# Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
########################################################


############# 整数
############# 浮点数
print(1.23e9)
# 相等于
print(12.3e8)
# 0.000012 相等于下面的输出？？？
print(1.2E-5)

###########################################
# 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。
###########################################
print('\n')
############# 字符串类型
print('I\'m OK!')
print('I\'m \"OK\"!')
print('I\'m learning\nPython')
print('\\\n\\')
print("\\\t\\")
#r'' 表示''内部的字符串默认不转义
print(r'\\\t\\')

#命令行下 '''...''' 表示多行内容 相对于\n比较便于阅读
print('''line1
... line2
... line3''')
# .py文件中不使用...
print('''Line1
Line2
Line3''')

# r'''xxxx''' 不对字符串执行转义
print(r'''Hello, \n
world''')

print('\n')
############# 布尔值 经常用在条件判断中
print(True)
print(False)
print(not True)
print(not False)

print(3>5)
print(3<5)
print(not 3>5)
print(not 3<5)

age = 28
if age>=18:
    print('\'adult\'')
else:
    print('teenager')

######### 空值，None表示
# None不能理解为0，因为0是有意义的，而None是一个特殊的空值


a = 123  # a为整数
print(a)
a = 'ABC' # a 变为字符串
print(a)

print('\n')
######################################################
######################################################
# 要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
# Python对bytes类型的数据用带 b 前缀的单引号或双引号表示
x = b'ABC'
print(x)
print('ABC'.encode('ascii'))
print(x.decode('ascii'))
print("中文".encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
# ascii 识别不了的字符在解码时会报错
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('ascii'))


#################################################################
# len() 函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
#################################################################
print(len('abc'))
print(len("中文"))
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print("中文".encode('utf-8'))
print(len("中文".encode('utf-8')))

print("\n")

#################################### 占位符%?
print("hi, %s, your score is %d." % ("Brant", 534))
print('groth rate : %d %%' % 23)
# format
print('Hello, {0} 的成绩提升了{1}%'.format("小明", 17.125))
print('Hello, {0} 的成绩提升了{1:.1f}%'.format("小明", 17.125))

r = (85-72)/72
print('{0:.1f}%'.format(r))
