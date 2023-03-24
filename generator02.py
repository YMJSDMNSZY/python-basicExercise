# -*- coding=utf-8 -*-



# g=(x*5 for x in range(10))
#
# while True:
#     try:
#         res=next(g)
#         print(res)
#     except:
#         print('没有多余元素了！！！')
#         break
#
#

#
# #1.定义一个函数，函数中使用yield关键字
# #2.调用函数，接收调用的结果
# #3.得到的结果就是生成器  借助next()  __next__可将值取出来
# def func():
#     n=0
#     while True:
#         n+=1
#         #print(n)
#         yield n#只要出现了yield这个关键字，说明该函数变成一个生成器了
#         #相当于return n+暂停
# g=func()
# print(g)
# print(next(g))


#斐波那切数列

def fib(length):
    a,b=0,1
    n=0

    while n<length:
        #print(b)
        yield b
        a,b=b,a+b
        n+=1
    return 'abc'#得到StopIteration之后将该结果在其后返回出来

g=fib(8)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
