import requests
import json

tname_data = []

def get_data():
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37'
    }

    url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    res = requests.get(url=url, headers=header)
    print(res.text)
    parse(res.text)
    res.close()

def parse(text):
    dict = json.loads(text)
    for item in dict['data']['list']:
        tname_data.append(item['tname'])

def save_tname():
    with open('tname_7.3.txt', mode='w', encoding='utf-8-sig') as fp:
        for i in tname_data:
            fp.write(i + '\n')

if __name__ == '__main__':
    get_data()
    save_tname()
    print(len(tname_data))