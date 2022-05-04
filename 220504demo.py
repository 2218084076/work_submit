import asyncio
from playwright.async_api import async_playwright
import pymysql
import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s')

ip_list = [{'ip': '210.26.124.143', 'mark': ''}, {'ip': '106.75.226.36', 'mark': ''},
           {'ip': '125.62.26.197', 'mark': ''}, {'ip': '120.92.74.237', 'mark': ''},
           {'ip': '120.92.74.189', 'mark': ''}, {'ip': '218.60.8.99', 'mark': ''}, {'ip': '218.60.8.83', 'mark': ''},
           {'ip': '101.37.79.125', 'mark': ''}, {'ip': '113.200.56.13', 'mark': ''}, {'ip': '106.12.32.43', 'mark': ''},
           {'ip': '171.221.239.11', 'mark': ''}, {'ip': '119.31.210.170', 'mark': ''},
           {'ip': '203.86.26.9', 'mark': ''}, {'ip': '183.129.207.73', 'mark': ''}, {'ip': '218.28.191.6', 'mark': ''},
           {'ip': '121.40.183.166', 'mark': ''}, {'ip': '106.75.164.15', 'mark': ''},
           {'ip': '59.37.18.243', 'mark': ''}, {'ip': '61.182.88.133', 'mark': ''},
           {'ip': '61.157.206.176', 'mark': ''}, {'ip': '114.113.126.82', 'mark': ''},
           {'ip': '114.113.126.83', 'mark': ''}, {'ip': '59.46.112.34', 'mark': ''},
           {'ip': '120.27.13.145', 'mark': ''}, {'ip': '114.113.126.87', 'mark': ''},
           {'ip': '218.90.174.37', 'mark': ''}, {'ip': '118.190.210.227', 'mark': ''},
           {'ip': '61.128.208.94', 'mark': ''}, {'ip': '116.21.186.45', 'mark': ''},
           {'ip': '61.157.206.174', 'mark': ''}, {'ip': '123.133.36.26', 'mark': ''},
           {'ip': '221.233.198.142', 'mark': ''}, {'ip': '222.69.130.252', 'mark': ''},
           {'ip': '116.237.67.127', 'mark': ''}, {'ip': '113.57.208.16', 'mark': ''},
           {'ip': '119.254.94.114', 'mark': ''}, {'ip': '183.129.153.122', 'mark': ''},
           {'ip': '119.254.94.103', 'mark': ''}, {'ip': '123.132.232.254', 'mark': ''},
           {'ip': '119.254.94.107', 'mark': ''}, {'ip': '153.37.32.5', 'mark': ''},
           {'ip': '113.74.172.185', 'mark': ''}, {'ip': '183.129.244.17', 'mark': ''},
           {'ip': '211.101.136.86', 'mark': ''}, {'ip': '211.159.171.58', 'mark': ''},
           {'ip': '58.216.199.202', 'mark': ''}, {'ip': '221.6.201.18', 'mark': ''},
           {'ip': '58.241.217.66', 'mark': ''}, {'ip': '218.3.176.66', 'mark': ''}, {'ip': '183.47.2.201', 'mark': ''},
           {'ip': '61.157.206.173', 'mark': ''}, {'ip': '218.30.137.130', 'mark': ''},
           {'ip': '218.61.203.102', 'mark': ''}, {'ip': '218.4.193.22', 'mark': ''},
           {'ip': '123.153.75.20', 'mark': ''}, {'ip': '140.143.64.219', 'mark': ''},
           {'ip': '125.71.217.91', 'mark': ''}, {'ip': '218.75.69.50', 'mark': ''},
           {'ip': '123.244.148.30', 'mark': ''}, {'ip': '60.191.57.79', 'mark': ''}, {'ip': '114.217.0.52', 'mark': ''},
           {'ip': '59.57.151.126', 'mark': ''}, {'ip': '182.18.13.149', 'mark': ''},
           {'ip': '219.150.85.138', 'mark': ''}, {'ip': '110.189.152.86', 'mark': ''},
           {'ip': '221.221.47.222', 'mark': ''}, {'ip': '27.216.193.250', 'mark': ''},
           {'ip': '58.210.133.98', 'mark': ''}, {'ip': '218.91.151.243', 'mark': ''},
           {'ip': '14.155.115.158', 'mark': ''}, {'ip': '183.129.207.70', 'mark': ''},
           {'ip': '36.110.14.5', 'mark': ''}, {'ip': '58.56.108.226', 'mark': ''}, {'ip': '218.76.253.201', 'mark': ''},
           {'ip': '58.241.70.13', 'mark': ''}, {'ip': '60.214.153.14', 'mark': ''},
           {'ip': '58.240.232.126', 'mark': ''}, {'ip': '183.129.207.83', 'mark': ''},
           {'ip': '218.66.79.175', 'mark': ''}, {'ip': '139.227.253.119', 'mark': ''},
           {'ip': '175.2.115.50', 'mark': ''}, {'ip': '61.150.96.27', 'mark': ''}, {'ip': '124.89.33.59', 'mark': ''},
           {'ip': '113.100.72.179', 'mark': ''}, {'ip': '221.195.73.170', 'mark': ''},
           {'ip': '183.159.69.129', 'mark': ''}, {'ip': '180.213.166.96', 'mark': ''},
           {'ip': '202.112.237.102', 'mark': ''}, {'ip': '183.6.129.212', 'mark': ''},
           {'ip': '183.129.207.80', 'mark': ''}, {'ip': '125.40.238.181', 'mark': ''},
           {'ip': '123.134.92.240', 'mark': ''}, {'ip': '123.144.0.230', 'mark': ''},
           {'ip': '219.142.132.146', 'mark': ''}, {'ip': '121.17.133.124', 'mark': ''},
           {'ip': '202.108.251.230', 'mark': ''}, {'ip': '140.207.50.246', 'mark': ''},
           {'ip': '140.207.147.69', 'mark': ''}, {'ip': '113.135.219.161', 'mark': ''},
           {'ip': '119.180.146.127', 'mark': ''}]


