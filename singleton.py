# -*- coding=utf-8 -*-

class Singleton:
    #私有化
    __instance=None

    #重写__new__
    def __new__(cls, *args, **kwargs):
        # print('---------->new')
        # if cls.__instance is None:
        #     print('----->1')
        #
        #
        #     cls.__instance=object.__init__(cls)
        #     '''
        #     ----------->__new__
        #     ----->1
        #     None
        #     ----------->__new__
        #     ----->1
        #     None
        #     None
        #     None
        #     '''
        #
        #
        #     # cls.__instance=object.__new__(cls)
        #     '''
        #     ----------->__new__
        #     ----->1
        #     <__main__.Singleton object at 0x0000025BD074BF40>
        #     ----------->__new__
        #     ------>2
        #     <__main__.Singleton object at 0x0000025BD074BF40>
        #     <__main__.Singleton object at 0x0000025BD074BF40>
        #     '''
        #
        #
        #     print(cls.__instance)
        #     return cls.__instance
        #
        # else:
        #     print('------>2')
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance


s=Singleton()
s1=Singleton()

print(dir(Singleton))  #可以看它的方法
print(s)
print(s1)