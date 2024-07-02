import jieba
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import numpy as np
from collections import Counter

# ��ȡ���ִ�
with open('location.txt', mode='r', encoding='utf-8') as fo:
    str_text = fo.read()
words = jieba.lcut(str_text)

# ͳ�ƴ�Ƶ
word_counts = Counter(words)
# ��ȡ���ִ�������ǰ20����
top_words = word_counts.most_common(20)

# ���ӳ��ַ������������ɴ���
top_words_str = " ".join([word for word, freq in top_words])

# ����ͼƬ��ת��Ϊ����
img = Image.open('kill6remain1.png')
img_array = np.array(img)

# ʹ��WordCloud���ɴ���
wc = WordCloud(
    font_path='msyh.ttc', 
    width=800, 
    height=600,
    background_color='white',
).generate(top_words_str)

# ��ʾ����ͼ
plt.imshow(wc)
plt.axis('off')  # �ر�������
plt.tight_layout()  # �Զ�������ͼ����, ʹ֮�������ͼ������

# �������ͼ
plt.savefig('top20_locations.jpg', dpi=500)

# ע�⣺��ʵ�ʻ����У�ȷ��'msyh.ttc'�����ļ�������ָ��·�����Ҹ�·��������ĳ����ǿɷ��ʵġ