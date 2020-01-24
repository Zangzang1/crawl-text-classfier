import jieba
import re
import csv

def tokenize(text):
    """
    带有语料清洗功能的分词函数
    """
    text = re.sub("\{%.+?%\}", " ", text)           # 去除 {%xxx%} (地理定位, 微博话题等)
    text = re.sub("@.+?( |$)", " ", text)           # 去除 @xxx (用户名)
    text = re.sub("【.+?】", " ", text)              # 去除 【xx】 (里面的内容通常都不是用户自己写的)
    icons = re.findall("\[.+?\]", text)             # 提取出所有表情图标
    text = re.sub("\[.+?\]", "IconMark", text)      # 将文本中的图标替换为`IconMark`

    tokens = []
    for k, w in enumerate(jieba.lcut(text)):
        w = w.strip()
        if "IconMark" in w:                         # 将IconMark替换为原图标
            for i in range(w.count("IconMark")):
                tokens.append(icons.pop(0))
        elif w and w != '\u200b' and w.isalpha():   # 只保留有效文本
                tokens.append(w)
    return tokens


def load_corpus(path):
    """
    加载语料库
    """

    stopwords = []
    with open("stopwords.txt", "r", encoding="utf8") as f:
        for w in f:
            stopwords.append(w.strip())
    stopwords = set(stopwords)
    data = []
    with open(path, "r", encoding="gbk") as f:
        rows = csv.reader(f)
        for row in rows:
            content = row[1]
            tokens = tokenize(content)
            tokens = [i for i in tokens if i not in stopwords]
            data.append(tokens)
    print(data[2])
    return data


stopwords = []
with open("stopwords.txt", "r", encoding="utf8") as f:
    for w in f:
        stopwords.append(w.strip())
stopwords = set(stopwords)

def prepare_text_for_lda(text):
    tokens = tokenize(text)
    # tokens = [i for i in tokens if i not in stopwords]
    return tokens