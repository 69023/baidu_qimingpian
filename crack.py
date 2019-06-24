import os
import json
import requests

"""
企名片-商业信息服务平台!中国领先的商业社区和金融大数据平台
https://www.qimingpian.com/finosda/project/pinvestment
破解JS代码参数破解
https://vipapi.qimingpian.com/DataList/productListVip # 接口地址
"""

headers = {
    "Origin": "https://www.qimingpian.com",
    "Referer": "https://www.qimingpian.com/finosda/project/pinvestment",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


def decrypt_data(str):
    with open("template.js", 'r', encoding='utf-8') as f:
        crack_js = f.read().replace('&&&&', str)

    with open("crack.js", 'w', encoding="utf-8") as f2:
        f2.write(crack_js)

    return os.popen("node crack.js").readlines()[0]


def handle_request():
    data = {
        "time_interval": "",
        "tag": "",
        "tag_type": "",
        "province": "",
        "lunci": "",
        "page": "1",
        "num": "20",
        "unionid": ""
    }
    conn = requests.post(
        url="https://vipapi.qimingpian.com/DataList/productListVip",
        data=data,
        headers=headers
    )

    encrypt_data = conn.json().get('encrypt_data')
    print("原始数据：{}".format(encrypt_data))

    decrypt_data_json = json.loads(decrypt_data(encrypt_data))

    print(json.dumps(decrypt_data_json, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    handle_request()
