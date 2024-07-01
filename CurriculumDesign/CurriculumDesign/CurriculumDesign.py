import requests
import json

all_data = []

def get_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37"
    }
    url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    response = requests.get(url=url, headers=headers)
    text = response.text
    response.close()
    return text

def parse(text):
    data_dict = json.loads(text)  # 将数据转化为字典
    for i in data_dict["data"]["list"]:
        temp = (i['title'], i['owner']['name'], i['stat']['view'], i['stat']['danmaku'])
        all_data.append(temp)

if __name__ == '__main__':
    text = get_data()
    parse(text)
    # 直接打印all_data的内容
    for video_info in all_data:
        print(f"视频名称: {video_info[0]}, UP主: {video_info[1]}, 播放量: {video_info[2]}, 评论数: {video_info[3]}")
        




#热门视频爬取：名称、up主、IP地址、播放量、评论数
#视频数据爬取：
#生成词云
#数据可视化