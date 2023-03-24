# -*- coding=utf-8 -*-
#递归函数
'''
普通：def func:pass
匿名函数：lambda参数：返回结果
递归函数：普通函数的一种表现形式
特点：
1.通常有一个入口
2.递归函数必须要设定一个终点





递归函数是一种特殊的函数，它可以在函数内部调用自身。
递归函数通常用于解决问题的分治处理，将一个大问题分解成若干个小问题，
然后逐个解决小问题，最终合并得到大问题的解。
在 Python 中，递归函数的基本定义形式如下：


def recursive_function(args):
    if base_case:
        return base_case_result
    else:
        return recursive_function(modified_args)

在上面的代码中，recursive_function 是一个递归函数，当满足 base_case 条件时，
递归函数会返回 base_case_result，否则递归函数会修改参数 args
并继续调用自身 recursive_function，直到满足 base_case 条件为止。
下面是一个使用递归函数计算阶乘的示例：

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # 输出：120

在上面的代码中，factorial 函数使用递归的方式计算阶乘。当 n 等于 0 时，
递归函数返回 1，否则递归函数返回 n 乘以 factorial(n - 1) 的结果，直到 n 等于 0 为止。
factorial(5) 的计算过程如下：


factorial(5) = 5 * factorial(4)
             = 5 * 4 * factorial(3)
             = 5 * 4 * 3 * factorial(2)
             = 5 * 4 * 3 * 2 * factorial(1)
             = 5 * 4 * 3 * 2 * 1 * factorial(0)
             = 5 * 4 * 3 * 2 * 1 * 1
             = 120

'''


def sum(n):  #1~n
    if n==0:
        return 0
    else:
        return n+sum(n-1)


result=sum(10)
print(result)




s=0
for i in range(11):
    s+=i
print(s)


