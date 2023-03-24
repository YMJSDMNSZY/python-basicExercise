# -*- coding=utf-8 -*-
#


'''
map() 函数是 Python 内置的一个高阶函数，它可以对一个可迭代对象中的每个元素应用一个函数，
然后返回一个新的可迭代对象，其中包含了所有经过函数处理过的元素。map(function, iterable, ...)
其中，function 是一个函数，可以是 Python 内置函数，也可以是自定义函数；iterable 是一个可迭代对象，
比如列表、元组、集合等。
可以有多个 iterable 参数，如果有多个，则 map() 函数会以其中最短的那个为准，多余的元素会被忽略。

lst = [1, 2, 3, 4, 5]
squared_lst = map(lambda x: x**2, lst)
print(list(squared_lst))  # 输出：[1, 4, 9, 16, 25]
在上面的代码中，map() 函数将列表 lst 中的所有元素依次传入匿名函数 lambda x: x**2 中进行平方运算，
然后返回一个新的可迭代对象 squared_lst，其中包含了所有平方后的元素。
最后，通过 list() 函数将 squared_lst 转换为列表并输出。


'''
# list1=[1,2,3,4,5,5,6,2]
#
# result=map(lambda x:x+2,list1)
# print(list(result))
#
#
# result1=map(lambda x:x if x%2==0 else x+1,list1)
# print(list(result1))
#
# #和上面的匿名函数功能一样
# for index,i in enumerate(list1):
#     if i%2!=0:
#         list1[index]=i+1
#
# print(list1)



'''
reduce() 函数是 Python 内置的一个高阶函数，它可以对一个列表、元组等可迭代对象中的所有元素进行累积操作。
而在 reduce() 函数中，可以使用匿名函数（lambda函数）作为参数，来对可迭代对象进行自定义的累积操作。
其中，参数可以是任意个数，表达式是匿名函数的主体部分。匿名函数的返回值就是这个表达式的结果。
'''


from functools import reduce

# tuple1=(2,23,4,3,43,43,5,87,5,6,5)
#
# result=reduce(lambda x,y:x+y,tuple1)
#
# print(result)
#
# tuple2=(1,2)
# result1=reduce(lambda x,y:x*y,tuple2,12)
# print(result1)
#


'''
filter() 函数是 Python 内置的一个高阶函数，它可以过滤一个可迭代对象中的元素，
只保留符合条件的元素，然后返回一个新的可迭代对象。
filter() 函数的语法格式如下：


filter(function, iterable)

其中，function 是一个函数，用来对可迭代对象中的每个元素进行判断，返回值为 True 或 False；
iterable 是一个可迭代对象，比如列表、元组、集合等。
filter() 函数会依次将 iterable 中的每个元素传入 function 中进行判断，
只保留返回值为 True 的元素，最后返回一个新的可迭代对象，其中包含了所有符合条件的元素。
下面是一个使用 filter() 函数过滤列表中偶数的示例：

lst = [1, 2, 3, 4, 5]
even_lst = filter(lambda x: x %! (MISSING)== 0, lst)
print(list(even_lst))  # 输出：[2, 4]

在上面的代码中，filter() 函数将列表 lst 中的每个元素依次
传入匿名函数 lambda x: x %! (MISSING)== 0 中进行判断，只保留返回值为 True 的元素，
也就是偶数。最后，通过 list() 函数将过滤后的结果转换为列表并输出。
'''

# list1=[2637,14,312,6,44,87,2,23,21,32,32,42,76,5,4,5,7,8,0]
# result=filter(lambda x:x>100,list1)
#
# print(list(result))
#
# print(list1)
#
# def func(list1):
#     list2=[]
#     for i in list1:
#         if i>100:
#             list2.append()
#     return list2
#
# func(list1)
#


#找出所有年龄大于20岁的学生案例

# students=[
#     {'name':'tom','age':20},
#     {'name':'lucy','age':23},
#     {'name':'cray','age':12},
#     {'name':'mark','age':23},
#     {'name':'hen','age':18},
#     {'name':'steven','age':23},
# ]
#
#
# result=filter(lambda x:x['age']>20,students)
# print(list(result))
#
# #按照年齡進行从小到大的排序
# students=sorted(students,key=lambda x:x['age'],reverse=True)
#
# print(students)
