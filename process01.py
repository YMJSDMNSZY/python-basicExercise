# -coding=utf-8 -*-

import os
'''

进程和线程是计算机操作系统中的两个重要概念，它们都是计算机执行程序的基本单位，但是它们之间存在着一些区别。

进程是指正在运行的一个程序的实例，它包括了程序代码、数据和进程控制块等信息。每个进程都拥有自己的地址空间、
系统资源和进程控制块等，进程之间相互独立，彼此之间不能直接访问对方的资源。

线程是指进程中的一个执行单元，它可以看作是进程中的一个子任务，它与进程共享同一地址空间、系统资源和进程控制块等，
线程之间可以直接访问对方的资源。一个进程可以包含多个线程，这些线程可以并发执行，从而提高了程序的运行效率。

总的来说，进程是一个独立的执行环境，而线程是在同一进程中的不同执行路径。进程之间相互独立，线程之间可以共享资源。
在实际编程中，需要根据实际需求来选择使用进程还是线程，以达到最优的程序效率和资源利用率。




多进程和多线程都是实现并发的方式，可以同时执行多个任务，提高程序的效率和性能。

多进程是指在操作系统中，每个进程都有自己独立的地址空间和系统资源，可以独立运行，相互之间不会影响。多进程可以利用多核CPU的优势，
同时处理多个任务，但是进程间的通信和同步需要通过进程间通信(IPC)的方式来实现，开销较大。

多线程是指在一个进程中，有多个线程共享进程的地址空间和系统资源，可以同时执行不同的任务，相互之间可以通过共享内存等方式来通信和同步，
开销较小。但是多线程的并发控制和资源共享需要考虑线程安全问题，需要使用锁、信号量等同步机制来保证程序的正确性和可靠性。

总的来说，多进程和多线程都是实现并发的方式，各有优缺点，需要根据具体的应用场景和需求来选择合适的方式。
'''

#进程创建
from multiprocessing import Process
from time import sleep
def task1():
    while True:
        sleep(1)
        print('这是任务1------------',os.getpid(),os.getppid())


def task2():
    while True:
        sleep(2)
        print('这是任务2------------',os.getpid(),os.getppid())


if __name__=='__main__':
    p=Process(target=task1,name='任务1')
    p.start()  #启动进程
    print(p.name)

    # p.join()   #等待进程结束
    p1 = Process(target=task2,name='任务2')
    p1.start()  # 启动进程
    print(p1.name)
    # p.join()  # 等待进程结束

    print('-------------------')
    print('********************')


    # task2()
