import jieba
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import numpy as np
from collections import Counter

# 读取并分词
with open('location.txt', mode='r', encoding='utf-8') as fo:
    str_text = fo.read()
words = jieba.lcut(str_text)

# 统计词频
word_counts = Counter(words)
# 获取出现次数最多的前20个词
top_words = word_counts.most_common(20)

# 连接成字符串，用于生成词云
top_words_str = " ".join([word for word, freq in top_words])

# 加载图片和转换为数组
img = Image.open('kill6remain1.png')
img_array = np.array(img)

# 使用WordCloud生成词云
wc = WordCloud(
    font_path='msyh.ttc', 
    width=800, 
    height=600,
    background_color='white',
).generate(top_words_str)

# 显示词云图
plt.imshow(wc)
plt.axis('off')  # 关闭坐标轴
plt.tight_layout()  # 自动调整子图参数, 使之填充整个图像区域

# 保存词云图
plt.savefig('top20_locations.jpg', dpi=500)

# 注意：在实际环境中，确保'msyh.ttc'字体文件存在于指定路径，且该路径对于你的程序是可访问的。