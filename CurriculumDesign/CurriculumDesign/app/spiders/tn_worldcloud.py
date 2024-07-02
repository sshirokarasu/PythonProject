import jieba
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import numpy as np

fo = open('tname.txt', mode='r', encoding='utf-8')
str_text = fo.read()
print(str_text)

img = Image.open('kill6remain1.png')
img_array = np.array(img)

wc = WordCloud(
font_path='msyh.ttc', width=800, height=600,

                          background_color='white'
).generate_from_text(str_text)

plt.imshow(wc)
plt.axis(False)
plt.savefig('tname.jpg', dpi=500)
fo.close()