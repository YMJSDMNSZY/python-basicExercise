# -*- coding=utf-8 -*-

#使用greenlet 完成协程任务  需要人工切换
import time

import greenlet


def a(): #任务a
    for i in range(5):
        print('A'+str(i))
        gb.switch()
        time.sleep(0.2)

def b(): #任务b
    for i in range(5):
        print('B'+str(i))
        gc.switch()
        time.sleep(0.2)

def c(): #任务c
    for i in range(5):
        print('C'+str(i))
        ga.switch()
        time.sleep(0.2)

if __name__ == '__main__':
    ga=greenlet.greenlet(a)
    gb=greenlet.greenlet(b)
    gc=greenlet.greenlet(c)

    ga.switch()