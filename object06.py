# -*- coding=utf-8 -*-
import sys
#！！！init_:初始化魔术方法（构造方法：创建完空间后调用的第一个方法）
#触发时机:初始化对象时触发（不是实例化触发，但是和实例化在一个操作中)

#了解即可 __new__
# 实例化的魔术方法
# 触发时机:在实例化的时候触发

#__call__:对象调用方法
#触发时机：将对象当成函数使用时，会默认调用此函数里面的内容


#99%不需要重写   __del__:
#   1.对象赋值 p=Person()
#     p=Person()
#     p1=p
#     说明：p和p1指向同一个地址

#   2.删除地址的引用
#       del p1 删除p1对地址的引用
#   3.查看对地址引用的次数
#       import sys
#       print(sys.getrefcount(n))
#   4.当一块空间没有了任何引用，默认执行__del__
#       ref=0的时候


#！！！__str__:触发时机：打印对象名  自动触发__str__里面的内容
# 注意：一定要在这个方法里加return，其后的内容就是要打印的内容


class Person:
    def __init__(self,name):
        # print('--------->init',self)
        self.name=name

    # def __new__(cls, *args, **kwargs):#会覆盖上面的魔术方法,开辟内存
    #     print('------->new')
    #     # return super(Person,cls).__new__(cls,*args,**kwargs)
    #     # return  object.__new__(cls,*args, **kwargs)  此时参数无需传
    #     position=object.__new__(cls)
    #     print(position)
    #     return position
    #
    # def __call__(self, *args, **kwargs):#
    #     print('-------->call')
    #     # print('执行方法得到的参数是：',name)

    # def __del__(self):
    #     print('----------->del')

    def __str__(self):
        return self.name

p=Person('jack')
print(p)


# 单纯打印对象名称，出来的只是一个地址，地质队与开发者说没有太大意义
# 若想在打印对象名的时候能够给开发者更多的信息量



# # # p=Person()
# # # print(p)
# #
# # #对象当成函数
# # p('jack')
#
# p=Person('jack')
# p1=p
# print(p1.name)  # p和p1 用的都是同一个地址




print(sys.getrefcount(p))

# p1.name='tom'
# print(p.name)

'''
元类是一种比较高级的概念，它是用于创建类的类。在Python中，一切皆对象，包括类也是对象。
因此，我们可以使用元类来控制类的创建和行为，从而实现更加灵活和高效的编程。
元类最常用的场合是在框架和库中，用于控制类的创建和行为，
例如Django框架中的ORM（Object-Relational Mapping）模块就使用了元类来实现自动映射数据库表和类。
此外，元类还可以用于实现单例模式、装饰器、插件等功能。
在Python中，我们可以使用type类来创建类，例如：

MyClass = type('MyClass', (object,), {})

以上代码创建了一个名为MyClass的类，该类继承自object，并且没有任何属性和方法。
其中，type类的第一个参数是类名，第二个参数是继承的父类元组，第三个参数是类的属性和方法字典。
通过这种方式，我们就可以使用type类来动态创建类，从而实现更加灵活和高效的编程。
除了使用type类创建类之外，我们还可以通过定义元类来创建类。例如：

class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['my_attribute'] = 'Hello, world!'
        return super().__new__(cls, name, bases, attrs)
class MyClass(metaclass=MyMeta):
    pass

以上代码定义了一个名为MyMeta的元类，该元类继承自type。在元类中定义了一个名为__new__的方法，
用于创建类。在方法中，我们向类的属性和方法字典中添加了一个名为my_attribute的属性，并赋值为Hello, world!。
在定义类时，我们使用metaclass=MyMeta来指定元类，从而创建了一个名为MyClass的类。
这样，在创建MyClass类实例时，会自动调用元类中的__new__方法，从而实现对类的控制。
总之，元类是一种高级的概念，它可以用于控制类的创建和行为，从而实现更加灵活和高效的编程。
在实际开发中，我们可以根据具体需求和场景，选择适合的方式来使用元类。







类中的魔术方法是在Python中具有特殊含义的方法，它们以双下划线开头和结尾（例如__init__方法）。以下是一些常见的魔术方法及其介绍：


init(self, ...)：类的构造函数，在创建对象时自动调用，用于初始化对象的属性。

str(self)：返回对象的字符串表示形式，可以使用print()函数打印对象时自动调用。

repr(self)：返回对象的“官方”字符串表示形式，可以用于调试和开发过程中的输出。

len(self)：返回对象的长度，可以使用len()函数获取对象的长度时自动调用。

getitem(self, key)：返回对象中指定键的值，可以使用索引或切片操作获取对象的元素时自动调用。

setitem(self, key, value)：设置对象中指定键的值，可以使用索引或切片操作设置对象的元素时自动调用。

delitem(self, key)：删除对象中指定键的值，可以使用del语句删除对象的元素时自动调用。

getattr(self, name)：获取对象中不存在的属性时自动调用，返回一个默认值或抛出AttributeError异常。

setattr(self, name, value)：设置对象的属性时自动调用，用于防止设置不存在的属性或进行其他额外操作。

delattr(self, name)：删除对象的属性时自动调用，用于防止误删除或进行其他额外操作。

call(self, ...)：使对象可以像函数一样被调用，可以在类中定义可调用的对象。

eq(self, other)：判断两个对象是否相等时自动调用，可以自定义对象的比较方式。

lt(self, other)：判断对象是否小于另一个对象时自动调用，可以自定义对象的比较方式。

gt(self, other)：判断对象是否大于另一个对象时自动调用，可以自定义对象的比较方式。

le(self, other)：判断对象是否小于或等于另一个对象时自动调用，可以自定义对象的比较方式。

ge(self, other)：判断对象是否大于或等于另一个对象时自动调用，可以自定义对象的比较方式。
总之，魔术方法可以让我们自定义类的行为，实现更灵活和高效的代码。
'''