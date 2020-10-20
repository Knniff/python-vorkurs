from typing import List, Tuple, Generator
import re


def ngrams(size: int, input: str) -> Generator:
    input = re.sub(r"[^a-zA-Z0-9\s]", " ", input)
    input_list = input.split(" ")

    for step in range(len(input_list)):
        yield tuple(input_list[step : step + size])


gen = ngrams(4, "Ich bin ein String der konform der Aufgabe ist")
while True:
    try:
        print(next(gen))
    except StopIteration as err:
        print("You reached the end of the string.")
        break