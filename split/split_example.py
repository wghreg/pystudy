#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''

参考

Python list [http://diveintopython.org/native_data_types/lists.html]
Python tuple [http://diveintopython.org/native_data_types/tuples.html]
Python 字符串方法 [http://docs.python.org/3/library/stdtypes.html#string-methods]
Python array [http://docs.python.org/library/array.html]

'''


# 示例 1: 打印出一个包含网站技术的列表
s = "python, javascript, jquery"
print(s.split(","))     # ['python', 'jquery', 'javascript']

a, b, c = s.split(",")  # a='python', b='javascript', c='jquery'

print("a=%s, b=%s, c=%c" %(a, b, c))


#示例 2: 提取网址组成部分
s = 'irc.freenode.net'
subdomain, domain, tld = s.split('.')
# subdomain = 'irc'
# domain = 'freenode'
# tld = 'net'


#示例 3: 提取网站域名
s = 'irc.freenode.net'
i = s.split('.', 1)
domain_name = i[1]  #'freenode.net'


# 示例 4: 唱一首歌
lyrics = 'one! two! three! four!'
nums = lyrics.split(' ', 2)
for num in nums:
     print('I say' + num)
