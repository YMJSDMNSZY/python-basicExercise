# -*- coding=utf-8 -*-
# s = lambda a, b: a + b
# print(s)  # 现在s就是函数function
#
# result=s(1,2)
# print(result)



# #匿名函数可以作为某个函数的参数
# def func(x,y,func):
#     print(x,y)
#     print(func)
#     s=func(x,y)
#     print(s)
#
#
# #调用func
# func(1,2,lambda a,b:a+b)

list1=[{'a':1,'b':1},{'a':2,'b':2},{'a':3,'b':3},{'a':4,'b':4}]

m=max(list1,key=lambda x:x['a'])
print('列表的最大值：',m)