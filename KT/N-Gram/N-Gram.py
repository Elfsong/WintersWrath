# coding:utf-8

import time
import ngram
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


def file_input(file_name):
    file_content = list()
    with open(file_name, 'r') as lines:
        for line in lines:
            line = line.strip()
            if line:
                file_content.append(line)
    return file_content


def establish_dictionary(dict_list):
    n_dict = ngram.NGram(dict_list, N=4)
    return n_dict


def compare(word, dictionary):
    print(word)
    return dictionary.find(word)


def identity(cor_list, result):
    length = len(result)
    count = 0
    for i in range(length):
        if cor_list[i] == result[i]:
            count += 1
    accuracy = count / length
    return accuracy


@warps()
def check():
    dictionary = file_input("dict.txt")
    mis_list = file_input("mis.txt")
    cor_list = file_input("cor.txt")

    n_dict = establish_dictionary(dictionary)
    print("Dictionary completed!")

    pool = Pool(8)
    partial_compare = partial(compare, dictionary=n_dict)
    result = pool.map(partial_compare, mis_list)

    accuracy = identity(cor_list, result)
    print(accuracy)


if __name__ == "__main__":
    check()
