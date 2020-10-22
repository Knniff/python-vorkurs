import numpy as np
import time


def load_file():
    with open(
        "/home/knniff/python-projects/python-vorkurs/Uebung08/words.txt", "r"
    ) as file:
        all_words = file.readlines()
    for word in range(len(all_words)):
        all_words[word] = all_words[word].replace("\n", "")
    return all_words


def get_anagramm(input):
    find = []
    array = load_file()
    shorter_array = []
    for item in array:
        if len(item) == len(input):
            shorter_array.append(item)
    dictionary_array = dict_array(shorter_array)
    word_dict = make_dict(input)
    for item in dictionary_array:
        if word_dict == item:
            find.append(item)
    return find


def make_dict(word):
    word = word.lower()
    return {char: word.count(char) for char in word}


def dict_array(array):
    return [make_dict(item) for item in array]


for repetition in range(100):
    zeit = []
    start = time.time()
    print(get_anagramm("lampe"))
    zeit.append(time.time() - start)

zeit = np.array(zeit)
print("Time: ")
print(f"Mean: {np.mean(zeit)}  Min: {np.min(zeit)}   Max: {np.max(zeit)}")
