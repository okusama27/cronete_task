"""郵便番号から住所を取得する
http://zipcloud.ibsnet.co.jp/
"""

import json
import urllib.request


def get_address(zipcode):
    with urllib.request.urlopen('http://zipcloud.ibsnet.co.jp/api/search?zipcode=' + zipcode) as response:
        d = json.loads(response.read().decode('utf-8'))
    return '{address1} {address2} {address3}'.format(**d['results'][0])


#print(get_address('8540001'))

def test_get_address():
    actual = get_address('7830060')
    expected = '高知県 南国市 蛍が丘'
    assert actual == expected


#test_get_address()