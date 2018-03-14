#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
    定义函数时，需要确定函数名和参数个数；

    如果有必要，可以先对参数的数据类型做检查；

    函数体内部可以用return随时返回函数结果；

    函数执行完毕也没有return语句时，自动return None。

    函数可以同时返回多个值，但其实就是一个tuple。
'''
#######################################################################################################
''' Python 内置函数 '''
# abs()有且只有一个参数，多个参数或类型不对都会报错
print(abs(10))
print(abs(-11))
print(abs(12.34))

a = abs
print(a(-123.0))

# min() , max() 可多个参数
print(min(1,2,5,-3,9))
print(max(1,2,5,-3,9))

# int()函数可以把其他数据类型转换为整数
print(int('123'))
print(int(12.34))   # int()转浮点数时只获取整数部分，忽略小数；并且不支持转字符串类型的小数(会报错)
# float()
print(float('12.34'))
# str()
print(str(10.0))
# boolean 
print(bool(1))  # True
print(bool('')) # True
print(bool('1'))# Flase

# hex() 转16进制
print(hex(1))
print(hex(16))
print(hex(17))
print(hex(100))
print(hex(255))
#######################################################################################################

# Python中，定义一个函数要使用def语句，依次是函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
# 格式：def function_name([args]):
''' 请注意:
函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。
'''
print("\n自定义函数使用def关键字：")
def my_abss(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abss(100))
print(my_abss(-10.01))

# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，
# 那么，可以在该文件的当前目录下启动Python解释器，
# 用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：
print("\nfrom py_file_name import my_function_name:")
from test_abs import my_abs
print(my_abs(-90)) 

# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass

# 例子：
age = 20
if age >=18:
    pass
else:
    age=18

'''
参数检查

调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError。
但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别就知道。
当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
'''
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type!")
    if x>=0:
        return x
    else:
        return -x
# 添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误

'''
返回多个值

函数可以返回多个值吗？答案是肯定的。
比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标:
'''
import math
def move(x, y, step, angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi/6)
print(x, y)
# 其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi/6)
print(r)
# 返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

def quadratic(a, b, c):
    if not isinstance(a, int) & isinstance(b, int) & isinstance(c, int):
        return TypeError("参数不是数字类型！")

    if a==0:
        if b ==0:
            return False
    else:
        if (b*b - 4*a*c) >= 0:
            r1 = (-b + math.sqrt(b*b - 4*a*c))/2*a
            r2 = (-b - math.sqrt(b*b - 4*a*c))/2*a
            return r1, r2
        else:
            return "没有实数解"

print(quadratic(1, 3, -4))
print(quadratic(2,3,1))

print(math.pow(2,5)) # 2的5次方

def power(x, n):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s
print(power(3,3))

''' 可变参数 '''
print("\n*nums 表示把nums的所有元素作为可变参数处理:")
# *nums 表示把nums的所有元素作为可变参数处理
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calc(1,2,3))

nums = [2,3,4]
print(calc(*nums))

''' 关键字参数 '''
def person(name, age, **kw):
    print('name:', name, ', age:', age, ', other:', kw)
person('Bob', 23, city="北京")
person("Jack", 34, city='上海', job ='IT')

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
extra = {'city':'北京', 'job':'IT'}
person('lisi', 30, city=extra['city'], job=extra['job'])
person('lisi', 30, **extra)

''' 命名关键字参数 '''
def person2(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'others:', kw)
person2('张三', 40, city='beijing', addr='大屯路甲一号', zipcode='123456')

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person3(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)
person3('李四', 32, city='深圳', job='Engineer')

# 命名关键字参数city具有默认值，调用时，可不传入city参数
def person4(name, age, *, city='beijing', job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)
person4('李四', 32, job='Engineer')
'''
使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass
'''

''' 参数组合 '''
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

print("\n练习：")
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# 使用可变参数 *args
def test(*numbers):
    sum = 0
    for nums in numbers:
        sum = sum + nums*nums
    return sum
print(test(2,3,4))

'''
小结
    Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
    默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

    要注意定义可变参数和关键字参数的语法：
        *args是可变参数，args接收的是一个tuple；
        **kw是关键字参数，kw接收的是一个dict。

    以及调用函数时如何传入可变参数和关键字参数的语法：
        可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
        关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

    使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

    命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

    定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''