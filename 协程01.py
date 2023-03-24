# -*- coding=utf-8 -*-

'''
协程：微线程   耗时操作：网络请求（爬虫） IO：文件的读写  阻塞

'''


import time

def task1():
    for i in range(3):
        print('A'+str(i))
        yield
        time.sleep(0.2)

def task2():
    for i in range(3):
        print('A'+str(i))
        yield
        time.sleep(0.2)

if __name__ == '__main__':
    g1=task1()
    g2=task2()

    while True:
        try:
            next(g1)
            next(g2)

        except:
            break
