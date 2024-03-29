# -*- coding=utf-8 -*-
'''
补充方法：
     静态方法(很类似类方法)
     1.需要装饰器@staticmethod
     2.静态方法无需传递参数
     3.也只能访问类的属性和方法，对象是无法访问的
     4.加载的时机同类方法


总结：
类方法  静态方法
不同：
1.装饰器不同
2.类方法是有参数的，静态方法没有参数
相同：
1.只能访问类的属性和方法，对象是无法访问的
2.都可以通过类名调用访问
3.都可以在创建对象之前使用，因为是不依赖于对象的

普通方法与两者的区别
不同：
1.没有装饰器
2.普通方法永远是要依赖对象的，因为每个方法都有一个self
3.只有创建了对象才可以调用普通方法，否则无法调用
'''



class Person:
    age=18  #__age就可将这个变成私有的

    def __init__(self,name):
        self.name=name

    def show(self):
        print('---------->',Person.age)

    @classmethod
    def update_age(cls):
        cls.age=20
        print('--->类方法')

    @classmethod
    def show_age(cls):
        print('修改后你的年龄是：',cls.age)

    @staticmethod  #静态方法
    def test():
        print('------>静态方法')
        # print(self.name)
        print(Person.age)


# Person.age=Person.age+1
# print(Person.age)

# p=Person()
# p.age=p.age+1
# p.show()

Person.update_age()
Person.show_age()
Person.test()


