# -*- coding=utf-8 -*-
# 列表推导式  字典推导式  集合推导式
# 旧的列表--->新的列表

# 1.列表推导式：格式：[含变量的表达式 for 变量 in 旧列表]  或者[含变量的表达式 for 变量 in 旧列表 if 条件]


# 过滤掉长度小于或等于3的人名
# names = ['tom', 'ew', 'huwrihihfewi', 'few', 'fhu', 'fe', 'trewggre']
# res = [name for name in names if len(name) > 3]
# res01 = [name.capitalize() for name in names if len(name) > 3]
# print(res)
# print(res01)

#
# '''
# def func(names):
#     list1=[]
#     for name in names:
#         if len(name)>3:
#         list1.append(name)
#
#     return list1
# '''


#
#
# #将1-100列表中能被3整除的，组成一个新的列表
# newlist=[i for i in range(1,100) if i%3==0]
# print(newlist)


#0~5的偶数 0~10的奇数构成的元组
#[(奇数，偶数),()]
#
# def func():
#     newlist=[]
#     for i in range(5):
#         if i%2==0:
#             for j in range(10):
#                 if j%2!=0:
#                     newlist.append((i,j))
#     return newlist
#
# x=func()
# print(x)
#

# res=[(x,y) for x in range(5) if x%2==0 for y in range(5) if y%2!=0]
# print(res)

# dict1= {'name':'tom','salary':3000}
# dict2= {'name':'ytre','salary':2000}
# dict3={'name':'fhg','salary':5000}
# dict4={'name':'ghcf','salary':8000}
# dict5= {'name':'bnbjn','salary':7000}
# list1=[dict1,dict2,dict3,dict4,dict5]
#
# newlist=[employee['salary']+200 if employee['salary']>5000 else employee['salary']+500 for employee in list1]
# print(newlist)


#集合推导式 类似列表推导式，在列表推导式的基础上增加了去重的功能
list1=[1,2,3,4,5,5,6,6,7,8,8,80,8,6,5,3]
set=[x for x in list1 if x>6]
print(set)


#字典推导式  key和value进行交换
dict1={'a':'A','b':'B','c':'C','d':'C'}
newdict={value: key for key,value in dict1.items()}
print(newdict)
