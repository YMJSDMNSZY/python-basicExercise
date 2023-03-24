# -*- coding=utf-8 -*-
import re

'''
# 不需要引用分组的内容：
    result=re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>',msg)
    - `<([0-9a-zA-Z]+)>`: 匹配一个HTML标签的开始部分，其中`[0-9a-zA-Z]+`表示匹配一个或多个数字或字母字符，`<`和`>`表示标签的开始和结束。
    - `<([0-9a-zA-Z]+)>`: 匹配一个HTML标签的开始部分，与前一个标签的区别是使用了一个不同的捕获组。
    - `(.+)`: 匹配标签中间的内容，其中`.`表示匹配任意字符，`+`表示匹配一个或多个字符。
    - `</\2></\1>`: 匹配HTML标签的结束部分，其中`\2`表示对第二个捕获组的引用，`\1`表示对第一个捕获组的引用，`</`和`>`表示标签的开始和结束。
    
    这个正则表达式使用了捕获组来匹配标签的开始和结束部分，并使用`\1`和`\2`来引用这些捕获组。
    同时，使用了`$`符号来表示匹配整个字符串的结尾，以确保没有其他字符出现在HTML标签之后。

    print(result)
    print(result.group(1))



    (\w+)(\d+)   ------>分成了两组

#  引用分组匹配内容
    1.number   #\number 表示引用第number组的数据
        msg='<html><h1>abc</h1></html>'
        result=re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
        print(result)
        
        在分组的时候还可以结合| 来使用  ，其表示或者的意思
        
        
        
        （\w+）(\d*)  \1 \2  表示引用前面的内容

    2.?P<名字>
        msg='<html><h1>abc</h1></html>'
        result=re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)(.+)</(?P=name2)></(?P=name1)>',msg) 
        #正则表达式中的 `P` 是 Python 中的 `re` 模块中的一个特殊语法，用于给一个子表达式命名，方便后续引用。
        #在这个例子中，`P<name1>` 和 `P<name2>` 分别给两个子表达式命名为 `name1` 和 `name2`，
        #后面通过 `(?P=name1)` 和 `(?P=name2)` 引用这两个子表达式。这样做的好处是可以让正则表达式更加易读和易维护。
        
        print(result)
        # 1. `<(?P<name1>\w+)>`：匹配以`<`开头、以`>`结尾的标签，`(?P<name1>\w+)`表示将匹配的内容命名为`name1`，
        # `\w+`表示匹配至少一个字母、数字或下划线。
        # 2. `<(?P<name2>\w+)`：匹配以`<`开头、以空格结尾的标签，`(?P<name2>\w+)`表示将匹配的内容命名为`name2`，
        # `\w+`表示匹配至少一个字母、数字或下划线。
        # 3. `(.+)`：匹配任意字符，`+`表示匹配至少一个字符。
        # 4. `</(?P=name2)>`：匹配以`</`开头、以`>`结尾的标签，其中`(?P=name2)`表示引用前面命名为`name2`的匹配结果。
        # 5. `</(?P=name1)>`：匹配以`</`开头、以`>`结尾的标签，其中`(?P=name1)`表示引用前面命名为`name1`的匹配结果。
        # 整个正则表达式的意思是：匹配以`<name1>`开头、以`</name1>`结尾的标签，其中包含以`<name2>`开头、以`</name2>`结尾的标签，
        # 并且`name1`和`name2`的内容相同，`name2`标签中可以包含任意字符。
        
        
    （?P<name>\w+）  (?P=name)  
'''
msg='<html><h1>abc</h1></html>'
result=re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
print(result)

#替换示例sub  相当于replace
res=re.sub(r'\d+','90','java:99,python:199')
print(res)


def fun1(temp):
    num=temp.group()
    num1=int(num)+1
    return str(num1)


res=re.sub(r'\d+',fun1,'java:99,python:199')
print(res)


res01=result=re.split(r'[:,]','java:234,python:837')
print(res01)