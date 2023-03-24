# -*- coding=utf-8 -*-
'''
生成器方法：
    __next__():获取下一个元素  每次调用的时候会产生新的元素，如果元素产生完成，会有异常报错
    send():既可以生成一个元素，也可以送出一个元素  注意：第一次调用的时候要先传一个None

'''

def gen():
    i=0
    while i<5:
        temp=yield i
        print('temp:',temp)
        for x in range(temp):
            print('---------->',x)
        print('************')
        i+=1

    return 'No more data!!!'

g=gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#g.__next__()

print(g.send(None))
n1=g.send('1')
print('n1:',n1)
n2=g.send('2')
print('n2:',n2)
