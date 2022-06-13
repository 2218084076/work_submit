# coding=utf-8
import random
import time
from typing import Any

import pandas as pd
from playwright.sync_api import Playwright
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Spider:

    def __init__(self):
        self.url = 'https://b2b.11467.com/'  # 公司黄页
        self.browser = None
        self.response = None

    def make_spider(self, playwright: Playwright):
        self.browser = playwright.webkit.launch(headless=False)
        page = self.browser.new_context().new_page()
        self.response = page.goto(self.url)


company_sort = ['https://b2b.11467.com/search/3338.htm', 'https://b2b.11467.com/search/3339.htm',
                'https://b2b.11467.com/search/3340.htm', 'https://b2b.11467.com/search/3341.htm',
                'https://b2b.11467.com/search/3342.htm', 'https://b2b.11467.com/search/3343.htm',
                'https://b2b.11467.com/search/3344.htm', 'https://b2b.11467.com/search/3345.htm',
                'https://b2b.11467.com/search/3346.htm', 'https://b2b.11467.com/search/3347.htm',
                'https://b2b.11467.com/search/3348.htm', 'https://b2b.11467.com/search/3349.htm',
                'https://b2b.11467.com/search/3350.htm', 'https://b2b.11467.com/search/3351.htm',
                'https://b2b.11467.com/search/3352.htm', 'https://b2b.11467.com/search/3353.htm',
                'https://b2b.11467.com/search/3354.htm', 'https://b2b.11467.com/search/3355.htm',
                'https://b2b.11467.com/search/3356.htm', 'https://b2b.11467.com/search/3357.htm',
                'https://b2b.11467.com/search/3358.htm', 'https://b2b.11467.com/search/3359.htm',
                'https://b2b.11467.com/search/3360.htm', 'https://b2b.11467.com/search/3361.htm',
                'https://b2b.11467.com/search/3362.htm', 'https://b2b.11467.com/search/3363.htm',
                'https://b2b.11467.com/search/3364.htm', 'https://b2b.11467.com/search/3365.htm',
                'https://b2b.11467.com/search/3366.htm', 'https://b2b.11467.com/search/3367.htm',
                'https://b2b.11467.com/search/3368.htm', 'https://b2b.11467.com/search/3369.htm',
                'https://b2b.11467.com/search/3371.htm', 'https://b2b.11467.com/search/3372.htm',
                'https://b2b.11467.com/search/3374.htm', 'https://b2b.11467.com/search/11739.htm',
                'https://b2b.11467.com/search/12104.htm']  # 一级分类
chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)


# browser.get('https://b2b.11467.com/search/11739.htm')
# time.sleep(random.randint(1, 3))
# company_sort: list = []


# all_box = browser.find_elements(By.CLASS_NAME, 'content')[0].find_elements(By.TAG_NAME, 'a')
# for i in all_box:
#     sort_url = i.get_attribute('href')
#     time.sleep(random.randint(1, 5))
#     company_sort.append(sort_url)
#     print(sort_url)
# print(len(company_sort), company_sort)

def read_csv_file(file_name: str) -> list[Any]:
    """read csv file"""
    data = pd.read_csv(file_name, usecols=[0], encoding='utf-8')
    url_list = []
    for u in data.values.tolist():
        url_list.append(u[0])
    return url_list


l = read_csv_file('all_category.csv')
print(len(l))


def write_file(data_list: list, dest_file: str):
    """write to csv file"""
    with open('%s' % dest_file, 'w', newline='') as csvfile:
        for i in data_list:
            csvfile.write(i)
            csvfile.write('\n')


def crawl_mian_category(url: str) -> list:
    """crawl all city link"""
    browser.get(url)
    time.sleep(random.randint(1, 5))
    main_category_list = []
    most_category = browser.find_elements(By.CLASS_NAME, 'boxcontent')[0].find_elements(By.TAG_NAME, 'a')
    box_list = browser.find_elements(By.CLASS_NAME, 'boxcontent')[5].find_elements(By.TAG_NAME, 'a')
    vip_category = browser.find_elements(By.CLASS_NAME, 'sidesubcat')[0].find_elements(By.TAG_NAME, 'a')  # VIP最多的行业
    for city in box_list:
        time.sleep(random.uniform(0, 2))
        main_category_list.append(city.get_attribute('href'))
    for v in vip_category:
        time.sleep(random.uniform(0, 2))
        main_category_list.append(v.get_attribute('href'))
    for m in most_category:
        time.sleep(random.uniform(0, 2))
        main_category_list.append(m.get_attribute('href'))
    return main_category_list  # 273个一级分类


def crawl_all_company(company_sort_list: list):
    """
    抓取行业中所有企业主页链接
    """
    company_list = []
    page_info = browser.find_elements(By.CLASS_NAME, 'pages')[0].find_elements(By.TAG_NAME, 'a')
    page_num = int(page_info.pop().get_attribute('href').split('.htm')[0].split('-')[1])
    for sort in company_sort_list:
        browser.get(sort)
        time.sleep(random.uniform(0, 3))
        for p in range(page_num):
            box_list = browser.find_elements(By.CLASS_NAME, 'f_l')
            for box in box_list:
                company_link = box.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
                company_list.append(company_link)

            next_page = browser.find_elements(By.CLASS_NAME, 'pages')[0].find_elements(By.TAG_NAME, 'a')[
                -2].get_attribute(
                'href')
            browser.get(next_page)
            time.sleep(random.uniform(0, 3))
            print(len(company_list))
    return company_list


def parse(url: str):
    """Parse company homepage"""
    browser.get(url)
    time.sleep(random.randint(1, 5))


# def main():
#     """main"""
#     url_list = read_csv_file('all_category.csv')
#     for i in company_sort:
#         company_list = crawl_all_company(i)
#         write_file(company_list, 'company_urls.csv')


browser.quit()
