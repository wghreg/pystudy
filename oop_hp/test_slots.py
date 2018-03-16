#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class Student(object):
    pass

def set_age(self, age):
    self.age = age

def set_name(self, name):
    self.name = name

from types import MethodType
# 绑定到实例对象上的方法
s = Student()
s.set_age = MethodType(set_age, s)
s.set_age(30)
print(s.age)
s.set_name = MethodType(set_name, s)
s.set_name("Test")
print(s.name)
''' 绑定到实例对象上的方法，只能用在实例上。别的实例需要重新绑定
s2 = Student()
print(s2.age)

解决方式是把方法绑定到class上， 这样每次生成实例都会把方法复制下来
'''
Student.set_name = MethodType(set_name, Student)
Student.set_age = MethodType(set_age, Student)

s3 = Student()
s3.set_name("Test3")
s3.set_age("33")
print(s3.name, s3.age)
s4 = Student()
s4.set_name("Test4")
s4.set_age(44)
print(s4.name, s4.age)

# 如果只允许给class绑定指定的属性时，可以使用__slots__ = ("name", "age") tuple类型限制
class Person(object):
    __slots__ = ("name", "age")

# 绑定属性
pt = Person()
pt.name = "pTest"
pt.age = 20
print("\n使用__slots__限制类的属性：", pt.name, pt.age)
# pt.score = 80     # AttributeError: 'Person' object has no attribute 'score'
# print(pt.score)

# 绑定方法
def set_person_name(self, name):
    self.name = name

def set_person_age(self, age):
    self.age = age

def set_person_score(self, score):
    self.score = score

Person.set_person_name = MethodType(set_person_name, Person)
Person.set_person_age = MethodType(set_person_age, Person)
p = Person()
p.set_person_name("Person")
p.set_person_age(10)
print("\nMethodType为class绑定方法：", p.name, p.age)

Person.set_person_score = MethodType(set_person_score, Person)
p.set_person_score(90)
print("set_score = ", p.score)
'''
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的,
除非在子类中也定义__slots__
'''
class PersonItem(Person):
    pass
pi = PersonItem()
pi.name = "PItem"
print(pi.name)  # PItem
pi.score = 88
print(pi.score) # 88  父类的__slots__限制对子类不起作用，除非子类定义自己的__slots__。

class PII(Person):
    __slots__=("score")

pii = PII()
pii.score = 89
print(pii.score)
'''
pii.name = "pii" # AttributeError: 'PII' object attribute 'name' is read-only
pii.age = 28
print(pii.name, pii.age, pii.score)
'''

class Code(object):
    __slots__ = ("name", "age", "funct_age") # age属性在funct_age中被赋值， 在slots中也要定义，否则获取不到属性

def funct_age(self, age):
    self.age = age

c = Code()
c.name = "abc"
c.funct_age = MethodType(funct_age, c)
c.funct_age(22)
print(c.name, c.age)

