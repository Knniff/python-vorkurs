def list_comprehension():
    matrix = [
        [1 if row == 2 or column == 2 else 0 for column in range(5)] for row in range(5)
    ]
    print(matrix)


# von Jonas(JoBo12) aus dem Discord


def with_for():
    matrix_1 = []
    for item in range(5):
        matrix_1.append([])
        for item2 in range(5):
            matrix_1[item].append(int(item == 2 or item2 == 2))
    print(matrix_1)


list_comprehension()