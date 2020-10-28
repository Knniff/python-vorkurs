import numpy as np
import time
from typing import Dict


def load_file():
    with open(
        "/home/knniff/python-projects/python-vorkurs/Uebung08/word_list.txt", "r"
    ) as file:
        all_words = file.readlines()

    for word in range(len(all_words)):
        all_words[word] = all_words[word].replace("\n", "").lower()
    return all_words


def get_anagramm(input: str):
    array = load_file()
    find = []
    input = input.lower()
    input_len = len(input)
    dictionary_array = [
        make_dict(item) for item in [item for item in array if len(item) == input_len]
    ]
    word_dict = make_dict(input)
    for item in dictionary_array:
        if word_dict == item:
            find.append(item)
    return find


def make_dict(word: str) -> Dict[str, int]:
    return {char: word.count(char) for char in word}


for repetition in range(50):
    zeit = []
    start = time.time()
    print(get_anagramm("lampe"))
    zeit.append(time.time() - start)

zeit = np.array(zeit)
print("Finn: ")
print(f"Mean: {np.mean(zeit)}  Min: {np.min(zeit)}   Max: {np.max(zeit)}")
