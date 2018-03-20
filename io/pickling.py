#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等。'
'''
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
Python提供了pickle模块来实现序列化。

首先，我们尝试把一个对象序列化并写入文件：
'''
import pickle

d = dict(name="Bob", age=20, score=80)
print("将内容序列化:", pickle.dumps(d)) # pickle.dumps(obj) 序列化数据
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
print("将内容序列化后写入文件:pickle.dump(obj, file)")
f = open("D:\dump.txt", "wb")
pickle.dump(d, f)   # pickle.dumps(obj, file) 将序列化文件写入file-like Object
f.close()

f = open("D:\\dump.txt", "rb")
d = pickle.load(f)  # pickle.loads()反序列化出对象
f.close()
print("读取序列化文件-pickle.load(file_path):", d)
'''
这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。

Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

JSON

如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
JSON类型	Python类型
{}	        dict
[]	        list
"string"	str
1234.56	    int或float
true/false	True/False
null	    None
'''
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json
d = dict(name="Bob", age =20, score=80)
jsonstr = json.dumps(d)
print("\n对象转json(jsn.dumps(obj) 返回json格式):", jsonstr)
'''
dumps()方法返回一个str，内容就是标准的JSON。
类似的，dump()方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
'''
json_str = '{"name":"Bob", "age":20, "score":89}'
print(json.loads(json_str))
# JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换
'''
JSON进阶

Python的dict对象可以直接序列化为JSON的{}，很多时候，可以用class表示对象，
比如定义Student类，然后序列化：
'''
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student("Bob", 23, 90)
# print(json.dumps(s))  # TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable
'''
此时运行代码，会得到一个TypeError：
Traceback (most recent call last):
  ...
TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable

错误的原因是Student对象不是一个可序列化为JSON的对象。
仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
https://docs.python.org/3/library/json.html#json.dumps
这些可选参数来定制JSON序列化。
前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
'''
# 转换Student对象为json对象
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))
# 把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj:obj.__dict__))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class。
# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d["name"], d["age"], d["score"])
print(json.loads(json_str, object_hook=dict2student))   # 打印出的是反序列化的Student实例对象

'''
练习
    对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
'''
obj = dict(name="小明", age=30, score=99)
s1 = json.dumps(obj, ensure_ascii=True)
s2 = json.dumps(obj, ensure_ascii=False)
print("True:", s1, "\nFalse:", s2)

'''
小结

Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
json模块的dumps()和loads()函数是定义得非常好的接口的典范。
当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，
我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
'''
# 将json转为任意类json2obj(cls, jsonstr): cls 类对象，jsonstr json字符串
def json2obj(cls, jsonstr):
    jsonDict = json.loads(jsonstr)
    for key in jsonDict:
        setattr(cls, key, jsonDict[key])
    return cls
s = json2obj(Student, json_str)
print(s.name)