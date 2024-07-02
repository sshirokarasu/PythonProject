from flask import Flask, render_template, request
import csv
from app import app  # app在__init__.py中被创建和初始化


@app.route('/')
def hello_world():
    # 初始化列表
    title, up, view, comment, like, forward, coin = [], [], [], [], [], [], []
    
    # 读取 CSV 数据
    with open('all_data.csv', mode='r', encoding='utf-8-sig') as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            title.append(row['视频名称'])
            up.append(row['up主'])
            view.append(int(row['播放数量']))  # 确保数值类型正确
            comment.append(int(row['评论数']))
            like.append(int(row['点赞数']))  # 假设 CSV 中有这一列
            forward.append(int(row['转发数']))  # 同上，根据实际情况调整
            coin.append(int(row['投币数']))  # 同上
    
    # 将数据传给模板
    return render_template('index.html', 
                           title=title, 
                           up=up, 
                           view=view, 
                           comment=comment, 
                           like=like, 
                           forward=forward, 
                           coin=coin)



# @app.route('/demo1')
# def demo():
#     # ... 第二部分代码 ...
#     data = []
#     with open(r'D:\py_code\Bzhan\all_data.csv', mode='r', encoding='utf-8') as fp:
#         reader = csv.reader(fp)
#         for i in reader:
#             if len(i) == 4:  # 这里假设有效的数据行有四个元素
#                 data.append(i)
#     return render_template('data.html', alldata=data)


# @app.route('/demo2')
# def demodemo():
#     # ... 第三部分代码 ...
#     title, up, view, comment = [], [], [], []  # 初始化列表
#     with open('all_data.csv', mode='r', encoding='utf-8') as fp:
#         reader = csv.DictReader(fp)  # 使用DictReader读取字典
#         for row in reader:
#             title.append(row['视频名称'])
#             up.append(row['up主'])
#             view.append(row['播放量'])
#             comment.append(row['评论数'])
#     return render_template('echarts.html', title=title, view=view, comment=comment, up=up)

# @app.route('/all_zx')
# def zx():
#     # ... 第四部分代码 ...
#     title, like, comment, show, coin, view = [], [], [], [], [], []  # 初始化列表
#     with open(r'D:\py_code\Bzhan\name_like.csv', mode='r', encoding='utf-8') as fp:
#         reader = csv.DictReader(fp)
#         for row in reader:
#             title.append(row['视频名称'])
#             like.append(row['点赞量'])
#             view.append(row['播放量'])
#             show.append(row['转发动量'])  # 注意这里的变量名与原说明不同，应与csv文件对应
#             coin.append(row['投币数目'])
#             comment.append(row['评论数'])
#     return render_template('big_info.html', title=title, view=view, comment=comment, show=show, like=like, coin=coin)




# #if __name__ == '__main__':
# #    app.run(debug=True)




