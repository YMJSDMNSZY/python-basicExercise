
'''


Alt+�س���  �ɿ��ٵ�����Ӧ����ģ��


��python�У�ģ���Ǵ�����֯��һ�ַ�ʽ���ѹ�������ĺ���������ŵ�һ���ļ��У�һ���ļ�(.py��
����һ��ģ�顣ģ���������ļ���ȥ����׺py��
�������ĺô���:
�C��ߴ���Ŀɸ��á���ά���ԡ�һ��ģ���д�����󣬿��Ժܷ������������Ŀ�е���
һ�����������ͻ����ͬģ������ͬ�����������ͻ


���ñ�׼��:
��׼��
˵��

builtins
�ڽ�����Ĭ�ϼ���
math
��ѧ��
random
random.random()  ������0-1֮������С��
random.randrange(step,stop,step)
random.randint(1,10)  ���������
random.randchoice(���б�)  ���ѡ���б������
random.shuffle() ϴ�ƣ��������

#��֤�� ��д��ĸ�����ֵ����
def func():
    code=''
    for i in range(4):
        ran1=str(random.randint(0,9))
        ran2=chr(random.randint(65,90))#������ת��ASCII��   ord():����Ӧ��ASCII��ת�ɶ�Ӧ���ַ�
        ran3=chr(random.randint(97,122))
        r=random.choice([ran1,ran2,ran3 ])
        code+=r
    return code
code=fun()
print(code)


���������
time


t=time.time()������ʱ���   time.ctime(t)����ʱ���ת���ַ�������ʽ  time.sleep(��) ���ӳ�ִ��
time.localtime(t):��ʱ��ת��Ԫ�����ʽ��Ԫ��������ꡢ�¡��ա�ʱ���֡������Ϣ
�����Ǹ�����Ļ�����.tm.mday  .tm_hour  �õ���Ӧ��Ҫ��ֵ
time.mktime() :��Ԫ��ʱ��ת��ʱ�������ʽ
strftime()���������ڽ�ʱ��Ԫ���ʱ�����ʽ��Ϊָ�����ַ����������ظ�ʽ������ַ�����  ʾ��('%Y-%m-%d %H:%M:%S')
strptime()���������ڽ�ָ�����ַ�������Ϊʱ��Ԫ�顣

�������ϳ��õĺ���֮�⣬timeģ�黹�ṩ��һЩ�࣬����struct_time��(struct_time��Python�е�һ������ģ�飬���ڱ�ʾʱ�䡣
����һ������9�����Ե�Ԫ�飬�ֱ�Ϊ���ꡢ�¡��ա�ʱ���֡��롢�ܼ���һ���еĵڼ��졢����ʱ��
struct_timeͨ����timeģ��һ��ʹ�ã�����ʱ���ת���ͼ��㡣
���磬����ʹ��time.localtime()��������ǰʱ��ת��Ϊstruct_time��ʽ��
��ʹ��time.mktime()��struct_time��ʽ��ʱ��ת��Ϊʱ�����)��

monotonic()����(monotonic()������Python��timeģ���е�һ�����������ڻ�ȡһ������������ʱ��ֵ��
���ʱ��ֵ�����ܵ�ϵͳʱ���Ӱ�죬Ҳ�����ܵ�ʱ�ӵ�����Ӱ�죬�������һ���ɿ���ʱ��Դ��
����������ص�ʱ��ֵ��һ������������λΪ�롣����ĳ��δָ����ʱ��㿪ʼ���㣬
ÿ�ε��ö��᷵��һ������һ�ε��õ�ֵ�������ֵ��������ǵ��������ġ�
�������ͨ�����ڼ���ʱ��������Ϊ�����Ա�֤�����׼ȷ�Ժ;��ȡ�)��

perf_counter()����(`perf_counter` �� Python �е�һ����ʱ�����������ڲ�������ִ�е�ʱ�䡣
������һ������������ʾ�Գ��������𾭹������������и߾��ȺͿ���ֲ�ԡ�
��������ʱ���������� `time()`����ͬ���ǣ�`perf_counter` �ľ��ȸ����Ҳ���ϵͳʱ�ӵ�����Ӱ�죬
��˸��ʺ��������ܷ����ͻ�׼���ԡ�һ��ʹ�� `perf_counter` ��������ִ��ʱ���ʾ����
import time
start_time = time.perf_counter()

# ִ�д���
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"����ִ��ʱ��Ϊ {elapsed_time:.6f} ��")
�������ʾ���У�`start_time` �� `end_time` �ֱ��¼����ʼ�ͽ�����ʱ�䣬
`elapsed_time` �������ִ�е�ʱ������������ִ��ʱ�䡣)�ȣ���Щ��ͺ����������ڸ��Ӹ߼���ʱ�䴦�������
��֮��timeģ����Python�д���ʱ�����Ҫģ�飬���ǿ��Ը��ݾ�������ͳ���ѡ����ʵĺ���������ʹ�á�
ʱ��




datetime

datetime.time.hour  ����ֻ�ܵõ�һ������
datetime.date.ctime(datetime.date(2019,6,20))

datetime.date.today() ��ʾ���� 2019-6-20
datetime.datetime.now() �õ���ǰ����ʱ��
datetime.timedelta(hours��weeks������ϵ�ʱ��)   ʱ���

#�ڻ������������Ӧ��  redis.set(key,value,ʱ���)    �Ự:session


���ں�ʱ��
calendar
����
hashlib
md5��Python���õ�һ�����ڼ���MD5��ϣֵ��ģ�飬�����Խ����ⳤ�ȵ�����ת��Ϊһ��128λ�Ĺ�ϣֵ��
hexdigest()��md5ģ���е�һ�����������ڷ��ؼ�����Ĺ�ϣֵ��ʮ�������ַ�����ʾ�������÷����£�
import hashlib
# ����md5����
md5 = hashlib.md5()
# ���¹�ϣֵ
md5.update(b'Hello, world!')
# ��ȡ��ϣֵ��ʮ�������ַ�����ʾ
hash_str = md5.hexdigest()
print(hash_str)  # 3e25960a79dbc69b674cd4ec67a72c62

���ϴ������ȵ�����hashlibģ�飬Ȼ�󴴽���һ��md5����
���ţ�ʹ��update()�������ϣֵ�и������ݣ�������µ���Hello, world!�ַ������ֽ��롣
���ʹ��hexdigest()������ȡ������Ĺ�ϣֵ��ʮ�������ַ�����ʾ���������ӡ������
��Ҫע����ǣ�hexdigest()�������ص���һ���ַ�����������һ�����֡������Ҫ����ת��Ϊ���֣�
����ʹ��int()��������ת�������磺
import hashlib
md5 = hashlib.md5()
md5.update(b'Hello, world!')
hash_str = md5.hexdigest()
hash_num = int(hash_str, 16)
print(hash_num)  # 87295857789884204908247555443101460258

���ϴ����У�ʹ��int()��������ϣֵ��ʮ�������ַ�����ʾת��Ϊһ���������������ӡ������
hashlib.md5(msg.encode('utf-8')) #md5�����㷨
md5.hexdigest()     #������֮��������Ϣת��16����  md5��32λ��   �����ѶȽϸ�   base64�������߼��ܽ���


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



�����㷨
copy
����
functeols
���õĹ���
os
����ϵͳ�ӿ�
re

match  �ӿ�ͷƥ��
search  ֻ����һ��
findall  ��������
sub  ��ʾ�滻sub(������ʽ���������ݡ���string)
split ���зָ�  result=re.split(r'[:,]','java:234,python:837')
        ��ʾ���ַ��������������ض����ַ��ͷָ�һ�²����浽�б���

�ַ�������ƥ��
sys��   sys.argv(���г���ʱ�Ĳ�����argv��һ���б�)  sys.path  sys.version
Python��������л���
multiprocessing
�����
threading
���߳�
json
����ͽ���JSON ����
logging
��¼��־������
timedelta  ʱ���


1.�Զ���ģ��                ģ����.(������������)
2.ʹ��ϵͳһЩģ��
����ģ�飺
1.import ģ����
ģ����.���� ģ����.���� ģ����.��
2. from ģ���� import ����/����/��
�ڴ����п���ֱ��ʹ�ñ�������������
3.from ģ���� import*
    ��������ƻ�ȡ���ݣ�����ʹ��__all__=[ʹ��*���Է��ʵ�����]
4.������import����from�����Ὣģ������Ķ������س���
   �����뱻���ص���������ݣ������õİ�Ҫ����if __name__='__main__':  pass

һ�������ԷŶ��ģ��

from ... import *
from package import module
from package.module import (class or variable or function)



__init__�ļ����ã���������ʱ�򣬻�Ĭ��ִ�и��ļ��������
��ʼ������Ϣ�������к�����������ֻҪͨ��������ʱ����ʾ���


from ģ�� import *  ��ʾ����ʹ��ģ��������������ݣ����û�ж���_all_���еĶ����Է��ʣ�
��������������_all_,ֻ��__all__=['','']�б��п��Է��ʵ�

from �� import * ��ʾ�ð������ݣ�ģ�飩�ǲ��ܷ��ʣ�
����Ҫ��__init__.py�ļ��ж���__all__=[����ͨ��*���ʵ��������]



����������ѭ������İ취��
1.�ع�����
2�����������ŵ�������
3.�ѵ������ŵ�ģ�����









'''