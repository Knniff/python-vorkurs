# Aufgabe: Anagramme mit einem Wörterbuch generieren
from typing import Dict, List, Generator
import time

from collections import defaultdict

times = []


def coll_count_letters(word: str) -> Dict[str, int]:
    result = defaultdict(int)
    for c in word:
        result[c] += 1
    return result


def count_letters(word: str) -> Dict[str, int]:
    return {char: word.count(char) for char in set(word) if char.isalpha()}


def generate_anagram(startword: str) -> List[str]:
    startword = startword.lower()
    startword_letter_count = coll_count_letters(startword)

    anagrams = []

    with open(
        "/home/knniff/python-projects/python-vorkurs/Uebung08/words.txt", "r"
    ) as file:
        all_words = file.readlines()
        # all_words = list(filter(lambda w : len(w) == len(startword), all_words))
        for word in all_words:
            word = word.replace("\n", "")

            if coll_count_letters(word.lower()) == startword_letter_count:

                anagrams.append(word.replace("\n", ""))

    return anagrams


for _ in range(50):
    start = time.time()
    print(generate_anagram("ampel"))
    times.append(time.time() - start)

print(f"Durchschnitt: {sum(times) / 50}")
print(f"Min: {min(times)}")
print(f"Max: {max(times)}")
