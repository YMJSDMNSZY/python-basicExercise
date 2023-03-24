# -*- coding=utf-8 -*-

import threading
import random
import time

# lock=threading.Lock()
#
# list1=[0]*10
# def task1():
#     #获取线程锁，若已上锁，则等待锁的释放
#     lock.acquire() #阻塞
#     for i in range(len(list1)):
#         list1[i]=1
#         time.sleep(0.5)
#
#     lock.release()
#
#
# def task2():
#     lock.acquire()  # 阻塞
#     for i in range(len(list1)):
#         print('----->',i)
#         time.sleep(0.5)
#
#     lock.release()
#
#
# if __name__ == '__main__':
#     t1=threading.Thread(target=task1)
#     t2 = threading.Thread(target=task2)
#
#     t2.start()
#     t1.start()
#
#     t2.join()
#     t1.join()
#
#     print(list1)
'''
开发过程中使用线程，在线程间共享多个资源的时候，
如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不做任何事情。

解决死锁的方法：
1.重构代码
2.使用timeout

'''
from threading import Thread,Lock
lockA=Lock()
lockB=Lock()
class MyThread(Thread):
    def run(self):  #start()
        if lockA.acquire():  #若能获取到锁，则返回True
            print(self.name+'获取了A锁')
            time.sleep(0.1)
            if lockB.acquire():
                print(self.name+'又获取到了B锁，原来还有A锁 ')
                lockB.release()

            lockA.release()
class MyThread1(Thread):
    def run(self):  #start()
        if lockB.acquire():  #若能获取到锁，则返回True
            print(self.name+'获取了B锁')
            time.sleep(0.1)
            if lockA.acquire():
                print(self.name+'又获取到了A锁，原来还有B锁 ')
                lockA.release()

            lockB.release()

if __name__ == '__main__':
    t1=MyThread()
    t2=MyThread1()

    t1.start()
    t2.start()

