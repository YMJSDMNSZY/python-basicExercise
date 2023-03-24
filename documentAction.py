# -*- coding=utf-8 -*-
# #文件操作
'''
文件上传
保存log

系统函数：
    open(file,mode:'rt',buffering,encoding)---->返回值：stream(管道)
    stream.read()--------->读取管道中的内容

    注意读取图片时的读取方式要是'rb'，默认是'rt'






在Python3中，文件操作是通过内置的open()函数来实现的。
open()函数返回一个文件对象，我们可以对该对象进行读取、写入等操作。
下面是一些常见的文件操作：

打开文件
file = open("filename.txt", "r")

以上打开了一个名为filename.txt的文件，以只读模式打开。
如果文件不存在，将会抛出FileNotFoundError异常。
以下是打开模式的几个常见选项：


"r": 只读模式，默认的模式。如果文件不存在，抛出异常。

"w": 写入模式，如果文件存在先清空文件，然后写入新内容。如果文件不存在，创建新文件。

"a": 追加模式，如果文件存在，在文件末尾追加新内容。如果文件不存在，创建新文件。

读取文件
file对象有几种读取文件内容的方法：

file.read()         # 读取整个文件，返回字符串
file.readline()     # 读取文件的一行，返回字符串
file.readlines()    # 读取整个文件，返回每行文本组成的列表

写入文件
file.write(str)     # 将字符串写入文件

关闭文件
file.close()        # 关闭文件

在Python3中，我们也可以使用with语句来自动处理文件的打开和关闭，
这样可以确保文件在使用完毕后被正确关闭。例如：
with open("filename.txt", "r") as file:
    # 对文件进行操作
# 文件自动关闭









目录操作
1. 创建目录
使用os.mkdir()函数可以创建一个新目录。


import os
# 创建目录
os.mkdir("new_dir")

2. 删除目录
使用os.rmdir()函数可以删除一个目录。注意，只有当目录为空时才能被删除。


import os
# 删除目录
os.rmdir("new_dir")

3. 判断目录是否存在
使用os.path.exists()函数可以判断一个目录是否存在。

import os
# 判断目录是否存在
if os.path.exists("dir"):
    print("目录存在")
else:
    print("目录不存在")

4. 列出目录下所有文件和子目录
使用os.listdir()函数可以列出目录下所有的文件和子目录。

import os
# 列出目录下所有文件和子目录
files = os.listdir("dir")
for file in files:
    print(file)

5. 改变当前工作目录
使用os.chdir()函数可以改变当前的工作目录。

import os
# 改变当前工作目录
os.chdir("new_dir")















os.path模块是Python中用于处理文件路径的模块。它可以帮助我们更方便地处理各种路径问题。
下面是一些常用的os.path模块的操作：

1. 获取文件名和目录名
使用os.path.basename()函数可以获取文件名，使用os.path.dirname()函数可以获取目录名。

import os
path = "/home/user/Desktop/test.txt"
# 获取文件名
filename = os.path.basename(path)
print(filename) # test.txt
# 获取目录名
dirname = os.path.dirname(path)
print(dirname) # /home/user/Desktop

2. 拼接路径
使用os.path.join()函数可以将多个路径拼接成一个完整的路径。

import os
path1 = "/home/user/Desktop"
path2 = "test.txt"
# 拼接路径
full_path = os.path.join(path1, path2)
print(full_path) # /home/user/Desktop/test.txt

3. 获取文件扩展名
使用os.path.splitext()函数可以获取文件扩展名。

import os
path = "/home/user/Desktop/test.txt"
# 获取文件扩展名
file_ext = os.path.splitext(path)[1]
print(file_ext) # .txt

4. 判断路径是否为文件或目录
使用os.path.isfile()函数可以判断路径是否为文件，
使用os.path.isdir()函数可以判断路径是否为目录。

import os
path = "/home/user/Desktop/test.txt"
# 判断路径是否为文件
is_file = os.path.isfile(path)
print(is_file) # True
# 判断路径是否为目录
is_dir = os.path.isdir(path)
print(is_dir) # False

5. 判断路径是否存在
使用os.path.exists()函数可以判断路径是否存在。

import os
path = "/home/user/Desktop/test.txt"
# 判断路径是否存在
if os.path.exists(path):
    print("路径存在")
else:
    print("路径不存在")


'''

