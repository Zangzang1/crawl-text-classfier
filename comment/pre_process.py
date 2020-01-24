import spacy
import nltk
import string
from spacy.lang.en import English
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet as wn

spacy.load('en_core_web_sm')
parser = English()
#对文章内容进行清洗并将单词统一降为小写
def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens

# nltk.download('wordnet')
def get_lemma(word):
    #dogs->dog
    #aardwolves->aardwolf'
    #sichuan->sichuan
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


#定义预处理函数
def prepare_text_for_lda(text):
    en_stop = set(nltk.corpus.stopwords.words('english'))
    #分词处理
    # for c in string.punctuation:
    #     text = text.replace(c, ' ')
    tokens = tokenize(text)
    #取出非停顿词
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [token for token in tokens if len(token)>1]
    #对词语进行还原
    # tokens = [get_lemma(token) for token in tokens]
    return tokens

    # 加载gensim

