# encoding = 'utf-8'
#-*- coding=utf-8 -*-

from selenium import webdriver
import time
import re
from selenium.webdriver.common.by import By
import pandas as pd
import os


def close_windows():

    try:
        dr.implicitly_wait(20)  # 智能等待20秒，等待页面的元素加载出来后，就继续执行，下同
        if dr.find_element(By.XPATH, '//div[@class="boss-login-dialog"]//i[@class="icon-close"]'):
            dr.find_element(By.XPATH, '//div[@class="boss-login-dialog"]//i[@class="icon-close"]').click()
            # 13 14行代码的作用是判断是否有弹出登录框，如果弹出登录框则右上角的关闭按钮，若无则跳过执行并告知没有弹窗
    except BaseException as e:
        print('close_windows,没有弹窗', e)


def get_current_region_job(k_index, query, city_no):
    # 该函数的作用是获取指定城市指定区域的岗位信息
    # 北京101010100
    # 上海101020100
    # 杭州101210100
    flag = 0
    df_empty = pd.DataFrame(columns=['岗位', '地点', '薪资', '工作经验', '学历', '公司', '技能'])

    global dr
    # dr = webdriver.Chrome(executable_path='/Users/liulinghua/PycharmProjects/NickProject/venv/chromedriver')
    dr = webdriver.Chrome(executable_path='D:\Python3.10/chromedriver.exe')
    # 将浏览器最大化显示
    dr.maximize_window()

    # 转到目标网址
    dr.get("https://www.zhipin.com/c101010100/?query={0}&ka=sel-city{1}".format(query, city_no))  # 北京
    print("打开网址")
    time.sleep(5)
    while (flag == 0):
        close_windows()
        dr.implicitly_wait(20)
        job_list = dr.find_elements(By.XPATH, '//ul[@class="job-list-box"]/li')  # 这里是获取所有的岗位信息块
        for job in job_list:  # 获取当前页的职位30条
            job_name = job.find_element(By.CSS_SELECTOR, '.job-name').text  # 获取岗位名称
            job_area = job.find_element(By.CSS_SELECTOR, '.job-area').text  # 获取岗位所在地区
            salary = job.find_element(By.CSS_SELECTOR, '.salary').text  # 获取薪资
            experience_education = job.find_element(By.XPATH, '//div[@class="job-info clearfix"]/ul[@class="tag-list"]')
            experience_education_list = experience_education.find_elements(By.TAG_NAME, 'li')
            if len(experience_education_list) != 2:
                print('experience_education_list不是2个，跳过该数据', experience_education_list)
                break
            experience = experience_education_list[0].text
            education = experience_education_list[1].text
            # 上面31-37行代码是获取工作经验和学历要求
            dr.implicitly_wait(20)
            company = job.find_element(By.CSS_SELECTOR, '.company-name').text  # 获取公司名
            dr.implicitly_wait(20)
            skill_div = job.find_element(By.CSS_SELECTOR, '.job-card-footer')
            skill_list = skill_div.find_elements(By.TAG_NAME, "li")
            skill = []  # 存储技能的列表skill
            for skill_i in skill_list:
                skill_i_text = skill_i.text
                if len(skill_i_text) == 0:
                    continue
                skill.append(skill_i_text)
            print("job_skill:", skill)
            # 39-50行代码是获取岗位的技能要求

            df_empty.loc[k_index, :] = [job_name, job_area, salary, experience, education, company, skill]
            k_index = k_index + 1
            print("已经读取数据{}条".format(k_index))
        close_windows()
        try:  # 点击下一页
            dr.implicitly_wait(20)
            cur_page_num = dr.find_element(By.XPATH,
                                           '//div[@class="options-pages"]//a[@class="selected"]').text  # 当前所在页面的按钮上的数字
            print('cur_page_num:', cur_page_num)
            # 点击下一页
            dr.implicitly_wait(20)
            element = dr.find_element(By.XPATH, '//i[@class="ui-icon-arrow-right"]')  # 找到点击下一页的按钮
            dr.implicitly_wait(20)
            dr.execute_script("arguments[0].click();", element)
            dr.implicitly_wait(20)
            new_page_num = dr.find_element(By.XPATH,
                                           '//div[@class="options-pages"]//a[@class="selected"]').text  # 点击下一页按钮后，当前所在页面的按钮上的数字
            print('new_page_num', new_page_num)
            if cur_page_num == new_page_num:  # 如果当前页面与最新页面的数字一致，则表示已经是最后一页，跳出循环
                flag = 1
                break
        except BaseException as e:
            print('点击下一页错误', e)
            break
    dr.quit()
    # 退出浏览器
    print(df_empty)
    # 写入数据到CSV中
    if os.path.exists("数据.csv"):  # 存在追加，不存在创建
        df_empty.to_csv('数据.csv', mode='a', header=False, index=None, encoding='gb18030')
    else:
        df_empty.to_csv("数据.csv", index=False, encoding='gb18030')

    return k_index


if __name__ == '__main__':
    # get_current_region_job(0,'电竞','101210100')#杭州
    # get_current_region_job(0, '电竞', '101020100')  # 北京
    # 北京101020100
    # 上海101010100
    # 杭州101210100
    # 想要获取其他职位，其他城市，替换搜索关键词或BOSS上对应的城市代号即可
    get_current_region_job(1, '自动化测试', '101020100')