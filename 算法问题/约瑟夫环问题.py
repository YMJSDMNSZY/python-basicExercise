# -*- coding=utf-8 -*-
#约瑟夫环问题
'''
Josephu环(约瑟夫环)
30个人坐船出海(15个基督徒和15个非基督徒)，船坏了需要把15个人扔到海里，30人围成一圈，从某个人从1开始报数，报到9的人就扔到海里面，下一个人继续从1开始报数，以此类推，直到把15个人扔到海里面。结果由于上帝的保佑，15个基督徒都幸存下来，问开始怎么站的，哪些位置是基督徒，哪些位置是非基督徒。
冒泡排序–两两比较，前面比后面大就交换位置35，12，99，18，57，66，43，32，9012，35，18，57，66，43，32，90，99

'''
# 约瑟夫环问题是一个经典的问题，题目描述如下：

# 有n个人围成一圈，从第一个人开始报数，报到m的人出圈，剩下的人继续从1开始报数，报到m的人出圈，以此类推，直到所有人都出圈，请输出出圈顺序。


# def main():
#     persons =[True] *30
#     index, num, counter = 1000,1000,1000
#     while counter < 15:
#         if persons[index]:
#             num +=1
#             if num == 9:
#                 persons[index] = False
#                 counter+= 1
#                 num = 0
#     index +=1
#     index %=30
#     for pos,person in enumerate(persons):
#         print(pos,'基'if person else '非')
#
# if __name__ == '__main__':
#     main()
#


def josephus(n, m):
    """
    :param n: 总人数
    :param m: 报到m的人出圈
    :return: 出圈顺序
    """
    # 初始化人员编号
    people = list(range(1, n + 1))
    # 初始化报数位置
    pos = 0
    # 开始报数
    while len(people) > 0:
        # 计算出下一个出圈的人的位置
        pos = (pos + m - 1) % len(people)
        # 输出出圈的人的编号
        print(people.pop(pos), end=' ')
    print()

josephus(10, 3)