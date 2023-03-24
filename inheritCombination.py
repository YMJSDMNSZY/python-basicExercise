# -*- coding=utf-8 -*-
#
# #"is a" 和 "has a" 是面向对象编程中的两个基本概念。
#
# '''
#
# 特点:
# 1.如果类中不定义_init_，调用父类super class的__init
# 2．如果类继承父类也需要定义自己的_init_，就需要在当前类的_init_调用一下父类_init3.如何调用父类__init:
# super().__init__(参数)
# super (类名,对象).__init__(参数)
# 4.、如果父类有eat(),子类也定义一个eat方法，默认搜索的原则:先找当前类，再去找父类
# s.eat()
# override:重写（覆盖)   定义一个同名的方法，这种行为:重写
#
#可以多继承！！！多继承搜索原则：顺序是广度优先
#1）验证 import inspect   inspect.getmro(某个类)  2） 直接打印   某个类.__mro__
#使用 “类名.__bases__” 可以查看继承的父类


# "is a" 表示继承关系，即一个类是另一个类的子类，具有一些共同的属性和方法，同时也可以拥有自己的属性和方法。
# 在 Python 中，使用 class Subclass(BaseClass): 的语法来表示一个类 Subclass 是另一个类 BaseClass 的子类。例如：
# '''
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print("Animal is eating food.")
# class Dog(Animal): #继承的标准格式
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)  #调用父类的init  也可 super(类名,对象).__init__(参数 参数可有可无)
#         #Animal.__init__(self)
#         self.breed = breed
#     def bark(self):
#         print("Dog is barking.")
#
#
# #组合关系举例
# # 在上述代码中，类 Dog 继承自类 Animal，因此 Dog 是 Ani，可以通过在类中创建其他类的实例来实现组合关系。例如：
# # #mal 的子类，具有 Animal 的属性和方法，同时 Dog 还有自己的属性和方法，例如 bark() 方法。
# # "has a" 表示组合关系，即一个类包含另一个类的实例作为其属性，可以通过该实例来调用包含类中的方法。在 Python 中
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def start_engine(self):
#         print("Car engine is started.")
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.car = Car("Toyota", "Corolla", 2020)
#     def drive_car(self):
#         self.car.start_engine()
#
# # 在上述代码中，类 Person 包含一个名为 car 的属性，其类型是 Car 类的实例。
# # 这意味着 Person 可以调用 Car 中定义的方法，例如 start_engine() 方法，而不必自己实现该方法。
# # 实际应用方面，"is a" 和 "has a" 的概念通常用于设计类的继承关系和组合关系，以便于更好地实现代码的复用和扩展。
# # 对于继承关系，可以通过继承来实现代码的重用，减少代码的冗余；对于组合关系，可以通过将多个类组合在一起来实现更复杂的功能，提高代码的灵活性和可扩展性。



'''
编写一个简单的工资管理程序,系统可以管理以下四类人(worker)、销售员(salesman)、
经理(manager)、销售经理(salemanger)。所有的员工都具有员工号，姓名，工资等属性，
有设置姓名，获取姓名，获取员工号，计算工资等方法。
1）工人:工人具有工作小时数和时薪的属性，工资计算法方法为工作小时数*时薪。
2）销售员:具有销售额和提成比例的属性，工资计算方法为销售额*提成比例。
3)经理:具有固定月薪的属性，工资计算方法为固定月薪。
4)销售经理:工资计算方法为销售额*提成比例+固定月薪。
请根据以上要求设计合理的类，完成以下功能:
    1）添加所有类型的人员
    2)计算月薪
    3)显示所有人工资情况

'''
#
# class Person:
#     def __init__(self,no,name,salary):
#         self.no=no
#         self.name=name
#         self.salary=salary
#
#     def __str__(self):
#         msg='工号：{}，姓名：{}，本月薪资：{}'.format(self.no,self.name,self.salary)
#         return msg
#
#
#     def getSalary(self):
#         return self.salary
#
#
# class Worker(Person):
#     def __init__(self,no,name,salary,hours,per_hour):
#         super().__init__(no,name,salary)
#         self.hours=hours
#         self.per_hour=per_hour
#
#     def getSalary(self):
#         money=self.hours*self.per_hour
#         self.salary+=money
#         return self.salary
#
# class Salesman(Person):
#     def __init__(self,no,name,salary,salemoney,percent):
#         super().__init__(no,name,salary)
#         self.salemoney=salemoney
#         self.percent=percent
#
#     def getSalary(self):
#         money=self.salemoney*self.percent
#         self.salary+=money
#         return self.salary
#
#
# #创建子类对象
# # w=Worker('001','king',2000,160,50)
# # s=w.getSalary()
# # print('月薪是：',s)
#
# saler1=Salesman('002','ca',6483,26742765378,0.003)
# s1=saler1.getSalary()
# print('月薪是：',s1)
# print(saler1)





class Person:
    def __init__(self, no, name, salary):
        self.no = no
        self.name = name
        self.salary = salary
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def getNo(self):
        return self.no
    def getSalary(self):
        return self.salary
class Worker(Person):
    def __init__(self, no, name, salary, hours, per_hour):
        super().__init__(no, name, salary)
        self.hours = hours
        self.per_hour = per_hour
    def getSalary(self):
        money = self.hours * self.per_hour
        self.salary += money
        return self.salary
class Salesman(Person):
    def __init__(self, no, name, salary, salemoney, percent):
        super().__init__(no, name, salary)
        self.salemoney = salemoney
        self.percent = percent
    def getSalary(self):
        money = self.salemoney * self.percent
        self.salary += money
        return self.salary
class Manager(Person):
    pass
class SaleManager(Salesman, Manager):
    def __init__(self, no, name, salary, salemoney, percent):
        super().__init__(no, name, salary, salemoney, percent)
    def getSalary(self):
        money = self.salemoney * self.percent + self.salary
        return money
class SalaryManage:
    def __init__(self):
        self.persons = []
    def addPerson(self, person):
        self.persons.append(person)
    def getSalary(self, no):
        for person in self.persons:
            if person.getNo() == no:
                return person.getSalary()
        else:
            return None
    def displayAll(self):
        for person in self.persons:
            print(person)
# 测试代码
salary_manage = SalaryManage()
# 添加所有类型的人员
worker = Worker("001", "张三", 0, 160, 50)
salesman = Salesman("002", "李四", 0, 200000, 0.03)
manager = Manager("003", "王五", 8000)
sale_manager = SaleManager("004", "赵六", 8000, 1000000, 0.02)
salary_manage.addPerson(worker)
salary_manage.addPerson(salesman)
salary_manage.addPerson(manager)
salary_manage.addPerson(sale_manager)
# 计算月薪并显示所有人工资情况
for person in salary_manage.persons:
    person.getSalary()
salary_manage.displayAll()