'''
    class Student(object):
        pass
    s = Student()
    s.age = 18
    print(s.age)

    def set_age(self,age):
        self.age = age 

    s.set_age = set_age
    s.set_age(s,25)
    print(s.age)

    #18
    25
[Finished in 0.2s]

Created at 4天前, Last updated at 4天前
加在类上的时候是有区别的，因为MethodType将set_age方法绑定到Stu类，并不是将这个方法直接写到Stu类内部，
而是在Stu内存中创建一个link指向外部的方法，在创建Stu实例的时候这个link也会被复制。

    from types import MethodType 
    class Student(object):
        pass

    def set_age(self,age):
        self.age=age

    Student.set_age=MethodType(set_age,Student)

    s1=Student()
    s1.set_age(15)

    s2=Student()
    s2.set_age(20)

    print(s1.age)


施瓦辛格号航空母舰 created at 2-9 23:09, Last updated at 4天前
    class Student(object):
        pass

    def set_age(self, age): # 定义一个函数作为实例方法
        self.age = age

    s=Student()
    s.set_age=set_age
    s.set_age(25)
这样是不行的，得到错误。提示还缺少一个age参数，说明输入的25被当成self参数。
因此，在给类(Class)进行绑定时才能直接用Student.set_age=set_age的方式，而给实例进行绑定则要使用s.set_age = MethodType(set_age, s)的方式。

Created at 2-28 18:15, Last updated at 2-28 18:15
    在给类(Class)进行绑定时才能直接用Student.set_age=set_age的方式，也可以用Student.set_age = MethodType(set_age, Student)

Created at 4天前, Last updated at 4天前
    s.set_age(s,25)


还是有点糊涂,__slots__也限制方法绑定吗
一只女人三个猫喵 created at 5天前, Last updated at 5天前
    class People(object):
        __slots__=('name','score')

    def set_age(self):
        print('My age is 18')

    p=People()
    p.name='Wang'
    p.score=90
    from types import MethodType
    p.set_age=MethodType(set_age,p) #这样错误，why？

    People.set_age=set_age          #这样就可以
    p.set_age(23)

Created at 5天前, Last updated at 5天前
    限制该 class 实例能添加的属性

    方法也是属性


设定限制属性后，实例不能动态添加方法的问题
我有疫苗 created at 2-17 21:28, Last updated at 3-6 15:55
    #类的定义
    class Teacher(object):
        slots = ('name','age')

    #函数的定义
    def printStr(self):
        print("好好学习")
    t = Teacher()
    t.printStr = MethodType(printStr, t)

#为什么报这个错误，不明白求解答
    AttributeError: 'Teacher' object has no attribute 'printStr'

Created at 2-22 21:00, Last updated at 2-22 21:00
    slot未限制方法

Created at 2-23 14:35, Last updated at 2-23 14:35
    slots=('name','age','printStr')

Created at 2-23 16:05, Last updated at 2-23 16:05
    我觉得你没加这一句吧： from types import MethodType


Created at 2-24 15:44, Last updated at 2-24 15:44
    我认为是，因为已经限制了t（实例）的属性，所以在执行 t.printStr = MetthodType(printStr,t) 语句中，等号左边就编译通不过了，
    你换成Teacher类里面指定的属性，比如t.name = MetthodType(printStr,t)，就能通过了

Created at 2-24 15:48, Last updated at 2-24 15:48
    我想了想，觉得应该是 t.printStr = MethodType(printStr, t)
    等号右边是绑定方法，等号左边是赋值的变量，也就是把绑定的方法赋值给了变量t.printStr
    左边的变量可以是其他数值（你设置的变量为printStr），比如可以写成 k = MethodType(printStr, t)
    这是给class添加的方法，实例化的时候，不管创建几个实例，t1，t2，t3
    这些实例都用class动态添加的方法k, 打印print (k()) 都会输出绑定的class方法‘好好学习’。
    后面打印print (t.printStr)的时候，输出的是t的属性attrbute “printStr”. 但是这个属性并没有被创建。所以会报错

Created at 2-24 15:51, Last updated at 2-24 15:51
    上面回复更正下，class方法应该是k = MethodType(printStr, Teacher)#(方法，类) # 实例绑定对应为（方法/属性，实例）


Created at 2-28 21:35, Last updated at 2-28 21:35
    t.printster = MethodType(printstr, t)这里有问题吧，
    t 是类Teacher的一个实例，而类Teacher中并未定义printstr这个函数，所以不可以通过实例t调用函数printstr。可以改为：
    t1 = MethodType(printstr, t)
    print(t1())

Created at 3-6 15:55, Last updated at 3-6 15:55
    限制属性后，实例可以动态添加方法，就是这个方法中涉及的属性只能是限制的那几个属性，如果有其他属性调用时也会出错。
    动态绑定的方法也不能用s.set_score=MethodType(set_score,s1),因为python会将set_score认为是一个属性，而不是方法。
    可以直接用a=MethodType(set_score,s1)。但因为score本身不在限制的两个属性内，所以调用时也会报错。

    class Student(object):
        slots=('name','age')# 用tuple定义允许绑定的属性名称
    s1=Student()
    绑定属性name和age
    s1.name='lily'
    s1.age=18
    print(s1.name,'\n',s1.age)

    s1.score=99   ##AttributeError: 'Student' object has no attribute 'score'
    由于'score'没有被放到slots中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
    用以上上述两种方法对实例绑定方法

    def set_score(self,score):##定义set_score方法
        self.score=score
方法一
    s1.set_score=set_score  #AttributeError: 'Student' object has no attribute 'set_score'
    s1.set_score(s1,98)     #调用s1的set_score方法
方法二
    from types import MethodType
    s1.set_score= MethodType(set_score,s1) #AttributeError: 'Student' object has no attribute 'set_score'
方法三：直接将函数赋值给a,然后再调用
    a=MethodType(set_score,s1)
    a(99)   #AttributeError: 'Student' object has no attribute 'score'
上述两种方法均不可以，因为python会将set_score看成属性而不是方法，直接用a=MethodType(set_score,s1)就可以了。
但是底下调用时还是会出错。因为这个类中是没有score属性的。
因此重新写了个reset_age的函数，因为这个类中有age这个属性，所以调用不会出错

    def reset_age(self,age):    #定义set_score方法
        self.age=age
    from types import MethodType
    a=MethodType(reset_age,s1)
    a(21)
    print(type(a))
    print(s1.age)

杀生丸6142509806 created at 2-24 15:01, Last updated at 2-24 15:01
    #A 加限制实例属性，类方法用MethodType绑定
    class Student1(object):
        slots = ('name', 'age')#指定实例可用的属性
    s1 = Student1()#实例化
    s2 = Student1()
    s1.name = 'zhangsan'#动态绑定属性
    s2.age = 'lisi'#动态绑定属性
    def set_info(self, m, n):
        self.height = m
        self.weight = n
    from types import MethodType
    Student1.set_info = MethodType(set_info, Student1)#给类绑定方法并赋值给class.set_info
    s1.set_info('175cm', '65kg')#调用方法
    s2.set_info('180cm', '80kg')
    print (s1.name, s2.age)
    print (s1.height, s2.weight)

    #B 不加实例属性限制slots，类方法不用MethodType绑定
    class Student2(object):
        pass
    s3 = Student2()
    s4 = Student2()
    s3.name = 'zhangsan'
    s4.age = 'lisi'

    #动态绑定方法
    def new_info(self, x, y):
        self.height = x
        self.weight = y
        return ('%s, %s') % (x, y)
    Student2.new_info = new_info
    s3.new_info('175cm', '65kg')
    s4.new_info('180cm', '80kg')
    print (s3.name, s4.age)
    print (s3.height, s4.weight)

    #C 加实例属性限制，类方法不用MethodType绑定
    class Student3(object):
        slots = ('name', 'age')
    s5 = Student3()
    s6 = Student3()
    s5.name = 'zhangsan'
    s6.age = 'lisi'
    def creat_info(self, z, t):
        self.height = z
        self.weight = t
        return '%s, %s' % (z, t)
    Student3.creat_info = creat_info
    s5.creat_info('175cm', '65kg')
    s6.creat_info('180cm', '80kg')
    print (s5.name, s6.age)
    print (s5.weight, s6.height)
    报错

总结 加slots 实例属性限制后，给类绑定方法要用MethodType

萌坏w created at 2-5 20:30, Last updated at 2-12 6:01
from types import MethodType

    class Student():
        __slots__ = ('name', 'age', 'grade')
        pass

    class Pupil(Student):
        pass

    def grade(self):
        print('测试测试测试')

    s = Student()
    s.name = 'Pig'
    s.age = 6
    # s.wtf = 123
    s.grade = MethodType(grade, s) # 方法动态绑定给实例
    s.grade()
    p = Pupil()
    p.wtf = 666 # 子类不会继承__slots__
继承关系，子类定义了slots，父类也必须定义，哪怕是空的。


Created at 2-12 6:01, Last updated at 2-12 6:01
父类可以不定义

__slots__ 指对class的实例限制，对class动态绑定属性方法不限制
杀生丸6142509806 created at 2-8 15:12, Last updated at 2-8 15:12
    class Student(object):
        slots = ('name', 'score')
    s1 = Student()
    s2 = Student()
    from types import MethodType
    def set_age(self, t):
        self.age = t
    Student.set_age = MethodType(set_age, Student)
    Student.set_age(20)
    print (s1.age)#20
    print (s2.age)#20

slots 指对class的实例限制，对class动态绑定属性方法不限制

属性方法傻傻分不清
我依然798-999 created at 2-5 21:20, Last updated at 2-5 21:24
    class Code(object):
        pass

    def s_name(self,name):
        self.nam = name

    h = Code()
    from types import MethodType
    h.s_name = MethodType(s_name,h)
    h.s_name('suy') 
    h.nam

    'suy'


Sunvvew created at 1-25 15:43, Last updated at 2-2 13:07
在给实例绑定方法的时候用到的MethodType函数是具体什么作用呢? 

s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
MethodType方法把set_age方法与实例s绑定，同时把set_age方法名字也设置为set_age

白骨堆起江山
Created at 2-2 13:07, Last updated at 2-2 13:07
个人理解:
MethodType(set_age, s) #意思是：把set_age方法转换成s类型的
s.set_age #定义一个对象属性，把转换过来的set_age，赋值给它（变量名随意写，也可定义成s.update_age）
调用：s.update_age()或s.set_age(),看你怎么定义了
'''