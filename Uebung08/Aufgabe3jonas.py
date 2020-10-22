import numpy as np
import time

zeit = []


def get_anagrams(word):
    word_list = np.loadtxt(
        "/home/knniff/python-projects/python-vorkurs/Uebung08/words.txt",
        dtype=str,
    )
    anagram_list = []
    word_dict = {char: word.count(char) for char in word}
    n = len(word)
    shorter_array = np.array([(word_l) for word_l in word_list if len(word_l) == n])
    for test_word in shorter_array:
        test_word = test_word.lower()
        discard = False
        for key in word_dict:
            if test_word.count(key) != word_dict[key]:
                discard = True
        if not discard:
            anagram_list += [test_word]
    return anagram_list


def test_time(word):
    for repetition in range(50):
        start = time.time()
        print(get_anagrams(word))
        zeit.append(time.time() - start)


test_time("palme")

print("Time: ")
print(f"Mean: {np.mean(zeit)}  Min: {np.min(zeit)}   Max: {np.max(zeit)}")
