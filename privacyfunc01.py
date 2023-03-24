# -*- coding=utf-8 -*-

# #私有化
# '''
# get好处：
#  1.隐藏属性不被外界随意修改
#  2.也可以修改，通过函数
#     def setXXX(self,XXX):
#         pass
#     3.筛选赋值的内容
#     if xxx 是否符合条件:
#         赋值
#     else:
#         报错不赋值
# 4.如果想获取某个具体的属性
#     使用get函数
#     def getXXX(self): #没有参数，但是有返回值
#         return self.__xxx
#
#
# '''
# #封装：1.私有化属性  2.定义公有set 和get 方法
# class Student:
#     # __age=18  #类属性
#
#     def __init__(self,name,age):   #这里的self叫对象属性
#         self.name=name
#         self.__age=age
#         self.__score=89
#
#
#     #定义公有set和get方法
#     #set是为了赋值   私有化的时候这样
#     # 可以限制其值的内容
#     def setAge(self,age):
#         if age>0 and age<120:
#             self.__age=age
#         else:
#             print('您输入的年龄不在标准范围内！！！')
#
#     #get是为了取值
#     def getAge(self):
#         pass
#
#
#
#     def __str__(self):
#         return '姓名：{}，年龄：{}，考试分数：{}'.format(self.name,self.__age,self.__score)
#
#
# student01=Student('于鹏',23)
# print(student01)
# print(dir(Student))
# print(dir(student01))
# print(student01.__dir__())
# # print(student01,_Student.__age)#其实就是__age，只不过是系统给它自动改名了
#
# # student02=Student('菲菲',23)
# # student02.setAge(30)
# # print(student02)


class Student:
    # __age=18  #类属性

    def __init__(self,name,age):   #这里的self叫对象属性
        self.name=name
        self.__age=age
        self.__score=89
    #先有getXXX，
    @property  #此时这个类是一个装饰器
    def age(self):
        return self.__age


    #再有setter,因为set依赖于get
    @age.setter
    def setAge(self,age):
        if age>0 and age<120:
            self.__age=age
        else:
            print('您输入的年龄不在标准范围内！！！')


    #定义公有set和get方法
    #set是为了赋值   私有化的时候这样
    # 可以限制其值的内容
    # def setAge(self,age):
    #     if age>0 and age<120:
    #         self.__age=age
    #     else:
    #         print('您输入的年龄不在标准范围内！！！')
    #
    # #get是为了取值
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return '姓名：{}，年龄：{}，考试分数：{}'.format(self.name,self.__age,self.__score)



s=Student('peng',30)
s.name='xiaoming'
print(s.name)
print(s.age)

# #私有化赋值
# s.setAge(20)
# print(s.getAge())