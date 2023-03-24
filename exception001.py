# -*- coding=utf-8 -*-
#异常：没有语法错误红色报错  真正运行的时候报的错就叫做异常
#只要出现异常，下面的就不会打印出来，所以要进行异常处理

#异常处理：
'''
try:
    可能出现异常的代码
except:
    如果有异常处理的代码
finally:
    无论是否存在异常都会被执行的代码   文件操作，数据库操作的时候要将内存释放，close()   这时候会用到
'''

# def func():
#     try:
#         a=int(input('输入第一个数字：'))
#         b = int(input('输入第二个数字：'))
#
#         per=input('输入运算符+ - * /')
#         result=0
#         if per=='+':
#             result=a+b
#         elif per=='-':
#             result=a-b
#         elif per=='*':
#             result=a*b
#         elif per=='/':
#             result=a/b
#         else:
#             print('符号输入错误！！！')
#         print('结果是：',result)
#     # except ZeroDivisionError:
#     #     print('除数不能为零！！！')
#     # except ValueError:
#     #     print('必须输入数字！！！')
#     except Exception as err:
#         print('出错了！！！',err)
#
# func()



#try...finally异常举例
def func():
    stream=None
    try:
        stream=open(r'...')
        container=stream.read()
        print(container)
    except Exception as err:
        print(err)
    finally:
        print('--finally---')
        if stream:
            stream.close()
        return 3#
func()


