# -*- coding=utf-8 -*-

"""
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程,
但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法。
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满,
那么就会创建一个新的进程用来执行该请求;但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，
直到池中有进程结束，才会创建新的进程来执行。

非阻塞式：

阻塞式：
   添加一个执行一个任务，如果一个任务不结束另一个任务就进不来

"""
import os
from multiprocessing import Pool
import time

# #非阻塞式进程
from random import random
#
#
# def task(task_name):
#     print('开始做任务啦！！！',task_name)
#     start=time.time()
#     #使用sleep
#     time.sleep(random()*2)
#     end=time.time()
#     # print('任务完成用时：',(end-start),'进程id:',os.getpid())
#     # return '任务完成用时：', (end - start), '进程id:', os.getpid()
#     return '完成任务：{}！用时：{}，进程id:{}'.format(task_name,(end-start),os.getpid())
#
#
# container=[]
# def callback_func(n):#将返回值进行输出处理
#     container.append(n)
#
#
# if __name__=='__main__':
#     pool=Pool(5)
#     tasks=['听音乐','打游戏','散步','吃饭','做饭','看孩子','洗衣服']
#     for task1 in tasks:
#         pool.apply_async(task,args=(task1,),callback=callback_func)  #非阻塞模式
#     # task(tasks)
#
#     pool.close() #添加任务结束
#     pool.join()  #
#     for c in container:
#         print(c)
#     # print('over!!!')


def task(task_name):
    print('开始做任务啦！！！',task_name)

    start=time.time()
    #使用sleep
    time.sleep(random()*2)
    end=time.time()
    print('任务完成用时：',(end-start),'进程id:',os.getpid())
    # return '任务完成用时：', (end - start), '进程id:', os.getpid()
    # return '完成任务：{}！用时：{}，进程id:{}'.format(task_name,(end-start),os.getpid())


container=[]
def callback_func(n):#将返回值进行输出处理
    container.append(n)


if __name__ == '__main__':
    pool=Pool(5)

    tasks=['听音乐','打游戏','散步','吃饭','做饭','看孩子','洗衣服']
    for task1 in tasks:
        pool.apply(task,args=(task1,))  #阻塞模式

    pool.close()
    pool.join()  #让主进程让步，插队

    print('over!!!!')