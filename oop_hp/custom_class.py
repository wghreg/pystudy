#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'定制类'
'''
看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

1. __str__
'''
print("1. __str__ & __repr__:")
class Student(object):
    def __init__(self, name):
        self.name = name
# print(Student("Michial"))   # <__main__.Student object at 0x00000000027CA240>
    def __str__(self):
        return "Student Object (name:%s)" % self.name
print(Student("Michial"))   # 好看，而且容易看出实例内部重要的数据。

s = Student("Michial")
print(s)

'''
直接敲变量不用print，打印出来的实例还是不好看：
    >>> s = Student('Michael')
    >>> s   # <__main__.Student object at 0x109afb310>

这是因为直接显示变量调用的不是__str__()，而是__repr__()，
两者区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，即__repr__()是为调试服务的。

解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
'''
class Person(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Person Object (name： %s)" % self.name
    __repr__ = __str__

p = Person("ABC")
print(p)
p 

'''
2. __iter__

如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
'''
print("\n2. __iter__:")
class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1    # # 初始化两个计数器a，b

    def __iter__(self):
        return self             # 实例本身就是迭代对象，故返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a +self.b # 计算下一个值
        if self.a > 60:        # 退出循环的条件
            raise StopIteration()
        return self.a           # 返回下一个值
print("type(Fib()): ", type(Fib()))     # <class '__main__.Fib'>
print("list(Fib())：", list(Fib()))     # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print("tuple(Fib())：", tuple(Fib()))   # (1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
for n in Fib():
    print(n)

'''
3. __getitem__
Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
    >>> Fib()[5]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'Fib' object does not support indexing
要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
'''
print("\n3. __getitem__:")
class Fib2(object):
    def __getitem__(self, n=10):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib2()
print(f[0])
print(f[1])
print(f[2])
print(f[10])
# list有个神奇的切片方法：
print(list(range(100))[5:10])   # [5, 6, 7, 8, 9]
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
print("判断参数类型：")
class Fib3(object):
    def __getitem__(self, n):
        if isinstance(n, int):      # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):    # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fib3()
print(f[0:5])       # [1, 1, 2, 3, 5]
'''
但是没有对step参数作处理：print(f[:10:2])  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
最后，还有一个__delitem__()方法，用于删除某个元素。

总之，通过上面的方法，自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


4. __getattr__
正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
    class Student(object):
        def __init__(self):
            self.name = 'Michael'

调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
    >>> s = Student()
    >>> print(s.name)
    Michael
    >>> print(s.score)
    Traceback (most recent call last):
    ...
    AttributeError: 'Student' object has no attribute 'score'

错误信息很清楚地告诉我们，没有找到score这个attribute。
要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，
那就是写一个__getattr__()方法，动态返回一个属性或函数。修改如下：
'''
print("\n4. __getattr__:")
class Student2(object):
    def __init__(self):
        self.name = "Michael"

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        elif attr=='age':
            return lambda:25
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
s2 = Student2()
print("{'name':'%s', 'age':%d, 'score':%d}" % (s2.name, s2.age(), s2.score))
print("调用不存在的属性或者__getattr__中没有定义的属性或方法时，默认返回：", s2.abc)
'''
此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：

class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

举个例子：

现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
    http://api.server/user/friends
    http://api.server/user/timeline/list

如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的__getattr__，我们可以写出一个链式调用：
'''
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s'%(self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
    __call__ = __getattr__

print("\n利用完全动态的__getattr__写出一个链式调用：", Chain().status.user.timeline.list)
print(Chain().users("Michael").repos)   # 仅仅添加 __call__ = __getattr__ 就能实现将实际用户名转换到url中
'''
无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！

还有些REST API会把参数放到URL中，比如GitHub的API： GET /users/:user/repos
调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
print(Chain().users("Michael").repos)
# TODO
就可以非常方便地调用API了, 可以试试写出来!
'''
class Chain2(object):
    def __init__(self,path=""):
        self._path=path
    def __getattr__(self,path):
        return Chain("%s/%s"%(self._path,path))
    def __call__(self,path):
        return Chain("%s/%s"%(self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain2().a.b.user("ChenTian").c.d)
'''
代码输出为 : /a/b/user/ChenTian/c/d
首先定义了Chain类，init函数接收一个path变量。
然后getattr函数，这个函数是如果你使用了类没有定义的变量的时候，就会调用它。它返回一个Chain()，并且把“原本的path/没有定义的变量”作为path的值传入了Chain里
call函数就是将类当作类似函数一样调用,  str函数是当有打印函数是，就会调用这个
所以这段代码的执行流程为：
先是Chain()创建了一个实例，最开始的path默认为“”，然后.a，因为没有a这个变量，所以会调用getattr函数，返回一个Chain实例，然后把/a作为path传入，
继续.b，因为没有b变量，所以执行getattr函数，将/a/b作为path传入，
然后.user(“ChenTian”)，先会执行getattr返回Chain实例，但是因为有()括号在，所以返回的是Chain()，这个就会调用call函数了，
然后把“ChenTian”作为path传入，然后call函数就返回了/a/b/user/ChenTian，剩下的类同。

主要是user(“ChenTian”)这一句，我的理解是，先执行了getattr，然后执行call，并把ChenTian作为path传入
具体的细节我目前不是很清楚，我猜测是多了括号所以会调用call，不过不知道为什么。。。
因为user("ChenTian")调用了实例对象中不存在的方法, 会默认执行call
'''
'''
5. __call__

一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
'''
print("\n5. __call__:")
class Student5(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print("My name is %s." % self.name)

s5 = Student5("Student5")
s5()        # My name is Student5.
'''
__call__()还可以定义参数。
对实例进行直接调用就好比对一个函数进行调用一样，
所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，
因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

那么，怎么判断一个变量是对象还是函数呢？
其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
比如函数和我们上面定义的带有__call__()的类实例：
'''
print(callable(Student5("ABC")))    # True
print(callable(max))                # True
print(callable([1,2,3]))            # False
print(callable(None))               # False
print(callable("str"))              # False
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。