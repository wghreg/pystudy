# -*- coding:utf-8 -*-
# pystudy

* base_type   基本数据类型
* encode      转码
* foreach     循环
* ifelse      条件判断
* input       输入
* tuple       不变集合类型
* collections 集合类型(list 列表、dict 字典、set集合)

* def_func    自定义函数
* recursive_func 递归函数(自引用)
* generator   生成器
* pointcute   切片
* range       列表生成式
* iterator    迭代器(generator)
* iterable    迭代(list, dict, tuple, str...)

* higher-order-function 高阶函数(函数为参数)
* map-reduce  map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
* filter      filter()接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
* do_sort     把源数据经过函数处理之后再排序

* anonymous_func 匿名函数
* do_decorator   装饰器
* do_return_func 返回函数
* partial_func   偏函数

`import queue` 与 `from multiprocess import Queue` 的区别
----
使用 `import 模块名`  是导入该模块，该模块下所有的方法都可以使用  使用规范： `模块名.方法名`  
`from 模块名 import 函数名`  是导入该模块下的特定的函数名，使用时直接使用函数名。
<pre>
eg:
    import math
    print(math.pi)

    from math import sqrt
    print（sqrt(2, 3)）
</pre>