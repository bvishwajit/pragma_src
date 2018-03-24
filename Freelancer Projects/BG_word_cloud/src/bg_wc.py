import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random

from wordcloud import WordCloud, STOPWORDS

def color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname('__file__')

# read the mask image
# taken from
mask = np.array(Image.open(path.join(d, "../imgs/bg_03.png")))


#BG Shlokas 1 to 18
text = open("bg1to18.txt").read()

# adding BG script specific stopwords
stopwords = set(STOPWORDS)
stopwords.add("na")
stopwords.add("uvaca")
stopwords.add("sa")
stopwords.add("tu")
stopwords.add("eva")
stopwords.add("ca")
stopwords.add("mam")
stopwords.add("te")
stopwords.add("api")
stopwords.add("karma")
stopwords.add("aham")
stopwords.add("kim")
stopwords.add("tvam")
stopwords.add("tad")
stopwords.add("hi")
stopwords.add("caiva")
stopwords.add("tat")
stopwords.add("tatha")
stopwords.add("yo")




wc = WordCloud(background_color="white",max_words=1000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(text)
# store default colored image
default_colors = wc.to_array()
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")
wc.to_file("bg_bw_wc.png")
plt.axis("off")
plt.figure()
plt.title("Bhagavad Gita Wordcloud")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
plt.show()
wc.to_file("bg_wc_color.png")