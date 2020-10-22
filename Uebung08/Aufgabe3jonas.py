import numpy as np
import time

zeit = []


def get_anagrams(word):
    with open(
        "/home/knniff/python-projects/python-vorkurs/Uebung08/words.txt", "r"
    ) as file:
        word_list = file.readlines()
        for i in range(len(word_list)):
            word_list[i] = word_list[i].lower().replace("\n", "")
        anagram_list = []
        word_dict = {char: word.count(char) for char in word}
        n = len(word)
        anagram_list = [
            (word_l)
            for word_l in word_list
            if len(word_l) == n
            and {char: word_l.count(char) for char in word_l} == word_dict
        ]
        return anagram_list


def test_time(word):
    for repetition in range(50):
        start = time.time()
        print(get_anagrams(word))
        zeit.append(time.time() - start)


test_time("palme")

print("Time: ")
print(f"Mean: {np.mean(zeit)}  Min: {np.min(zeit)}   Max: {np.max(zeit)}")
