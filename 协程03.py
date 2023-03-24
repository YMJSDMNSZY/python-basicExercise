# -*- coding=utf-8 -*-

'''

python还有一个比gxeenlet更强大的并且能够自动切换任务的模块gevent
其原理是当一个greenlet遇到IO（指的是input ouput输入输出，
比如网络、文件操作等）操作时，比如访问网络，就自动切换到其他的greenlet
等到IO完成，再适当的时候切换回来继续执行。
由于I0操作非常耗时，经常使程序处于等待状态，有了gevent我们自动切换协程,就保证总有greenlet在运行，而不是等待I0
'''

import time

import gevent
import greenlet
from gevent import monkey

monkey.patch_all()  #打补丁  用这个的时候会让下面的任务自动切换   没有这个的时候会自动按照顺序进行任务执行

def a(): #任务a
    for i in range(5):
        print('A'+str(i))

        time.sleep(0.2)

def b(): #任务b
    for i in range(5):
        print('B'+str(i))
        # gc.switch()  不需要手动写了
        time.sleep(0.2)

def c(): #任务c
    for i in range(5):
        print('C'+str(i))

        time.sleep(0.2)

if __name__ == '__main__':
    g1=gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()

    print('----------最后结束标志')