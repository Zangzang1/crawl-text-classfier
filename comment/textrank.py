from textrank4zh import TextRank4Keyword

def GetKeyWords(text,num):

    tr4w = TextRank4Keyword()
    tr4w.analyze(text=text, lower=True, window=2)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
    return tr4w.get_keywords(num, word_min_len=1)

#textrank算法查找text文本中num个关键词中存在的关键短语
def GetKeyPhrases(text,num):

    tr4w = TextRank4Keyword()
    tr4w.analyze(text=text, lower=True, window=2)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
    return tr4w.get_keyphrases(keywords_num=num, min_occur_num= 2)

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


    a = GetKeyWords(data,40)
    for item in a:
        print(item.word,item.weight)