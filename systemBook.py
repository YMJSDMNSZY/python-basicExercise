#-*- coding=utf-8 -*-
#用户注册
def register():

    username=input('输入用户名:')
    password=input('请输入密码:')
    repassword=input('请输入确认密码')


    if password==repassword:
        #保存信息
        with open(r'user.txt','a') as wstream:
            wstream.write('{} {}\n'.format(username,password))

        print('用户保存成功！')
    else:
        print('密码不一致，请重新输入！')

def login():
    username = input('输入用户名:')
    password = input('请输入密码:')
    if username and password:
        with open(r'user.txt','rb') as rstream:
            while True:
                use_info=rstream.readline()
                if not use_info:
                    print('用户名或密码有误有误！！！')
                    break
                inputuser_info='{} {}\n'.format(username,password)
                if use_info==inputuser_info:
                    print('用户登陆成功！！！')
                    break

def show_books():
    print('--------图书馆里面的图书有：-------------')
    with open(r'books.txt') as rstream:
        books=rstream.readlines()
        for book in books:

            print(book,end='')

# #调用函数
# register()
# login()
show_books()
