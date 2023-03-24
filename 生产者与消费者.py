# -*- coding=utf-8 -*-



'''
生产者与消费者:两个线程之间的通信

python的queue模块中提供了同步的、线程安全的队列类，包括FIFO(先入先出)队列Queue,
LIFO(后入先出）队列infoQueue，和优先级队列PriorityQueue。
这些队列都实现了锁原理(可以理解为原子操作，即要么不做，要么就做完〉，能够在多线程中直接使用。
可以使用队列来实现线程间的同步。



在这个示例中，Producer和Consumer都是继承自Thread的类，分别用于生产和消费数据。
这里使用了Python的queue模块来实现线程间的安全通信，Producer通过put方法向队列中添加数据，Consumer通过get方法从队列中取出数据。
为了保证程序的正常退出，当Producer生产完数据后，向队列中添加了一个None，表示数据已经全部生产完毕，Consumer在取出这个None后就会退出循环。

'''

import threading
import queue
import time

class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = "item-" + str(i)
            self.queue.put(item)
            print("Producer put " + item)
            time.sleep(1)

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            if item is None:
                break
            print("Consumer get " + item)
            time.sleep(2)

if __name__ == '__main__':
    q = queue.Queue()
    producer = Producer(q)
    consumer = Consumer(q)

    producer.start()
    consumer.start()

    producer.join()
    q.put(None)
    consumer.join()

