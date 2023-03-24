# -*- coding:utf-8 -*-

# 闭包的应用
# def generate_count():
#     container = [0]
#
#     def add_one():
#         container[0] =container[0]+1
#         print('当前是您第{}次访问'.format(container[0]))
#
#     return add_one
#
# counter = generate_count()
# counter() #第一次访问
# counter()
# counter()





# 装饰器：闭包的一个升级  1.将函数作为参数进行传递，装饰的是一个函数  2.要有闭包的特点出现

#
# def func(number):
#     a = 100
#
#     def inner_fun():
#         nonlocal a
#         nonlocal number
#         number += 1
#
#         for i in range(number):
#             a += 1
#         print('修改之后a的值是：', a)
#
#     return inner_fun
#
# #对func进行调用
# f = func(5)
# f()
#
# #函数作为参数
# a=50
# f1=func(a)#a是一个实参
# print(f1)
#
#
#
# #地址引用
# def test():
#     print('------test------')
#
# t=test



def decorate(func):
    a=100
    print('-------->wrapper外层函数开始了')
    def wrapper():

        func()
        print('-------->刷漆')
        print('-------->铺地板')

    print('-------->wrapper外层函数结束了。。。。。')

    return wrapper

#使用装饰器
@decorate
def house():  #此时1.house是被装饰函数  2.将被装饰函数作为参数传给装饰器decorate  3.执行decorate函数（底层会执行）
    print('我是毛坯,,,,')

def house1():
    house()
    print('刷漆')
    print('铺地板')

house()
print('--           ---')
house1()


