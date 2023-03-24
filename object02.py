# -*- coding=utf-8 -*-


# #定义类
# class Student:
#     #类属性
#     name='xiaowei'
#     age=2
#
#
# #使用类，创建对象   一个对象就占一个内存
# xiaowei=Student()
#
# #print(xiaowei.gender) #AttributeError: 'Student' object has no attribute 'gender'
# xiaowei.age=18  #对象属性  先找自己的，再找模型上的
# print(xiaowei.age)
#
#
# yupeng=Student()
# print(yupeng.name)
#
# yupeng.name='dhwau'
# print(yupeng.name)
#
# feifei=Student()
# Student.name='feifei'
# print(feifei.name)


class Person:
    name ='张三'
    def  __init__(self,name,age):
        self.name =name
        self.age = age

    def eat(self,food):
        print('{}正在吃{}!....'.format(self.name,food))

    def run(self):
        print('{},今年{}岁，正在跑步'.format(self.name,self.age))

p= Person('lisi',89)
p. name = '李四'
p. eat('红烧肉')
p.run()


p1 = Person('wangwu',23)
p1. name='王五'
p1.eat('狮子头')
p1.age=23
p1.run()












