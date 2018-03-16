#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'多重继承'
'继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。'
class Animal(object):
    pass

'''
通过多重继承，一个子类就可以同时获得多个父类的所有功能。
回忆一下Animal类层次的设计，假设我们要实现以下4种动物：
    Dog - 狗狗；
    Bat - 蝙蝠；
    Parrot - 鹦鹉；
    Ostrich - 鸵鸟。

如果按照哺乳动物和鸟类归类，我们可以设计出这样的类的层次：
                ┌───────────────┐
                │    Animal     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │   Mammal    │           │    Bird     │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │   Bat   │  │ Parrot  │  │ Ostrich │
└─────────┘  └─────────┘  └─────────┘  └─────────┘


但是如果按照“能跑”和“能飞”来归类，我们就应该设计出这样的类的层次：
                ┌───────────────┐
                │    Animal     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │  Runnable   │           │   Flyable   │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │ Ostrich │  │ Parrot  │  │   Bat   │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
'''
# 要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def running(self):
        return "running....."
class Flyable(object):
    def fly(self):
        return "flying....."

class Mammal(Animal):
    pass
class Bird(Animal):
    pass

# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
# 狗
class Dog(Mammal, Runnable):
    pass
# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
# 蝙蝠
class Bat(Mammal, Flyable):
    pass

# 鸵鸟
class Ostrich(Bird, Runnable):
    pass
# 鹦鹉
class Parrot(Bird, Flyable):
    pass

'''
MixIn

在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
类似的，你还可以定义出肉食动物 CarnivorousMixIn 和植食动物 HerbivoresMixIn ，让某个动物同时拥有好几个MixIn：
'''
class CarnivoursMixIn(object):
    def eat(self):
        return "can eat meat"

class HerbivoresMixIn(object):
    def eat(self):
        return "can eat plant"

class Pig(Mammal, Runnable, CarnivoursMixIn):
    pass

'''
MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
Python自带的很多库也使用了MixIn。
比如 Python自带了 TCPServe r和 UDPServer 这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，
这两种模型由 ForkingMixIn 和 ThreadingMixIn 提供。通过组合，我们就可以创造出合适的服务来。

比如，编写一个多进程模式的TCP服务，定义如下：
class MyTCPServe(TCPServe, ForkingMixIn):
    pass

class MyUDPServe(UDPServe, ThreadingMixIn):
    pass

如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：

class MyTCPServer(TCPServer, CoroutineMixIn):
    pass
这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

小结

由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。

只允许单一继承的语言（如Java）不能使用MixIn的设计。


关于多重继承,其实,只要了解拓扑排序,就能很清楚的指导多重继承的查询顺序了,从入度为0的位置起,剪掉入度为0相关边,然后接着找下一个入度为0的位置,如此往复到最后,遇到有多个入度为0的时候,按最左原则取就行了,大体上就是这样了

有兴趣的话,可以去看看我做的关于这个的笔记,应该能了解一点

python多重继承之拓扑排序[https://kevinguo.me/2018/01/19/python-topological-sorting/]

mro,解析方法调用的顺序

什么是拓扑排序：
    从DAG途中选择一个没有前驱(即入度为0)的顶点并输出
    从图中删除该顶点和所有以它为起点的有向边。
    重复1和2直到当前DAG图为空或当前途中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环。

python多重继承：
    把继承关系先构成一张图
    利用拓扑排序的方法输出拓扑顺序，并列关系时遵循取最左原则
    python继承顺序遵循C3算法，只要在一个地方找到了所需的内容，就不再继续查找

遵循多态定义，子类和父类有相同的方法时，子类覆盖父类的方法，输出子类方法。
'''

'''
1.有两个基类A和B,A和B都定义了方法f(),C继承A和B,那么调用C的f()方法时会出现不确定。
2.有一个基类A，定义了方法f()，B类和C类继承了A类（的f()方法），D类继承了B和C类，那么出现一个问题，D不知道应该继承B的f()方法还是C的f()方法
'''
#1.
class A(object):
    def f(self):
        print("A")

class B(object):
    def f(self):
        print("B")

class C(B,A):
    pass
c = C()
c.f()   #会输出什么?"A" or "B"   --> B
#结论:输出什么的决定性因素是C在继承父类时的顺序! 即靠近左边的先输出!

#2.
class A2(object):
    def f(self):
        print("A")

class B2(A2):
    def f(self):
        print("AB")

class C2(A2):
    def f(self):
        print("CB")

class D2(B2,C2):
    pass

d = D2()
d.f() #输出AB. B2.f() 会覆盖A2.f() 子类覆盖父类