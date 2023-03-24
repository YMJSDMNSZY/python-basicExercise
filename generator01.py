# -*- coding=utf-8 -*-

'''
通过列表生成式(列表推导式，我们可以直接创建一个列表。但是,受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元紊的列表，不仅占用很大的存储空间,
如果我们仅仅需要访问前面几个元素，那后面绝大多数元紊占用的空间都白白浪费了。
所以，如果列表元亲可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢?
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器: generator.

得到生成器的几种方式：
1.通过列表推导式生成生成器
    g=(x+1 for x in range(6))
2.借助函数完成
    def +yield



yield是一个关键字，用于在Python中定义生成器函数。生成器函数返回一个生成器对象，可以用于逐步生成序列或迭代器。
yield的使用场景包括：


生成器函数：使用yield定义生成器函数，可以逐步生成序列或迭代器，而不是一次性生成一整个序列，这可以节省内存占用，并且可以在处理大量数据时提高性能。

协程：yield可以用于协程的实现，协程是一种轻量级的线程，可以在单线程中实现并发操作，提高程序的执行效率。

延迟计算：yield可以用于延迟计算，在需要时才生成数据，可以节省计算资源。

无限序列：使用yield可以定义无限序列，只有在需要时才生成序列中的元素。

交替迭代器：使用yield可以定义交替迭代器，可以交替遍历多个序列。

递归生成器：使用yield可以定义递归生成器，可以生成无限嵌套的数据结构，例如树形结构。
总之，yield可以用于实现各种复杂的数据结构和算法，提高程序的灵活性和可维护性。


'''

# [x for x in range(100000000)]
newlist1=[x*3 for x in range(20)]#方括号是列表推导式的形式  type为list
print(type(newlist1))


g=(x*5 for x in range(10))#就是一个generator空间
print(type(g))
print(g)

#方式一：用__next__()方式得到元素
print(g.__next__())
#方式二：next() 内置函数  每调一次会产生一个元素
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))#StopInteration 生成器本来就可以产生10个，调用完后，再次调用就会产生这个异常

