# -*- coding=utf-8 -*-
'''
面向对象：
程序   现实中
对象----->具体的事物


好处：


面向对象：
    类
    对象
    属性
    方法

对象：
某某的手机.......

对象的集合----->共同特征：品牌 颜色 大小 价格
            可以实现的特征：打电话  发短信  上网 游戏


类别:手机类
    学生类
    特征:性别 年龄 姓名  身高 血型 婚否   ----->属性
    动作：刷抖音 敲代码 看书...         ------>方法
    多个对象---->提取对象的共同特征和动作----->封装到一个类中


'''
#所有的类名要求首字母大写，多个单词使用驼峰式命名法
#ValueError  TypeError StopIterable

# class Phone:
#     pass
#     #属性
#     #brand=''
#     brand='HUAWEI'
#     #方法
#
# print(Phone)
#
#
# yp=Phone()
# print(yp)
# print(yp.brand)
# yp.brand='IPHONE'
# print(yp.brand)
#
#
# feifei=Phone()
# print(feifei)
# print(feifei.brand)
#
# xiaowei=Phone()
# print(xiaowei.brand)



#类中的方法:动作
#种类：普通方法： def 方法(参数)  类方法 静态方法 魔术方法
class Phone:
    #魔术方法之一  __名字__()
    # 1.找有没有一块空间是Phone
    # 2.利用Phone类, 向内存申请一块
    # 'Phone一样空间。0x78349nabc
    # 3.去Phone中找有没有__init_.如果没有则执行将开辟内存给对象名: p
    # 4.如果有_init_, 则会进入 init方法执行里面动作。将内存地址赋给p

    def __init__(self):#初始化
        print('-----------init')
        self.brand='xiaomi'
        self.price=472864
    brand='xiaomi'
    price=23243
    type='mate 80'
    def call(self):
        print('self-------->',self)
        print('正在访问通讯录：')
        for person in self.address_book:#不能保证每个self都存在通讯录
            for name,number in person.items():

                print('联系人：{}，电话号码:{}'.format(name,number))
        print('正在打电话.........',self.note)

phone1=Phone()
phone1.note='我是phone1的note'
phone1.address_book=[{'hfeu':'与纯净水'},{'62446828':'比较差的话'}]
print(phone1,'----1')
# print(phone1.brand)
phone1.call()

phone2=Phone()
print('*'*238)
print(phone2,'----2')
phone2.note='我是phone2的note'
phone2.address_book=[{'twrurw':'与纯水'},{'626828':'比差的话'}]
phone2.call()

phone3=Phone()
phone3.price=47382
print(phone3.price)