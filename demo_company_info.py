# coding=utf-8
import random
import time

from playwright.sync_api import Playwright
from selenium import webdriver
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


browser = webdriver.Chrome()
# browser.get('https://b2b.11467.com/search/11739.htm')
# time.sleep(random.randint(1, 3))
# company_sort: list = []
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
                'https://b2b.11467.com/search/12104.htm']


# all_box = browser.find_elements(By.CLASS_NAME, 'content')[0].find_elements(By.TAG_NAME, 'a')
# for i in all_box:
#     sort_url = i.get_attribute('href')
#     time.sleep(random.randint(1, 5))
#     company_sort.append(sort_url)
#     print(sort_url)
# print(len(company_sort), company_sort)


def crawl_all_company(company_sort_list: list):
    """
    抓取行业中所有企业主页链接
    """
    company_list = []
    page_info = browser.find_elements(By.CLASS_NAME, 'pages')[0].find_elements(By.TAG_NAME, 'a')
    page_num = int(page_info.pop().get_attribute('href').split('.htm')[0].split('-')[1])
    for sort in company_sort_list:
        browser.get(sort)
        time.sleep(random.randint(1, 5))
        for p in range(page_num):
            box_list = browser.find_elements(By.CLASS_NAME, 'f_l')
            for box in box_list:
                company_link = box.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
                company_list.append(company_link)

            next_page = browser.find_elements(By.CLASS_NAME, 'pages')[0].find_elements(By.TAG_NAME, 'a')[
                -2].get_attribute(
                'href')
            browser.get(next_page)
            time.sleep(random.randint(1, 5))
            print(len(company_list))
    return company_list


crawl_all_company(company_sort)

browser.quit()
