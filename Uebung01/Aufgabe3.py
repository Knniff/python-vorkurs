def bubblesort(array):
    for x in range(len(array)):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                b = array[i]
                array[i] = array[i + 1]
                array[i + 1] = b
    return array


print(bubblesort([5, 6, 9, 8, 7, 4, 5, 6, 2, 4, 9, 1, 9, 8, 2, 96]))
