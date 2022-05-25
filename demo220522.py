import json

import requests


def get_ip_info(ip: str):
    r = requests.get('http://ip.aliyun.com/outGetIpInfo?ip=%s&accessKey=LTAI5t7ripD52p5hrRrVE4sB' % ip)
    ip_info = json.loads(r.text)
    print(ip_info)


a = '8080'
if a in '8080':
    print(a)
# get_ip_info('162.214.202.170')
