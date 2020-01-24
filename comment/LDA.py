import gensim
from gensim import corpora
# from pre_process import  prepare_text_for_lda
from pre_chinese_text import  prepare_text_for_lda

def top10(data):
    document = [prepare_text_for_lda(text) for text in data]
    # 使用gensim.Dictionary从text_data中生成一个词袋（bag-of-words)
    dictionary = corpora.Dictionary(document)
    corpus = [dictionary.doc2bow(text) for text in document]
    print(corpus)
    # 加载gensim，使用LDA算法求得前五的topic，
    # 同时生成的topic在之后也会被使用到来定义文本所属主题

    NUM_TOPICS = 10  # 定义了生成的主题词的个数
    ldamodel = gensim.models.ldamodel.LdaModel(corpus,
                                               num_topics=NUM_TOPICS,
                                               id2word=dictionary,
                                               passes=15)
    ldamodel.save('model/model5.gensim')
    topics = ldamodel.print_topics(num_words=5)
    for topic in topics:
        print(topic)

if __name__ == '__main__':

    import csv

    # text_1 = u"Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. It is altogether fitting and proper that we should do this."
    # text_2 = u'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'
    # text_3 = u"We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that nation might live. "
    # with open('F:\liziqi\comment\\en_rnn_neg.csv', 'r', encoding='gbk') as f:
    #     rows = csv.reader(f)
    #     data = []
    #     for row in rows:
    #         data.append(row[0])

    with open('F:\liziqi\comment\\zhatt_neg.csv','r',encoding='UTF-8') as f:
        # rows = csv.reader(f)
        lines = f.readlines()
        data = []
        for row in lines:
            row = row.strip()
            data.append(row)
    top10(data)