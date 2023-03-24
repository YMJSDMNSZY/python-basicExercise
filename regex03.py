# -*- coding=utf-8 -*-
import re
import requests

# msg='abc123abc'
# res1=re.match(r'abc(\d+)',msg)   #这样是贪婪模式
# # res1=re.match(r'abc(\d+?)',msg)   #这样是非贪婪模式  加上?即可
# print(res1)


path='<img class="currentImg" src="https://t7.baidu.com/it/u=3435942975,1552946865&amp;fm=193&amp;f=GIF" width="1200" height="800" log-rightclick="p=5.102" title="点击查看图片来源" style="left: 117px; top: 0px; width: 466.5px; height: 311px; cursor: pointer;">'

image_path=re.match(r'<img class="currentImg" src="(.*)"',path)
# print(res1.group(1))

response=requests.get(image_path)
with open('aa.ipg','wb') as wstream:
    wstream.write(response.context)