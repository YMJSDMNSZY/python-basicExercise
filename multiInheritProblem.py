# -*- coding=utf-8 -*-
'''
Python支持多继承，而任何实现多继承的语言都需要处理潜在的命名冲突，
这种命名冲突是由不相关的祖先类实现同名方法引起，这种冲突就被称为 菱形问题。
需要声明的是，在 Python3 中多继承的搜索顺序为：从左至右，广度优先；
Python2采用的多继承搜索顺序为：从左至右，深度优先。




  首先，创建D类的对象的d，然后调用其中的 show 方法，再调用 test 方法（以下序号在代码中标出）：

1、调用 show 方法，由于类 D 实现了自己的 show 方法，则此时进入 D 类的 show 方法，
    然后使用 super 方法调用了父类的 show方法，B、C类都没有实现该方法，则继续往上找，
    A 类中实现了 show 方法，则执行该方法，再继续向下执行。

2、在 test 方法中首先调用了自己的 show 方法，则重复上一条的执行顺序。

3、此处调用父类的 show 方法，往上找A类中实现了 show 方法，则执行该方法。

4、由于D类没有 fun 方法，则根据搜索顺序，B--->A，则执行B类的 fun 方法。

5、调用父类的 fun 方法，搜索顺序与上一条相同。

6、此处需要注意，直接在类上调用实例方法时，必须显示的传入参数 self。


'''
# class A:
#     def show(self):
#         print('---A---')
#
#
# class B(A):
#     def fun(self):
#         print('this is class B!')
#
#
# class C(A):
#     def fun(self):
#         print('this is class C!')
#
#
# class D(B, C):
#     def show(self):
#         super().show()  # --->1
#         print('---D---')
#
#     def test(self):
#         self.show()  # --->2
#         super().show()  # --->3
#         self.fun()  # --->4
#         super().fun()  # --->5
#         C.fun(self)  # ---->6
#         C.show(self)  # --->7
#
#
# d = D()
# d.show()
# print('-----------------------------')
# d.test()






#
# class A:
#     pass
#
#
# class B:
#     pass
#
#
# class C(A):
#     pass
#
#
# class D(A):
#     pass
#
#
# class E(B, C):
#     pass
#
#
# class G1(C, B, D):
#     pass
#
#
# class F1(D, B):
#     pass
#
#
# class F2(C, D):
#     pass
#
#
# class G2(C, D, B):
#     pass
#
#
# class G3(D, B, C):
#     pass
#
#
# print(C.__mro__)
# print(D.__mro__)
# print(E.__mro__)
# print(F1.__mro__)
# print(F2.__mro__)
# print(G1.__mro__)
# print(G2.__mro__)
# print(G3.__mro__)


'''
在这里，首先需要介绍一个类的属性 __mro__ ，它的返回值是一个元组，
可按照方法解析顺序（由于Python会按照特定的顺序遍历继承图，这个顺序成为方法解析顺序）列出各个超类，
从当前类一直向上，知道 object 类。为了更加深入的说明问题，在代码实现时，增加了几个不同的继承关系。
从以上代码中，可以得出以下结论：

1、类的多继承与继承的顺序有关，按照从左到右的顺序，依次搜索。

2、继承采用从左到右，广度优先顺序进行搜索，例如类 F2。

3、同一级别的父类搜索完之后，才继续向上一级搜索，例如类 G1、G2、G3。

4、所有的继承搜索顺序到达 object 类停止。
原文链接：https://blog.csdn.net/weixin_37963567/article/details/105099326
'''



class A:
    def __init__(self, i = 0):
        self.i = i
    def m1(self):
        self.i += 1

class B(A):
    def __init__(self,j =0):
        A.__init__(self,3)
        self.j =j
    def m1(self):
        self.j += 1

def main():
    b = B()
    b.m1()
    print(b.i, b.j)
main()
