# -*- coding=utf-8 -*-

def register():
    username=input('请输入用户名：')
    if len(username)<6:
        raise Exception('用户名长度必须六位以上') #raise  自定义异常错误-即手动往外扔错误
    else:
        print('用户注册成功')


try:
    register()
except Exception as err:
    print(err)
    print('注册失败')
else:
    print('注册成功！！！')