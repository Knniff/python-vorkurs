import numpy as np
import time


def load_file():
    return np.loadtxt(
        "/home/knniff/python-projects/python-vorkurs/Uebung08/words.txt",
        dtype=str,
    )


def get_anagramm(input):
    find = []
    array = load_file()
    shorter_array = []
    for item in array:
        if len(item) == len(input):
            shorter_array.append(item)
    # shorter_array = array[len(array) == len(input)]
    shorter_array = np.array(shorter_array)
    dictionary_array = dict_array(shorter_array)
    word_dict = make_dict(input)
    for item in dictionary_array:
        if word_dict == item:
            find.append(item)
    return find


def make_dict(word):
    dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    word = word.lower()
    for letter in word:
        for item in dict:
            if letter == item:
                dict[letter] += 1
    return dict


def dict_array(array):
    new_array = []
    for item in array:
        new_array.append(make_dict(item))
    return np.array(new_array)


for repetition in range(50):
    zeit = []
    start = time.time()
    get_anagramm("lampe")
    zeit.append(time.time() - start)

zeit = np.array(zeit)
print("Time: ")
print(f"Mean: {np.mean(zeit)}  Min: {np.min(zeit)}   Max: {np.max(zeit)}")
