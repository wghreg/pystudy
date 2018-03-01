#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改!
# 没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，
# 可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
classmates = ("张三", "李四", "王武")

# 如果要定义一个空的tuple，可以写成(), 长度为0
t = ()
print(t)
print(len(t))

# 要定义一个只有1个元素的tuple, 例如t = (1)。
t = (1)
print(t)
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，
# 这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：t = (1,)
t=(1,)
print(t)

# “可变的”tuple. 
# tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
t = ("a", "b", ["A", "B"], "c")
print(t)
t[2][0] = "X"
t[2][1] = "Y"
print(t)

# 练习
print("\n练习：")
L = [["Apple", "Google", "MS"], ["Java", "Python", "PHP", "Node"], ["张三", "李四", "王武"]]
print(L[0][0])
print(L[1][1])
print(L[2][2])