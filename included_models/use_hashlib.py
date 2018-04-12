#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
摘要算法简介

Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

举个例子，你写了一篇文章，内容是一个字符串'how to use python hashlib - by Michael'，并附上这篇文章的摘要是'2d73d4f15c0db7f5ecb321b6a65e5d6d'。如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，你可以一下子指出Bob篡改了你的文章，因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。

可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
'''
import hashlib
md5 = hashlib.md5()
md5.update("how to use md5 in python hashlib?".encode('utf-8'))
print("md5: ", md5.hexdigest())  # d26a53750bc40b38b65a520292f69306
# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5 = hashlib.md5()
md5.update("how to use md5 in ".encode("utf-8"))
md5.update("python hashlib?".encode("utf-8"))
print("md5分段update: ", md5.hexdigest())  # d26a53750bc40b38b65a520292f69306

'''
改动一个字母，计算的结果完全不同。
MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
'''
# import hashlib
sha1 = hashlib.sha1()
sha1.update("how to use sha1 in ".encode("utf-8"))
sha1.update("python hashlib?".encode("utf-8"))
print("\nsha1: ", sha1.hexdigest()) # 2c76b57293ce30acef38d98f6046927161b46a44

'''
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。

有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？
完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。
这种情况称为碰撞，比如Bob试图根据你的摘要反推出一篇文章'how to learn hashlib in python - by Bob'，
并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非常非常困难。

摘要算法应用
摘要算法能应用到什么地方？举个常用例子：
    任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：
name	    password
-----------------------------------------------
michael	    123456
bob	        abc999
alice	    alice2008

如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。
此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。

正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
username	password
-----------------------------------------------
michael	    e10adc3949ba59abbe56e057f20f883e
bob	        878ef96e86145580c38c87f0410ad153
alice	    99b1c2188db85afee403b1536010c2c9

当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。

练习
根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    pass
存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。

设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
'''
# -*- coding: utf-8 -*-
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    md5 = hashlib.md5()
    tmp = password
    md5.update(password.encode("utf-8"))
    password = md5.hexdigest()
    for name in db.keys():
        if user == name:
            print("%s's password '%s' is true."%(user, tmp))
            return password == db.get(name)

# 测试:
assert login('michael', '123456')       # True
assert login('bob', 'abc999')           # True
assert login('alice', 'alice2008')      # True

assert not login('michael', '1234567')  # True
assert not login('bob', '123456')       # True
assert not login('alice', 'Alice2008')  # True
print('ok')

'''md5转换'''
def get_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode("utf-8"))
    return md5.hexdigest()

'''密码加盐'''
def calc_md5(password):
    return get_md5(password + "the-Salt")

print("\nmd5加盐转换：", calc_md5('123456'))

'''
如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。

练习
    根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
db = {}
def register(username, password):
    db[username] = get_md5_salt(password + username + "the-Salt")
'''
import hashlib, random
print("\n密码加盐后获取对象摘要：")
def get_md5_salt(str):
    return hashlib.md5(str.encode("utf-8")).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = "".join([chr(random.randint(48, 122)) for i in range(20)])
        print("输出盐：", self.salt)
        self.password = get_md5_salt(password + self.salt)
# db在函数login外部，为什么可以直接调用？ 局部函数不改变全局变量的情况下，可以不用global，直接调用
db = {
    "张三": User("张三", "123456"),
    "李四": User("李四", "abc999"),
    "赵六": User("赵六", "alice2008")
}

def login2(username, password):
    user = db[username]
    print("原password=", password, "; md5加随机盐后的password=", user.password)
    return user.password == get_md5_salt(password + user.salt)

# 测试：
assert login2("张三", "123456")
assert login2("李四", "abc999")
assert login2("赵六", "alice2008")
print("OK!")

'''
小结

摘要算法在很多地方都有广泛的应用。
要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
'''