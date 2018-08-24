# coding:utf-8

import numpy as np
import time
import Levenshtein
from functools import partial
from multiprocessing import Pool


def warps():
    def deco(func):
        def _deco(*args, **kwargs):
            start = time.process_time()
            result = func(*args, **kwargs)
            end = time.process_time()
            print(end - start)
            return result
        return _deco
    return deco


def levenshtein_prototype(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in xrange(size_x):
        matrix[x, 0] = x
    for y in xrange(size_y):
        matrix[0, y] = y

    for x in xrange(1, size_x):
        for y in xrange(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])


def levenshtein(seq1, seq2):
    return Levenshtein.ratio(seq1, seq2)


def file_input(file_name):
    file_content = list()
    with open(file_name, 'r') as lines:
        for index, line in enumerate(lines):
            line = line.strip()
            if line:
                file_content.append((line, index))
    return file_content


def compare(word, dictionary):
    result = (0, None)

    for item in dictionary:
        sim = levenshtein(word[0], item[0])
        if sim > result[0]:
            result = (sim, item[0])
    return (word, result[1])


def identify(cor_list, result_list):
    ll = len(cor_list)
    count = 0
    for i in range(ll):
        if cor_list[i][0] == result_list[i][1]:
            count += 1

    accuracy = count / ll

    return accuracy


@warps()
def check():
    dictionary = file_input("dict.txt")
    mis_list = file_input("mis.txt")
    cor_list = file_input("cor.txt")

    pool = Pool(8)
    partial_compare = partial(compare, dictionary=dictionary)
    result = pool.map(partial_compare, mis_list)

    print("Accuracy:", identify(cor_list, result))


if __name__ == "__main__":
    print("Running...")
    check()
