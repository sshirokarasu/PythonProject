import csv
import requests
import json

name_like = []

def get_data():
    #模拟浏览器访问
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
        name_like.append(item['title'])

def save_name_like():
    with open('name_like.csv', mode='w', encoding='utf-8-sig') as fp:
        writer = csv.writer(fp)
        writer.writerow(['视频名称'])
        for name in name_like:
            writer.writerow(name)

if __name__ == '__main__':
    get_data()
    save_name_like()
    print(len(name_like))

