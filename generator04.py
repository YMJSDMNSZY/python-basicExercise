# -*- coding=utf-8 -*-

#进程>线程>协程
#写协程的时候，就是要把多个任务交替进行  可以快速的切换
def task1(n):
    for i in range(n+1):
        print('正在搬第{}块砖'.format(i))
        yield None

def task2(n):
    for i in range(n):
        print('正在听第{}几首歌'.format(i))
        yield None


g1=task1(4)
g2=task2(6)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except Exception as err:
        pass