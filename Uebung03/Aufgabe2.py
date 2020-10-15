def dict_comprehension(text):
    text = text.lower()
    print({char: text.count(char) for char in text if not char == " "})


def with_for(text):
    finalDict = {}
    text = text.lower()
    for letter in text:
        if not letter == " ":
            if not letter in finalDict:
                finalDict[letter] = 1
            else:
                finalDict[letter] += 1
    print(finalDict)


dict_comprehension(
    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
)
