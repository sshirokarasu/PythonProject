import csv
import requests
import json
import time

alt_data = []

def get_data():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37'
    }
    
    url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    res = requests.get(url=url, headers=header)
    print(res.text)
    parse(res.text)
    res.close()
    
    time.sleep(0.05)

def parse(text):
    data_dict = json.loads(text)
    for item in data_dict['data']['list']:
        # 添加点赞、转发、投币的统计信息
        temp = (item['title'], item['owner']['name'], item['stat']['view'], item['stat']['danmaku'],
                item['stat']['favorite'], item['stat']['share'], item['stat']['coin'])
        alt_data.append(temp)

def save_data(data):
    with open('all_data.csv', mode='w', encoding='utf-8-sig', newline='') as fp:
        writer = csv.writer(fp)
        # 更新列标题以包含新增的点赞、转发、投币列
        writer.writerow(['视频名称', 'up主', '播放数量', '评论数', '点赞数', '转发数', '投币数'])
        writer.writerows(data)

get_data()
time.sleep(5)
save_data(alt_data)