async def main():
    async with async_playwright() as p:
        browser_type = p.webkit
        browser = await browser_type.launch(headless=False)
        page = await browser.new_page()
        await page.goto('http://ip.yqie.com/proxyhttps/index_1.htm')
        n = 1
        result_ip_list = []
        json_list = await page.evaluate('''
get_ip = function() {
  var a, i, json, l, _i, _len;
  l = [];
  a = document.getElementsByTagName("tr");
  for (_i = 0, _len = a.length; _i < _len; _i++) {
    i = a[_i];
    json = {
      "ip": i.innerText.split("\t")[1],
      "title": i.innerText.split("\t")[3],
      "mark": ""
    };
    l.push(json);
  }
  return l;
};
        ''')
        result_json = {
            'page%s' % n: json_list
        }
        result_ip_list.append(result_json)
        print(json_list)
        await browser.close()


def insert_ip_pool():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123qweasd',
        db='ip_pool',
        charset='utf-8',
    )
    cur = conn.cursor()


def try_ip(ip_json_list):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.127 Safari/537.36 '
    }
    url = 'https://www.baidu.com/'
    for ip in ip_json_list:
        ip = ip.get('ip')
        proxies = {
            'http': '%s' % ip,
            'https': '%s' % ip
        }
        try:
            requests.get(url, headers=headers, proxies=proxies, timeout=5)
        except Exception as e:
            print('fail invalid: %s...' % ip)
        else:
            print('successful and effective: %s ip-%s' % e, ip)


def check_proxy(ip_json_list, port):
    for ip in ip_json_list:
        ip = ip.get('ip')
        try:
            # 设置重连次数
            requests.adapters.DEFAULT_RETRIES = 3
            # IP = random.choice(IPAgents)
            proxy = f"http://{ip}:{port}"
            # thisIP = "".join(IP.split(":")[0:1])
            # print(thisIP)
            res = requests.get(url="http://icanhazip.com/", timeout=2, proxies={"http": proxy})
            proxyIP = res.text
            if (proxyIP == proxy):
                print("代理IP:'" + proxyIP + "'有效！")
                return True
            else:
                print("2代理IP无效！")
                return False
        except:
            print("1代理IP无效！")
            return False


try_ip(ip_list)
# asyncio.get_event_loop().run_until_complete(main())
