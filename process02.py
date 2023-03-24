# -coding=utf-8 -*-

'''
进程的目的：能干活  用可变类型（列表）
计算密集型的时候用这个好点

'''

import os

#进程创建
from multiprocessing import Process
from time import sleep
def task1(s):
    while True:
        sleep(s)
        print('这是任务1------------',os.getpid(),os.getppid())


def task2(s):
    while True:
        sleep(s)
        print('这是任务2------------',os.getpid(),os.getppid())


if __name__=='__main__':
    number=1
    print(os.getpid())
    #子进程
    p=Process(target=task1,name='任务1',args=(1,))
    #Process(target=函数，name=进程名字，args=（给函数传的参数，可迭代的列表或元组）)
    p.start()  #启动进程
    print(p.name)

    # p.join()   #等待进程结束
    p1 = Process(target=task2,name='任务2',args=(2,))
    p1.start()  # 启动进程  同xxx.run
    print(p1.name)
    # p.join()  # 等待进程结束

    while True:
        number+=1
        sleep(0.9)
        if number==100:
            p.terminate()
            p1.terminate()#终止进程
            break
        else:
            print('--------->number',number)

    print('-------------------')
    print('********************')


    # task2()
