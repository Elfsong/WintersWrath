# coding: utf-8

import json
import re
import random
import jieba
import numpy as np
from itertools import chain
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
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


if __name__ == "__main__":
    bc = BertClient()
    stories = get_stories("es_stories.txt")
    # stories = get_stories("tt")
    real_vector_list = list()
    vector_list = []
    fake_vector_list = list()
    count = 1
    for story in stories:
        print(count)
        count += 1
        story_object = json.loads(story)
        sentences = get_sentences(story_object["content"])
        vectors = bc.encode(sentences, is_tokenized=True)
        vector_list += list(vectors)
        for index in range(1, len(vectors) - 1):
            v1 = list(vectors[index - 1])
            v2 = list(vectors[index])
            v3 = list(vectors[index + 1])
            temp_vector = v1 + v2 + v3
            real_vector_list += [temp_vector]

    for index in range(len(real_vector_list)):
        temp_vector = list(chain(*random.sample(vector_list, 3)))
        fake_vector_list += [temp_vector]

    print("Start!!!")

    X = np.array(real_vector_list + fake_vector_list)
    y = np.array([1]*len(real_vector_list) + [0]*len(fake_vector_list))
    clf = SVC(gamma='auto')
    clf.fit(X, y)

    result_list = list()

    for item in real_vector_list + fake_vector_list:
        result = clf.predict([item])
        result_list += [result]

    score = accuracy_score(y, result_list)
    print(score)
