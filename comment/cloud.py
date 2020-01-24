
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
# from pre_process import  prepare_text_for_lda
from pre_chinese_text import  prepare_text_for_lda

def make(data):
    document = prepare_text_for_lda(data)
    tongji = Counter(document).most_common(50)
    for (k,v) in tongji:
        print(k,v)
    content = ' '.join(document)
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="white", max_words=40).generate(content)
    # Display the generated image:
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()

if __name__ == '__main__':

    import csv
    # text_1 = u"Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. It is altogether fitting and proper that we should do this."
    # text_2 = u'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'
    # text_3 = u"We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that nation might live. "
    with open('F:\liziqi\comment\\zhatt_neg.csv','r',encoding='UTF-8') as f:
        # rows = csv.reader(f)
        lines = f.readlines()
        data = ''
        for row in lines:
            row = row.strip()
            data+=row
            data+=' '
    make(data)
