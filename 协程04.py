# -*- coding=utf-8 -*-

#协程案例
import requests
import gevent
from gevent import monkey
import urllib.request


monkey.patch_all() #(subprocess=False)
def download(url):

    response=urllib.request.urlopen(url)
    content=response.read()
    print('下载了{}的数据，长度为{}'.format(url,len(content)))


if __name__ == '__main__':
    urls=['http://www.163.com','http://www.qq.com','http://www.baidu.com']
    # g1=gevent.spawn(download,urls[0])
    # g2=gevent.spawn(download,urls[1])
    # g3=gevent.spawn(download,urls[2])
    greenlets = [gevent.spawn(download, url) for url in urls]

    gevent.joinall(greenlets)