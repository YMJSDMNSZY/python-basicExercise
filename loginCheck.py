# -*- coding:utf-8 -*-
#
# # 登陆校验
# import time
#
#
# def decorate(func):
#     def wrapper(*args, **kwargs):
#         print('正在校验中......')
#         time.sleep(3)
#         print('校验完毕.......')
#         # 调用原函数
#         func(*args, **kwargs)
#
#     return wrapper
#
#
# @decorate
# def f1():
#     print('----------f1-----------')
#
#
# @decorate
# def f2():
#     print('----------f2-----------')
#
#
# f1()
# f2()
#



#
# def zhaung1(func):
#
#     print('装修1')
#     def wrapper(*args,**kwargs):
#         func(*args, **kwargs)
#         print('刷漆')
#
#     print('装修1----end')
#     return wrapper
#
#
# def zhaung2(func):
#     print('装修2')
#
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         print('铺地板')
#
#     print('装修2----end')
#     return wrapper
#
# @zhaung2
# @zhaung1
# def house():
#     print('叫我毛坯房。。。')
#
# house()

import time

islogin=False

def login():
    username=input('请输入用户名:')
    password=input('请输入密码：')
    if username=='admin' and password=='12345':
        return True
    else:
        return False



#定义一个装饰器，进行支付验证
def login_require(func):
    def wrapper(*args,**kwargs):
        global islogin
        print('--------付款操作----------')
        #验证用户是否登录了
        if islogin:
            func(*args,**kwargs)
        else:
            print('用户未登录，不能付款')
            #跳转到登录界面
            islogin=login()
            print('当前登陆状态是：',islogin)


    return wrapper

@login_require
def pay(money):
    print('正在付款中，付款的金额是：{}元'.format(money))
    print('付款中，请稍后......')
    time.sleep(2)
    print('付款完成，恭喜您获得想要的商品')

money=10000
pay(10000)




