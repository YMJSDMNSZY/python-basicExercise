# -*- coding=utf-8 -*-

class Cat:
    type='猫'
    def __init__(self,nickname,age,color):
        self.nickname=nickname
        self.age=age
        self.color=color

    def eat(self,food):
        print('{}喜欢吃{}'.format(self.nickname,food))

    def catch_mouse(self,color,weight):
        print('{},抓了一只{}kg的，{}的大老鼠'.format(self.nickname,weight,color))

    def sleep(self,hour):
        if hour<5:
            print('乖乖睡吧')
        else:
            print('赶快起床抓老鼠')

    def show(self):
        print('猫的详细信息：')
        print(self.nickname,self.age,self.color)

#创建对象
cat1=Cat('花花',34,'灰色')

#通过对象调方法
cat1.catch_mouse('黑色',2)
cat1.sleep(4)
cat1.eat('小金鱼')
cat1.show()