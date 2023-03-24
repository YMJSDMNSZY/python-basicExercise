# -*- coding=utf-8 -*-

# qq_no=input('input your number')


'''
\A:表示从字符串的开始处匹配
\Z:表示从字符串的结束处匹配，如果存在换行，只匹配到换行前的结束字符串。
\b:匹配一个单词边界，也就是指单词和空格间的位置。
    例如， 'py\b’可以匹配' python”中的‘py'，但不能匹配“openyxl”中的 ‘py'
\B:匹配非单词边界。
    ‘py\b’可以匹配"openpyxl。”中的'py'，但不能匹配"python”中的 'py'。
\d:匹配任意数字，等价于[0-9]。
\D:匹配任意非数字字符，等价于[^\d]。
\s:匹配任意空白字符，等价于[\t\n\r\f]。
\S:匹配任意非空白字符，等价于[^\s]。
\w:匹配任意字母数字及下划线，等价于[a-zA-Z0-9_]。
\W:匹配任意非字母数字及下划线，等价于[^\w]
\\:匹配原义的反斜杠\。

‘.’用于匹配除换行符（\n）之外的所有字符。
'^'用于匹配字符串的开始，即行首。
‘$’用于匹配字符串的末尾（末尾如果有换行符\n，就匹配\n前面的那个字符），即行尾。
‘*’用于将前面的模式匹配0次或多次（贪婪模式，即尽可能多的匹配）
‘+’用于将前面的模式匹配1次或多次（贪婪模式)
‘?’用于将前面的模式匹配O次或1次（贪婪模式)
‘*?，+? ，? ?’即上面三种特殊字符的非贪婪模式（尽可能少的匹配）。
‘{m, n}’用于将前面的模式匹配m次到n次（贪婪模式），即最小匹配m次，最大匹配n次。
‘{m, n}?’即上面‘{m, n}’的非贪婪版本。
‘\\’:'\'是转义字符，在特殊字符前面加上\，特殊字符就失去了其所代表的含义，比如\+就仅仅代表加号+本身。
‘[]’用于标示一组字符,如果^是第一个字符，则标示的是一个补集。比如[0-9]表示所有的数字，[^0-9]表示除了数字外的字符。
‘|’比如A|B用于匹配A或B。
‘(...)’用于匹配括号中的模式，可以在字符串中检索或匹配我们所需要的内容。


总结：
. 任意字符，除\n
^ 开头
$ 结尾
[] 范围  [afswjf] [a-z] [a-z*&Y]
()  小括号表示分组

量词：
*  >=0
+  >=1
?  0,1

{m}    固定m位
{m,}   >=m
{m,n}  >=m <=n
'''


import re
# msg='娜扎热巴代斯佟丽娅'
#
# pattern=re.compile('佟丽娅')
#
# result=pattern.match(msg) #没有匹配成功返回None
# print(result)

# #正则使用示例：match
# s='娜扎佟丽娅热巴代斯'
# result=re.match('佟丽娅',s)  #一匹配不成功，就返回None
# print(result)
#
# result=re.search('佟丽娅',s)#进行正则匹配整个字符串  又叫查找
# print(result)
# print(result.span()) #返回位置
#
# print(result.group())#使用group提取到匹配的内容
# print(result.groups())

# # a2b h6k
# msg='gf2wuih2fihd2438h2gfe'
# # result=re.search('[0-9]+',msg)  #只要有匹配的，后面就不会进行匹配
# # print(result.group())
#
# result=re.findall('[a-z][0-9][a-z]',msg)  #会找出所有匹配的结果  匹配整个字符串直到结尾
# print(result)
#
#
# #qq 号码验证 5-11  开头不是0
# qq='41241'
# res=re.match('^[1-9][0-9]{4,10}$',qq)
# print(res)


# #用户名可以是字母或数字，不能是数字开头，用户名长度必须六位以上[0-9a-zA-Z]
# username='admin001'
# result=re.search('^[a-zA-Z]\w{5,}$',username)
# print(result)
#
# msg='aa.py ad.txt fswfe.png jvfdis.py'
# # res=re.findall('py\\b',msg)
# res=re.findall(r'\w*\.py\b',msg)  #加r或加\  防止出现转义
# print(res)
#
#
# #分组
# #匹配数字0-100数字
# n='109'
#
# # res=re.match(r'[1-9]+\d*',n)
#
# # 改进版
# res=re.match(r'[1-9]?\d?$|100$',n)
# print(res)

# #(word|word|word) 表示单词   区别  [qrwerwq]表示的是一个字母而不是一个单词
# #验证输入的邮箱  163 126 qq
# email='6723853629@qq.com'
# res=re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)$',email)
# print(res)
#
#

# #不是以4/7结尾的手机号码（11位）
# phone='13264778098'
# res=re.match(r'1\d{9}[0-35-689]$',phone)
# print(res.group())

#
#
# #爬虫相关
# phone='010-12345678'
#
# res=re.match(r'(\d{3}|\d{4})-(\d{8})$',phone) #小括号表示分组
# print(res)
#
# #分别提取
# print(res.group(1))
# print(res.group(2))
#
#
# #
msg='<html>abc</html>'
msg1='<h1>hello</h1>'

result=re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$',msg)
print(result)
print(result.group())

#结合number
result=re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$',msg1)
print(result)
print(result.group())