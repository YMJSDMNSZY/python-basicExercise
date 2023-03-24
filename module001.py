
'''


Alt+回车键  可快速导入相应包或模块


在python中，模块是代码组织的一种方式，把功能相近的函数或者类放到一个文件中，一个文件(.py）
就是一个模块。模块名就是文件名去掉后缀py。
这样做的好处是:
–提高代码的可复用、可维护性。一个模块编写完主后，可以很方便的在其他项目中导入
一解决了命名冲突，不同模块中相同的命名不会冲突


常用标准库:
标准库
说明

builtins
内建函数默认加载
math
数学库
random
random.random()  会生成0-1之间的随机小数
random.randrange(step,stop,step)
random.randint(1,10)  随机生成数
random.randchoice(放列表)  随机选择列表的内容
random.shuffle() 洗牌，打乱组合

#验证码 大写字母与数字的组合
def func():
    code=''
    for i in range(4):
        ran1=str(random.randint(0,9))
        ran2=chr(random.randint(65,90))#将数字转成ASCII码   ord():将对应的ASCII码转成对应的字符
        ran3=chr(random.randint(97,122))
        r=random.choice([ran1,ran2,ran3 ])
        code+=r
    return code
code=fun()
print(code)


生成随机数
time


t=time.time()：返回时间戳   time.ctime(t)：将时间戳转成字符串的形式  time.sleep(秒) ：延迟执行
time.localtime(t):将时间转成元组的形式，元组包含了年、月、日、时、分、秒等信息
可在那个上面的基础上.tm.mday  .tm_hour  得到对应想要的值
time.mktime() :将元组时间转成时间戳的形式
strftime()函数：用于将时间元组或时间戳格式化为指定的字符串，并返回格式化后的字符串。  示例('%Y-%m-%d %H:%M:%S')
strptime()函数：用于将指定的字符串解析为时间元组。

除了以上常用的函数之外，time模块还提供了一些类，例如struct_time类(struct_time是Python中的一个内置模块，用于表示时间。
它是一个包含9个属性的元组，分别为：年、月、日、时、分、秒、周几、一年中的第几天、夏令时。
struct_time通常与time模块一起使用，用于时间的转换和计算。
例如，可以使用time.localtime()函数将当前时间转换为struct_time格式，
或使用time.mktime()将struct_time格式的时间转换为时间戳。)、

monotonic()函数(monotonic()函数是Python中time模块中的一个函数，用于获取一个单调递增的时间值。
这个时间值不会受到系统时间的影响，也不会受到时钟调整的影响，因此它是一个可靠的时间源。
这个函数返回的时间值是一个浮点数，单位为秒。它从某个未指定的时间点开始计算，
每次调用都会返回一个比上一次调用的值更大的数值，因此它是单调递增的。
这个函数通常用于计算时间间隔，因为它可以保证计算的准确性和精度。)、

perf_counter()函数(`perf_counter` 是 Python 中的一个计时器函数，用于测量程序执行的时间。
它返回一个浮点数，表示自程序运行起经过的秒数，具有高精度和可移植性。
与其他计时器函数（如 `time()`）不同的是，`perf_counter` 的精度更高且不受系统时钟调整的影响，
因此更适合用于性能分析和基准测试。一个使用 `perf_counter` 测量程序执行时间的示例：
import time
start_time = time.perf_counter()

# 执行代码
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"程序执行时间为 {elapsed_time:.6f} 秒")
在上面的示例中，`start_time` 和 `end_time` 分别记录程序开始和结束的时间，
`elapsed_time` 计算程序执行的时间差，最后输出程序执行时间。)等，这些类和函数可以用于更加高级的时间处理操作。
总之，time模块是Python中处理时间的重要模块，我们可以根据具体需求和场景选择合适的函数和类来使用。
时间




datetime

datetime.time.hour  这样只能得到一个对象
datetime.date.ctime(datetime.date(2019,6,20))

datetime.date.today() 表示今天 2019-6-20
datetime.datetime.now() 得到当前日期时间
datetime.timedelta(hours或weeks或其组合的时间)   时间差

#在缓存机制上有所应用  redis.set(key,value,时间差)    会话:session


日期和时间
calendar
日历
hashlib
md5是Python内置的一个用于计算MD5哈希值的模块，它可以将任意长度的数据转换为一个128位的哈希值。
hexdigest()是md5模块中的一个方法，用于返回计算出的哈希值的十六进制字符串表示。具体用法如下：
import hashlib
# 创建md5对象
md5 = hashlib.md5()
# 更新哈希值
md5.update(b'Hello, world!')
# 获取哈希值的十六进制字符串表示
hash_str = md5.hexdigest()
print(hash_str)  # 3e25960a79dbc69b674cd4ec67a72c62

以上代码首先导入了hashlib模块，然后创建了一个md5对象。
接着，使用update()方法向哈希值中更新数据，这里更新的是Hello, world!字符串的字节码。
最后，使用hexdigest()方法获取计算出的哈希值的十六进制字符串表示，并将其打印出来。
需要注意的是，hexdigest()方法返回的是一个字符串，而不是一个数字。如果需要将其转换为数字，
可以使用int()函数进行转换。例如：
import hashlib
md5 = hashlib.md5()
md5.update(b'Hello, world!')
hash_str = md5.hexdigest()
hash_num = int(hash_str, 16)
print(hash_num)  # 87295857789884204908247555443101460258

以上代码中，使用int()函数将哈希值的十六进制字符串表示转换为一个整数，并将其打印出来。
hashlib.md5(msg.encode('utf-8')) #md5加密算法
md5.hexdigest()     #将加密之后的相关信息转成16进制  md5是32位的   解密难度较高   base64可以在线加密解密


password='123456'
list1=[]
sha256=hashlib.sha256(password.encode('utf-8'))
list1.append(sha256.hexdigest())
pwd=input('Enter your password,Please')
sha256=hashlib.sha256(pwd.encode('utf-8'))
pwd=sha256.hexdigest()
print(pwd)
for i in list1:
    if pwd==i
    print('login success!!!')



加密算法
copy
拷贝
functeols
常用的工具
os
操作系统接口
re

match  从开头匹配
search  只查找一次
findall  查找所有
sub  表示替换sub(正则表达式，’新内容‘，string)
split 进行分割  result=re.split(r'[:,]','java:234,python:837')
        表示在字符串搜索中遇到特定的字符就分割一下并保存到列表中

字符串正则匹配
sys：   sys.argv(运行程序时的参数，argv是一个列表)  sys.path  sys.version
Python自身的运行环境
multiprocessing
多进程
threading
多线程
json
编码和解码JSON 对象
logging
记录日志，调试
timedelta  时间差


1.自定义模块                模块名.(变量或函数或类)
2.使用系统一些模块
导入模块：
1.import 模块名
模块名.变量 模块名.函数 模块名.类
2. from 模块名 import 变量/函数/类
在代码中可以直接使用变量，函数，类
3.from 模块名 import*
    如果想限制获取内容，可以使用__all__=[使用*可以访问的内容]
4.无论是import还是from，都会将模块里面的东西加载出来
   若不想被加载调用相关内容，被引用的包要加上if __name__='__main__':  pass

一个包可以放多个模块

from ... import *
from package import module
from package.module import (class or variable or function)



__init__文件作用：当导包的时候，会默认执行改文件里的内容
初始化的信息，对其中函数，变量名只要通过导包的时候访问就行


from 模块 import *  表示可以使用模块里面的所有内容，如果没有定义_all_所有的都可以访问，
但是如果添加上了_all_,只有__all__=['','']列表中可以访问的

from 包 import * 表示该包中内容（模块）是不能访问，
就需要在__init__.py文件中定义__all__=[可以通过*访问的相关内容]



！！！避免循环导入的办法：
1.重构代码
2．将导入语句放到函数中
3.把导入语句放到模块最后









'''