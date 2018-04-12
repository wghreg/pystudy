#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''

通过哈希算法，我们可以验证一段数据是否有效，方法就是对比该数据的哈希值，
例如，判断用户口令是否正确，我们用保存在数据库中的password_md5对比计算md5(password)的结果，如果一致，用户输入的口令就是正确的。

为了防止黑客通过彩虹表根据哈希值反推原始口令，在计算哈希的时候，不能仅针对原始输入计算，
需要增加一个salt来使得相同的输入也能得到不同的哈希，这样，大大增加了黑客破解的难度。
如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。
但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不同口令计算出不同的哈希。
要验证哈希值，必须同时提供正确的口令。

这实际上就是Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

Python自带的hmac模块实现了标准的Hmac算法。我们来看看如何使用hmac实现带key的哈希。
我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下：
'''
import hmac
message = b"Hello, world!"
key = b"secret"
h = hmac.new(key, message, digestmod="MD5")
print("hmac(key, message, digestmod=指定算法md5, sha1等):", h.hexdigest())
'''
Traceback (most recent call last):
  File "use_hmac.py", line 26, in <module>
    print("练习：", hmac.new("123456", "my-key", digestmod="sha512").hexdigest())
  File "D:\Program Files\Python36\lib\hmac.py", line 144, in new
    return HMAC(key, msg, digestmod)
  File "D:\Program Files\Python36\lib\hmac.py", line 42, in __init__
    raise TypeError("key: expected bytes or bytearray, but got %r" % type(key).__name__)
TypeError: key: expected bytes or bytearray, but got 'str
'''
# key, message 必须是byte类型
print("练习：", hmac.new(b"123456", b"my-key", digestmod="sha512").hexdigest())
# 可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。
# 需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
'''
练习
    将上一节的salt改为标准的hmac算法，验证用户口令：
'''
import hmac, random, operator
'''
h = hmac.new(key=byte, message=byte, digestmode="SHA512")
h.hexdigest()
'''
def get_hmac(key, s, algorithm):
    return hmac.new(key.encode("utf-8"), s.encode("utf-8"), algorithm).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = "".join([chr(random.randint(48,122)) for i in range(20)])
        print("username =", username, ", password =", password, ", key =", self.key)
        self.password = get_hmac(self.key, password, "MD5")
db = {
    "张三": User("张三", "123456"),
    "李四": User("李四", "abc999"),
    "赵六": User("赵六", "alice2008")
}

def login(username, password):
    user = db[username]
    print(user.key, operator.eq( user.password, get_hmac(user.key, password, "MD5")) )
    return user.password == get_hmac(user.key, password, "MD5")

# 测试:
assert login('张三', '123456')
assert login('李四', 'abc999')
assert login('赵六', 'alice2008')
assert not login('张三', '1234567')
assert not login('李四', '123456')
assert not login('赵六', 'Alice2008')
print('ok')
'''
小结
Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，
使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。
'''