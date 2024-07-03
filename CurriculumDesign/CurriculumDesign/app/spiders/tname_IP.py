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
    try:
        res = requests.get(url=url, headers=header)
        res.raise_for_status()  # 检查请求是否成功
        parse(res.text)
    except requests.RequestException as e:
        print(f"请求错误: {e}")
    finally:
        res.close() if hasattr(res, 'close') else None
    time.sleep(0.05)

def parse(text):
    data_dict = json.loads(text)
    for item in data_dict['data']['list']:
        # 仅收集视频名称、发布位置（如果有的话）、分区名称和播放数量
        # 注意：原始数据中未直接提供发布位置（pub_location），此处假设它存在且需要收集
        pub_location = item.get('pub_location', '未知')  # 假设pub_location存在，如不存在则赋值为'未知'
        temp = (item['title'], pub_location, item['tname'], item['stat']['view'])
        alt_data.append(temp)

def save_data(data):
    with open('modified_data.csv', mode='w', encoding='utf-8-sig', newline='') as fp:
        writer = csv.writer(fp)
        # 更新列标题以反映实际收集的数据项
        writer.writerow(['视频名称', '发布位置', '分区名称', '播放数量'])
        writer.writerows(data)

if __name__ == "__main__":
    get_data()
    time.sleep(5)
    save_data(alt_data)