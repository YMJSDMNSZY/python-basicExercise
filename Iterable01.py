# -*- coding=utf-8 -*-
'''
在Python中，迭代器（iterator）是一个可以遍历访问序列中各个元素的对象，
它可以被for循环等语句所调用，每次返回序列中的一个元素。迭代器可以用来处理大型数据集
，因为它只在需要时生成数据，而不是一次性生成所有数据，从而节省内存和计算资源。
迭代器的基本特点如下：


可迭代对象（iterable）：可以返回一个迭代器的对象，例如列表、元组、集合等。

迭代器对象（iterator）：可以返回一个值的对象，例如列表、元组、集合等。

iter()方法：可迭代对象必须实现的方法，返回一个迭代器对象。

next()方法：迭代器对象必须实现的方法，返回迭代器中的下一项。
下面是一个使用迭代器遍历列表的例子：

lst = ['apple', 'banana', 'orange']
it = iter(lst)  # 返回一个迭代器对象
print(next(it))  # 输出apple
print(next(it))  # 输出banana
print(next(it))  # 输出orange

需要注意的是，在迭代器中调用next()方法时，如果到达了序列的末尾，
则会抛出StopIteration异常。因此，在使用迭代器时通常会使用for循环来避免这种异常，例如：

lst = ['apple', 'banana', 'orange']
for item in lst:
    print(item)

除了列表、元组、集合等内置数据类型，我们还可以自定义实现迭代器，例如：

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        value = self.start
        self.start += 1
        return value
mr = MyRange(1, 5)
for i in mr:
    print(i)

上面的代码定义了一个MyRange类，它实现了__iter__()和__next__()方法，并通过for循环遍历了该迭代器对象。

'''

#可迭代的对象：1.生成器 2.元组 列表 字典 集合 字符串
#迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。
#迭代器对象从集合的第一个元素开始访问，直到所有的元素均被访问完成
#迭代器只能往前不会往后
#可以被  next() 函数调用并不断返回下一个值的对象称为迭代器：Iterator

#生成器是可迭代的，同样也是迭代器
#list是可迭代的，但不是迭代器  print(next())会报错  可以通过iter()函数将列表变成迭代器

#如何判断一个对象是否可迭代

from collections.abc import Iterable

list=[2,3,4,5,6,8,8]
list1=iter(list)

# f= isinstance(list1,Iterable)
# print(f)
print(next(list1))

g=(x+1 for x in range(10))
f=isinstance(g,Iterable)
print(f)
print(next(g))