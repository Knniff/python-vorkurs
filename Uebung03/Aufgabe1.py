def list_comprehension(input):
    matrix = []
    for item in input:
        matrixrow = [letter for letter in item]
        matrix.append(matrixrow)
    print(matrix)


def smart_comprehension():
    return [
        [1 if row == 2 or column == 2 else 0 for column in range(0, 5)]
        for row in range(0, 5)
    ]


# list_comprehension(["00100", "00100", "11111", "00100", "00100"])
print(smart_comprehension())