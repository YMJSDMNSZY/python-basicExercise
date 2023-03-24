# -*- coding=utf-8 -*-

'''
特点：
    1.定义需要以来装饰器@classmethod
    2.类方法中参数不是一个对象，而是一个类
        print(cls) #<class '__main__.Dog'>
    3.类方法中只可以使用类属性
    4.类方法中是否可以使用普通方法？，既能用self.方法名()调用兄弟    是不能的 因为类方法实在对象创建前就已经存在的
类方法的作用：
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些动作（方法）


'''
#类方法
class Dog:
    def __init__(self,nickname):
        self.nickname=nickname

    def run(self):#self 依赖于对象
        print('{}在院子里跑来跑去'.format(self.nickname))


    def eat(self):
        print('吃饭。。。。。。')
        self.run() #类中方法的调用，兄弟之间方法的调用需要用到self.方法名()

    @classmethod  #调的是类方法，会把类传进去
    def test(cls): #cls class  类方法不依赖于对象
        print(cls)
        # print(cls.nickname)


# Dog.test()

d=Dog('大黄')
d.run()


# d.test()