# coding: utf-8

import json
import re
import random
import numpy as np
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import jieba
from bert_serving.client import BertClient


def get_stories(file_path):
    with open(file_path, "r", encoding="utf-8") as story_fd:
        return story_fd.readlines()


def get_sentences(story):
    sentences = list()
    for sentence in cut_sent(story):
        sentence = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", sentence)
        cutted_sentence = list(jieba.cut(sentence))
        if len(cutted_sentence) < 1:
            cutted_sentence = ["None"]
        sentences += [cutted_sentence]
    return sentences


def cut_sent(para):
    para = re.sub('([。！？\?])([^”])', r"\1\n\2", para)
    para = re.sub('(\.{6})([^”])', r"\1\n\2", para)
    para = re.sub('(\…{2})([^”])', r"\1\n\2", para)
    para = re.sub('(”)', '”\n', para)
    para = para.rstrip()
    return para.split("\n")


def get_vector(word_list):
    result = bc.encode([word_list], is_tokenized=True)
    return result


def sentence_process(sentence):
    sentence_vector = get_vector(sentence)
    return sentence_vector[0]


def process(story):
    story_vector_list = list()
    _real_data = list()
    for sentence in get_sentences(story):
        sentence_vector = sentence_process(sentence)
        story_vector_list += [sentence_vector]

    for index in range(1, len(story_vector_list)):
        new_vector = list(story_vector_list[index - 1]) + list(story_vector_list[index])
        _real_data += [new_vector]

    return story_vector_list, _real_data


if __name__ == "__main__":
    bc = BertClient()
    stories = get_stories("es_stories.txt")

    vector_list = list()
    real_data = list()
    fake_data = list()

    for story in stories:
        story = json.loads(story)
        story_vector_list, _real_data = process(story["content"])
        vector_list += story_vector_list
        real_data += _real_data

    for i in range(len(real_data)):
        a, b = random.sample(vector_list, 2)
        new_vector = list(a) + list(b)
        fake_data += [new_vector]

    test_data = real_data + fake_data


    X = np.array(test_data)
    y = np.array([1]*len(real_data) + [0]*len(fake_data))

    clf = SVC(gamma='auto')
    clf.fit(X, y)

    y_pred = list()

    for test in X:
        result = clf.predict(test.reshape(1, -1))
        y_pred += [result]

    print(accuracy_score(y, y_pred))
    tn, fp, fn, tp = confusion_matrix(y, y_pred).ravel()
    print(tn, fp, fn, tp)
