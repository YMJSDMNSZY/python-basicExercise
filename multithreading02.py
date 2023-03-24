# -*- coding=utf-8 -*-
'''
线程是可以共享全局变量的
python底层只要用线程默认加锁---->速度慢

GIL  全局解释器锁

耗时操作的时候推荐用线程，例如爬虫

'''
import threading
from time import sleep

# tickets=1000
# def func1():
#     global tickets
#     for i in range(100):
#         sleep(0.5)
#         tickets-=1
#
# if __name__ == '__main__':
#     #创建线程
#     th1=threading.Thread(target=func1,name='线程一')
#     th2 = threading.Thread(target=func1, name='线程二')
#     th3 = threading.Thread(target=func1, name='线程三')
#     th4 = threading.Thread(target=func1, name='线程四')
#
#     th1.start()
#     th2.start()
#     th3.start()
#     th4.start()
#
#     th1.join()
#     th2.join()
#     th3.join()
#     th4.join()
#




n=0
def task01():
    global n
    for i in range(10000000):#数值超大的时候不执行
        n+=1
    print('task1中n的值为:',n)


def task02():
    global n
    for i in range(10000000):
        n+=1
    print('task2中n的值为:',n)


if __name__ == '__main__':
    th1=threading.Thread(target=task01)
    th2=threading.Thread(target=task02)

    th1.start()
    th2.start()

    th1.join()
    th2.join()


    print('最后打印n的值：',n)