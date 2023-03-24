#体验可变参数

'''
在Python中，变量作用域指的是变量的有效范围，即变量可以被访问和修改的区域。Python中的变量作用域可以分为以下几种：


全局作用域：定义在模块级别的变量拥有全局作用域，可以在模块中的任意位置被访问和修改。

局部作用域：定义在函数或代码块内部的变量拥有局部作用域，只能在函数或代码块内部被访问和修改。

嵌套作用域：当一个函数内部定义了另外一个函数时，内部函数可以访问外部函数的变量，但是外部函数不能访问内部函数的变量。
在Python中，变量的作用域遵循LEGB规则，即：

Local作用域：指函数内部定义的变量，只在函数内部有效。

Enclosing作用域：指函数内部嵌套函数的作用域，内部函数可以访问外部函数的变量。

Global作用域：指模块级别定义的变量，可以在整个模块内部访问。

Built-in作用域：指Python内置函数的作用域，可以在整个程序中访问。
在Python中，变量的作用域可以通过关键字global和nonlocal来进行修改：

global关键字用于在函数内部修改全局变量，例如：

x = 10
def func():
    global x
    x = 20
func()
print(x)  # 输出20


nonlocal关键字用于在内部函数中修改外部函数的变量，例如：

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)  # 输出20
outer()

需要注意的是，全局变量和局部变量名称相同时，局部变量会覆盖全局变量，因此需要避免变量名重复的情况。
同时，过多的使用global和nonlocal关键字可能会导致代码的可读性和可维护性降低，因此需要谨慎使用。

'''
# def make_sandwich(*args):
#     res = " "
#     for item in args:
#         res+=item
#         res+='、'
#     print("你的三明治包含了"+res)
#     print("你的三明治包含了{}".format(res))
#
# make_sandwich('生菜','牛肉')


#体验关键字参数
# def kw_function(**args):
#     print(args)
#
# kw_function(w=3,r=6,re=3)


#体验各种元组相加的
def add_all_num(*L,a):
    print(L)
    sum = 0
    for item in L:
        sum+=item
    print("该内容的和为{}".format(sum))
    print("a的值",a)
add_all_num(1,3,5,7,a=2)