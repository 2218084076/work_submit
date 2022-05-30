import json
import random
import time

import requests


def ipquery(ip: str) -> str:
    """
    Get the region of the IP
    :param ip:
    :return proxy ip info:
    """
    url = "http://ip.taobao.com/outGetIpInfo?ip={}&accessKey=alibaba-inc".format(ip)
    time.sleep(random.randint(1, 3))
    req = requests.get(url).text
    json1 = json.loads(req)
    country = json1.get("data").get("country")  # 国
    province = json1.get("data").get("region").replace('XX', '')  # 省
    city = json1.get("data").get("city").replace('XX', '')  # 市
    return '{}：{} {} {}'.format(ip, country, province, city)
    # ip-api接口
    # url = "http://ip-api.com/json/%s?lang=zh-CN" % ip
    # time.sleep(random.randint(1, 3))
    # req = requests.get(url).text
    # json1 = json.loads(req)
    # country = json1["country"]  # 国
    # province = json1["regionName"]  # 省
    # city = json1["city"]  # 市
    # print("{}-{}-{}".format(country, province, city))

    # 太平洋api接口
    # url = 'http://whois.pconline.com.cn/ipJson.jsp?ip=%s&json=true' % ip
    # time.sleep(random.randint(1, 3))
    # req = requests.get(url).text
    # json1 = json.loads(req)
    # addr = json1.get('addr')  # 国
    # province = json1.get('pro')  # 省
    # city = json1.get('city')  # 市


ip_list = ['121.37.31.195', '120.42.46.226', '218.1.200.202', '210.5.10.87', '118.193.47.193', '175.24.112.3',
           '124.156.100.83', '58.220.95.40', '117.34.25.11', '116.63.170.189', '98.162.96.41', '98.170.57.231',
           '95.43.42.100', '193.84.184.25', '94.26.108.67', '93.184.151.48', '193.163.116.29']
for i in ip_list:
    print(ipquery(i))
