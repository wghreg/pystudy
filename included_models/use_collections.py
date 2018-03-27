#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import namedtuple
Point = namedtuple("Point", ['x','y'])
p = Point(1,2)
print("namedtuple:", p.x,",", p.y)
'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

可以验证创建的Point对象是tuple的一种子类：
'''
print(isinstance(p, Point))
print(isinstance(p, tuple))
# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
Circle = namedtuple("Circle",['x','y','z'])

'''
deque
    使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
from collections import deque
q = deque(['a', 'b', 'c'])
q.append("x")
q.appendleft("y")
print("\ndeque:", q)
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

'''
defaultdict
    使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
'''
from collections import defaultdict
dd = defaultdict(lambda:"N/A")
dd["key1"] = "abc"
print("\ndefaultdict:\n",dd["key1"])
print(dd["key2"])
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

'''
OrderedDict
    使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：
'''
from collections import OrderedDict
d = dict([("a", 1),('b',2),('c',3)])
print("\nOrderedDict:\n无序 dict=",d)    # dict的Key是无序的
od = OrderedDict([("a", 1),('b',2),('c',3)])
print("有序 OrderedDict=",od)   # OrderedDict的Key是有序的
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = OrderedDict()
od['x'] = 1
od['y'] = 2
od['z'] = 3
print("OrderedDict按照插入顺序排序，不是key的排序：", list(od.keys()))
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
# from collections import OrderedDict
class LastUpdateedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey =1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print("remove:", last)
        if containsKey:
            del self[key]
            print("set:", (key, value))
        else:
            print("add:", (key, value))
        OrderedDict.__setitem__(self, key, value)
'''
if len(self) - containsKey >= self._capacity:大于号完全没有必要改成 if len(self) = self._capcity and containsKey == 0:就可以了
这样设置永远不会有len(self)大于容量的时候，因为当他等于容量的时候后面的代码就会开始清除容量内容了，
里面有的key就用del删除该key和它的value并且用__setitem__方法在字典最后重新放一个key并赋值value，里面没有就用ordereddict的popitem(Last=False)方法删除最前面的key和它的value。
'''

'''
Counter
    Counter是一个简单的计数器，例如，统计字符出现的个数：
'''
from collections import Counter
c = Counter()
for ch in "programming":
    c[ch] = c[ch]+1
print("\nCounter:\n", c)

#Counter实际上也是dict的一个子类
c=Counter('abscsdsd') 
print(c)
#Counter({'s': 3, 'd': 2, 'a': 1, 'b': 1, 'c': 1})
#取最多的前3项：
from collections import Counter
c=Counter('abscsdsd').most_common(3)
print(c)
#[('s', 3), ('d', 2), ('a', 1)]
# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。
'''
补充几个地方：

1. Counter 类可以直接调用其构造方法，传入要统计的字符串：

>>> Counter('programming')
Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})

>>> dict(Counter('programming'))
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
2. 自己实现一个可以统计的 dict，最简单的做法是重写 __mission__ 方法：

class Counter(dict):
    def __missing__(self, key):
        return 0

c = Counter()
for ch in "hello world!":
    c[ch] += 1

print(c)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
'''