"""
This module is designed to calculate similarity between two documents.

Author: Narayan Jat
Date: 11 January 2024
"""


# Importing required module.
import requests as r
from Crawler import *
import time


def word_extractor(content):
    words = []      # Storing words so that n gram generation become faster
    word = ""
    text = html_tag_remover(content)
    for char in text:
        char = char.lower()
        if char.isalnum():
            word += char
        else:
            if word != "":
                words.append(word)
            word = ""
    return words


def n_gram_generator(words):
    n_grams = {}
    word = ""
    i = 0
    while i < len(words) - 2:
        word = " ".join(words[i: i+ 5])
        if word in n_grams:
            n_grams[word] += 1
        else:
            n_grams[word] = 1
        i += 3
    return n_grams

def calculate_bin_hash_value(t, p = 53, m = 2 ** 64):
    hash = 0
    for i in range(len(t)):
        hash = hash + ord(t[i]) * p**i
    hash = hash % m
    bin_hash = bin(hash)[2:]
    # Putting 0 if bits are not 64
    bin_hash = ("0"*(64 - len(bin_hash)) + bin_hash)
    return bin_hash

def simhash_vector(grams):
    vectors = []
    for g in grams:
        vector = []
        hash_code = (calculate_bin_hash_value(g))
        for c in hash_code:
            if c == "0":
                vector.append(grams[g])
            else:
                vector.append(-grams[g])
        vectors.append(vector)

    sim_vector = []
    for i in range(64):
        c = 0
        for v in vectors:
            c += v[i]
        sim_vector.append(c)
    return sim_vector


def document_vector(sv):
    dv = []
    for v in sv:
        if v >0:
            dv.append(1)
        else:
            dv.append(0)
    return dv


def main():
    url1 = input("Please enter your url 1: ")
    url2 = input("please enter your url 2: ")
    web_time = time.time()
    content1 = r.get(url1).text
    content2 = r.get(url2).text
    web_time = time.time() - web_time
    operation_time = time.time()
    simhash_content1 = document_vector(simhash_vector(n_gram_generator(word_extractor(content1))))
    simhash_content2 = document_vector(simhash_vector(n_gram_generator(word_extractor(content2))))
    operation_time = time.time() - operation_time

    # comparing number of bits same
    same = 0
    for i in range(64):
        if simhash_content1[i] == simhash_content2[i]:
            same += 1

    print("\nThe similarity percentage for both document is:", (same / 64) * 100, "%\n")
    print("Other statistics: \n")
    print("Total time taken to fetch content from Internet: ", web_time, "seconds")
    print("Total time taken to perform operations: ", operation_time, "seconds")
    print("\n Please check Internet connection if takes time longer than usual for fetching internet data.")


main()