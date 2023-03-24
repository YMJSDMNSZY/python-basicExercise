
# -*- coding: utf-8 -*-
#
# def func(a, b):
#     c = 10
#
#     def inner_fun():
#         s = a + b + c
#         print('该函数相加之后的结果是：', s)
#
#     return inner_fun
#
#
# # 调用内部函数
# ifunc0 = func(3, 9)
# ifunc1 = func(2, 8)
#
# #闭包的好处是那个内置函数会占用一块内存地址，没被回收  可供调用
# print(ifunc0)
# print(ifunc1)
# ifunc0()
# ifunc1()




# 闭包同级访问举例
# 闭包总结
# 1.闭包看似优化了变量，原来在时象完成的工作，闭包也可以完成
# 2由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
# 3.闭包的好处，使代码变得简洁，便于阅读代码。
# 4.闭包是理解装饰器的基础

def func():
    a = 10

    def inner_func1():
        b = 90
        s = a + b
        print('该函数相加之后的结果是：', s)



    def inner_func2():
       inner_func1()
       print('------------>inner_func2')
       return 'hello world'

    return inner_func2

#调用func
f = func()

print(f)
ff = f()
print(ff)
