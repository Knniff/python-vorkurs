def chiffre(input: str, key: int, direction: str) -> str:
    input = input.lower()
    output = ""
    if direction == "encrypt":
        for letter in input:
            if letter.isalpha():
                temp = ord(letter)
                temp = temp + key
                if temp > 122:
                    temp_key = temp - 123
                    temp = 97 + temp_key
                output += chr(temp)
            else:
                output += letter
        return output
    else:
        for letter in input:
            if letter.isalpha():
                temp = ord(letter)
                temp = temp - key
                if temp < 97:
                    temp_key = 97 - temp
                    temp = 123 - temp_key
                output += chr(temp)
            else:
                output += letter
        return output


print(
    chiffre(
        "fakt ist, dass alles im universum entweder eine kartoffel ist oder nicht.",
        13,
        "encrypt",
    )
)

# print(chiffre("Test Test.",3,"encrypt",))
