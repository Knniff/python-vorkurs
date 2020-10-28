import time


def load_list():
    start_time = time.time()
    with open(
        "/home/knniff/python-projects/python-vorkurs/Uebung08/words.txt",
        "r",
        encoding="UTF-8",
    ) as file:
        all_words = file.readlines()
    for word in range(len(all_words)):
        all_words[word] = all_words[word].replace("\n", "").lower()
    print("\nTime to load file:", time.time() - start_time, "seconds")
    return all_words


def find_anagrams(input_word):
    word_list = load_list()
    start_time = time.time()
    found = []
    input_word = input_word.lower()
    input_len = len(input_word)
    input_dict = word_to_dict(input_word)
    correct_len_list = []
    for word in word_list:
        if input_len == len(input_word):
            correct_len_list.append(word)
    for word in correct_len_list:
        if word_to_dict(word) == input_dict:
            found.append(word)
    print("Time to find anagrams:", time.time() - start_time, "seconds")
    print('Dies sind Anagramme des Wortes" ' + input_word + '":')
    for w in found:
        if input_word != w:
            print(w)


def word_to_dict(word):
    return {char: word.count(char) for char in word}


find_anagrams("Palme")