import csv
import requests
import json
import time

alt_data = []

def get_data():
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37'
    }
    
    url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    res = requests.get(url=url, headers=header)
    print(res.text)
    parse(res.text)
    res.close()
    
    # 简单的冷却时间以限制请求频率，这里假定整个处理过程不超过这个限制所需的时间
    time.sleep(0.05)  # 假设处理时间加上这个延时不会让频率超过20次/秒

def parse(text):
    data_dict = json.loads(text)
    for item in data_dict['data']['list']:
        temp = (item['title'], item['owner']['name'], item['stat']['view'], item['stat']['danmaku'])
        alt_data.append(temp)

def save_data(data):
    with open('all_data.csv', mode='w', encoding='utf-8-sig', newline='') as fp:  # 将encoding设置为'gbk'
        writer = csv.writer(fp)
        writer.writerow(['视频名称', 'up主', '播放数量', '评论数'])
        writer.writerows(data)

get_data()
# 延时5秒后再保存数据，这里保持原样，但实际是否需要这一步取决于具体需求
time.sleep(5)
save_data(alt_data)