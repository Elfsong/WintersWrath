# -*- coding: utf-8 -*-

import time
import Levenshtein
import jellyfish
from functools import partial
from multiprocessing import Pool


def levenshtein(seq1, seq2):
    return Levenshtein.ratio(seq1, seq2)


def compare(word1, dictionary):
    c1_1 = jellyfish.soundex(word1)
    c2_1 = jellyfish.metaphone(word1)
    c3_1 = jellyfish.nysiis(word1)
    c4_1 = jellyfish.match_rating_codex(word1)

    result = (0, None)

    for word2 in dictionary:
        c1_2 = jellyfish.soundex(word2)
        c2_2 = jellyfish.metaphone(word2)
        c3_2 = jellyfish.nysiis(word2)
        c4_2 = jellyfish.match_rating_codex(word2)
        c1 = levenshtein(c1_1, c1_2)
        c2 = levenshtein(c2_1, c2_2)
        c3 = levenshtein(c3_1, c3_2)
        c4 = levenshtein(c4_1, c4_2)

        sim = c1 * 0.2 + c2 * 0.3 + c3 * 0.3 + c4 * 0.2

        if sim > result[0]:
            result = (sim, word2)

    return result


def file_input(file_name):
    file_content = list()
    with open(file_name, 'r') as lines:
        for line in lines:
            line = line.strip()
            if line:
                file_content.append(line)
    return file_content

def identity(cor_list, result):
    length = len(result)
    count = 0

    for i in range(length):
        if cor_list[i] == result[i][1]:
            count += 1
    accuracy = count / length
    return accuracy


# @warps()
def check():
    dictionary = file_input("dict.txt")
    mis_list = file_input("mis.txt")
    cor_list = file_input("cor.txt")

    pool = Pool(8)
    partial_compare = partial(compare, dictionary=dictionary)
    result = pool.map(partial_compare, mis_list[:100])

    accuracy = identity(cor_list[:100], result)
    print(accuracy)

if __name__ == "__main__":
    print("Running...")
    check()
