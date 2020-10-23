import requests

letter_morse = {
    "A": "⚪➖",
    "B": "➖⚪⚪⚪",
    "C": "➖⚪➖⚪",
    "D": "➖⚪⚪",
    "E": "⚪",
    "F": "⚪⚪➖⚪",
    "G": "➖➖⚪",
    "H": "⚪⚪⚪⚪",
    "I": "⚪⚪",
    "J": "⚪➖➖➖",
    "K": "➖⚪➖",
    "L": "⚪➖⚪⚪",
    "M": "➖➖",
    "N": "➖⚪",
    "O": "➖➖➖",
    "P": "⚪➖➖⚪",
    "Q": "➖➖⚪➖",
    "R": "⚪➖⚪",
    "S": "⚪⚪⚪",
    "T": "➖",
    "U": "⚪⚪➖",
    "V": "⚪⚪⚪➖",
    "W": "⚪➖➖",
    "X": "➖⚪⚪➖",
    "Y": "➖⚪➖➖",
    "Z": "➖➖⚪⚪",
}
morse_letter = {
    "⚪➖": "A",
    "➖⚪⚪⚪": "B",
    "➖⚪➖⚪": "C",
    "➖⚪⚪": "D",
    "⚪": "E",
    "⚪⚪➖⚪": "F",
    "➖➖⚪": "G",
    "⚪⚪⚪⚪": "H",
    "⚪⚪": "I",
    "⚪➖➖➖": "J",
    "➖⚪➖": "K",
    "⚪➖⚪⚪": "L",
    "➖➖": "M",
    "➖⚪": "N",
    "➖➖➖": "O",
    "⚪➖➖⚪": "P",
    "➖➖⚪➖": "Q",
    "⚪➖⚪": "R",
    "⚪⚪⚪": "S",
    "➖": "T",
    "⚪⚪➖": "U",
    "⚪⚪⚪➖": "V",
    "⚪➖➖": "W",
    "➖⚪⚪➖": "X",
    "➖⚪➖➖": "Y",
    "➖➖⚪⚪": "Z",
}


def boo_to_hoo(input: str):
    return input.replace(".", "⚪").replace("-", "➖")


def get_pastebin(id: str) -> str:
    try:
        response = requests.get(f"https://pastebin.com/raw/{id}")
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"The request for code: {id} gave the error:")
        print(err)
    return response.text


def morse_to_letters(input: str) -> str:
    for item in letter_morse.items():
        morse_letter[item[1]] = item[0]
    input_list = input.split(" ")
    output = ""
    print(input_list)
    for item in input_list:
        if item != "":
            output += morse_letter[item]
        else:
            output += " "
    return output


def letters_to_morse(input: str) -> str:
    output = ""
    input = input.upper()
    for letter in input:
        if letter != " ":
            output += letter_morse[letter]
            output += " "
        else:
            output += " "
    return output


# print(morse_to_letters(boo_to_hoo(get_pastebin("EJyJpxPP"))))
print(morse_to_letters(letters_to_morse("Test Test")))
