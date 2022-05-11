import json
import re

import yaml
from bs4 import BeautifulSoup
import httpx
from lxml import etree
import datetime

config_file = r'D:\github\practise\crawlerstack-proxypool\src\crawlerstack_proxypool\config\settings.yml'
url1 = 'https://proxylist.geonode.com/api/proxy-list'
url2 = 'https://geonode.com/free-proxy-list/'
url_h = 'https://proxy.mimvp.com/freeopen?proxy=out_hp'


# 'https://proxy.mimvp.com/freeopen?proxy=out_hp'

def read_yml_file(file: str):
    with open(file, 'r') as obj:
        try:
            for i in yaml.safe_load(obj).get('fetch_task'):
                print(i)
        except yaml.YAMLError as exc:
            print(exc)


def spider_json(url: str):
    now = datetime.datetime.now()
    now_time = now.strftime('%Y.%m.%d,%H:%M:%S')
    response = httpx.get(url)
    result_list = []
    page_info = response.text
    print(type(page_info))
    pagr_json = json.loads(page_info)
    print(pagr_json)
    try:
        for j in pagr_json:
            ip = j.get('ip')
            country = j.get('country_name')
            port = j.get('port')
            result_json = {
                'ip': ip,
                'country': country,
                'port': port,
                'last_check': now_time,
            }
            result_list.append(result_json)
    except AttributeError:
        pagr_json = pagr_json.get('data')
        for j in pagr_json:
            ip = j.get('ip')
            country = j.get('country_name')
            port = j.get('port')
            result_json = {
                'ip': ip,
                'country': country,
                'port': port,
                'last_check': now_time,
            }
            result_list.append(result_json)
    return result_list


def spider_html(url: str):
    now = datetime.datetime.now()
    now_time = now.strftime('%Y.%m.%d,%H:%M:%S')
    result_list = []
    r = httpx.get(url)
    print('request status code =%s' % r)
    soup = BeautifulSoup(r.text, 'html.parser')
    tr = soup.find_all('tr')
    for t in tr:
        tr_text = t.text
        ip = re.findall(r'\d+\.\d+\.\d+\.\d+', tr_text)
        country = re.findall('[^\x00-\xff]+[^\x00-\xff]', tr_text)
        post = re.findall('[\u0041-\u005a]+[\u0041-\u005a]', tr_text)
        if ip:
            for i, p in zip(ip, post):
                p_json = {
                    'ip': i,
                    'country': country[1],
                    'post': p,
                    'last_check': now_time
                }
                result_list.append(p_json)
    return result_list


# read_yml_file(config_file)
# print(spider_json(url1))
for s in spider_html(url_h):
    print(s)