# stream=open(r'./ttt.txt','rt')
# # container=stream.read()
# # print(container)
# result=stream.readable() #判断是否可读
# print(result)
# #
# # while True:
# #     line=stream.readline()#读一行
# #     print(line)
# #     if not line:
# #         break
#
#
# lines=stream.readlines()#读多行
# print(lines) #保存在列表中
#
# for i in lines:
#     print(i)


#
# #写文件
# stream=open(r'./ttt.txt','w')  #若变成‘a’，只会在后面进行追加内容
#
# #mode是w，就是对文件进行写操作
# #mode='a'，不会清空文件在其后面进行追加操作
#
# s='''
# hello!
#    欢迎来到我的世界！
#
# '''
# result=stream.write(s)
# # print(result)
#
#
# stream.write('恢复IE晚饭后和人工\n')
# stream.writelines(['111\n','222\n','333\n']) #可迭代，没有换行效果，需要自己加换行符
#
# stream.close()

#
#
# with open(r'./ttt.txt','r') as stream:   #with结合open使用，会帮我们自动释放资源
#     container=stream.read()#读取文件中的内容
#
#     with open(r'./ccc.txt','w') as wstream:
#         wstream.write(container)
#
# print('文件复制完成')


# 复制文件夹：要用到os模块（operating system）
# 模块：xxx.py 就是一个模块
import os

#
# path=os.path.dirname(__file__)  #获取当前文件的目录文件夹类似os.getcwd()
# -  拿到当前文件的绝对路径 用os.path.abspath
# # print(path)
# # print(type(path))
# #
# #
#
# result=os.path.join(path,'ttt/ttt.txt')
# print(result)

#
#
# with open(r'.\ttt\ttt.txt','r') as stream:   #with结合open使用，会帮我们自动释放资源
#     container=stream.read()#读取文件中的内容
#     print(stream.name)
#     file=stream.name
#     filename=file[file.rfind('\\')+1:] #截取文件名
# 这段代码的作用是从一个带有路径的文件名中截取出文件名部分，去掉路径信息。
# file.rfind('\\')是找到最后一个反斜杠的位置，+1是为了把反斜杠本身排除掉，
# 然后使用切片操作file[file.rfind('\\')+1:]获取从反斜杠后一位开始到末尾的子字符串。
# 这样就得到了文件名部分。
#和os.path.split()功能一致


#     path=os.path.dirname(__file__)
#     path1=os.path.join(path,filename)
#     with open(path1,'w') as wstream:
#         wstream.write(container)


#
# r=os.path.isabs('ccc\ccc.txt')#在该代码文件同级的文件可以这样写
# print(r)
#
# path=r'D:\Python基础代码练习\python-basicExercise\ttt\ttt.txt'
# result=os.path.split(path)
# print(result[1])
#
# result=os.path.splitext(path)#分割文件名和扩展名
# print(result)

#
# size=os.path.getsize(path)
# print(size)
#
#
# result=os.path.join(os.getcwd(),'file','ccc2.txt')
# print(result)


# os里面的函数
# dir=os.getcwd()
# print(dir)
#
#
# all=os.listdir(r'D:\Python基础代码练习') #返回指定目录下的所有的文件文件夹，将其保存在一个列表中
# print(all)

#
# #创建文件夹
# os.makedir(r'')
# 删除文件夹（只能删除空文件夹）
# os.rmdir()
# #批量删除空文件夹
# os.removedirs()


# path=r'...'
# filelist=os.listdir(path=r'...')
# for file in filelist:
#     path1=os.path.join(path,file)
#
#     os.remove(path1)#删除文件
# else:
#     os.rmdir(path)
#
# print('删除成功')

#
# #切換目錄
# f=os.chdir(...)
# print(f)


# copy.py
# 文件复制

src_path = r'..\ccc\ccc.txt'
target_path = r'..\ttt\ttt.txt'


# 封装成函数
def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)

        for file in filelist:
            path = os.path.join(src, file)

            with open(path, 'r') as rstream:
                container = rstream.read()

                path1 = os.path.join(target, file)
                with open(path1, 'w') as wstream:
                    wstream.write(container)
    else:
        print('复制完毕！！！')


# 调用函数
copy(src_path, target_path)
