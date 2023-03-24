# -*- coding=utf-8 -*-

'''
在Python中，进程间通信有多种方式，常用的有以下几种：

1. 队列（Queue）：多个进程之间可以通过队列来实现数据的传递和共享，队列底层使用了锁机制来保证数据的安全性。

2. 管道（Pipe）：管道通常用于两个进程之间的通信，它可以实现双向通信，底层也是使用锁机制来保证数据的安全性。

3. 共享内存（Shared Memory）：多个进程之间可以通过共享内存来实现数据的共享，共享内存可以看作是一个特殊的变量，多个进程可以同时访问它，底层使用了锁机制来保证数据的安全性。

4. 信号量（Semaphore）：信号量通常用于控制多个进程之间的并发，可以通过信号量来控制进程的访问顺序，底层也是使用锁机制来保证数据的安全性。

5. 文件映射（File Mapping）：文件映射通常用于多个进程之间的数据共享，它可以将一个文件映射到多个进程的内存空间中，多个进程可以同时访问这个文件，底层使用了锁机制来保证数据的安全性。

以上这些方式都可以用于进程间的通信，具体使用哪一种方式，取决于具体的应用场景和需求。
'''
from multiprocessing import Queue
from multiprocessing import Process
#
# q=Queue(4)
#
# q.put('a')
# q.put('b')
# q.put('c')
# q.put('d')
# print(q.qsize())
# if not q.full():#判断队列是否满了  q.empty()判断queue是否为空
#     q.put('e',timeout=4)  #如果queue满了，则等待
# else:
#     print('队列已满')

# #获取队列的值
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# #q.put_nowait()
# #q.get_nowait()


#进程间通讯
from time import sleep


def download(q):
    images=['131.jpg','242.jpg','3214.eo']
    for image in images:
        print('正在下载：',image)
        sleep(0.4)
        q.put(image)


def getfile(q):
    while True:
        try:
            file=q.get(timeout=5)
            print('{}保存成功！'.format(file))
        except:
            print('全部保存完毕！')
            break


if __name__ == '__main__':
    q=Queue(5)
    p1=Process(target=download,args=(q,))
    p2=Process(target=getfile,args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print('0000000000000')