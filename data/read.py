import re

punctuation = '!,;:?"-'


def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip().lower()


def init(words):
    f1 = open("./data/big.txt", 'r', encoding='utf-8')  # 读取，似乎需要声明为utf-8
    source = f1.read().split('.')
    record = {}  # 记录排序的字典，key为元组（排序方法），value为此排序的数量
    word_rec = {}
    for each_word in words:
        record[("#start", each_word)] = 0
        # record[(each_word, "#end")] = 0
        word_rec[each_word] = 0
    for each_sentence in source:
        each_words = removePunctuation(each_sentence).replace(
            "\n", "").replace("'", "").lower().split(' ')  # 将数据集每句都拆分成单词
        # 将换行符，逗号和空元素去除
        sequence = []
        for each in words:
            if each_words[0] == each:
                record[("#start", each)] += 1
            # if each_words[-1] == each:
            #    record[(each, "#end")] += 1
        for j in each_words:
            if j in words:
                word_rec[j] += 1
                if len(sequence) != 0 and j == sequence[-1]:
                    continue
                sequence.append(j)
                if len(sequence) == 3:
                    sequence.pop(0)
                if len(sequence) == 2:
                    sequence = tuple(sequence)
                    if record.get(sequence) == None:
                        record[sequence] = 1
                    else:
                        record[sequence] += 1
                    sequence = list(sequence)
    for each in record:
        if word_rec[each[1]] != 0:
            record[each] /= word_rec[each[1]]
        else:
            record[each] = 0
    return record


def get_w(a, b):
    return data[(a, b)]
