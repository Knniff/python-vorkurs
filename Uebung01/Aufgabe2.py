def is_even(number: int):
    if number == 0:
        print("Number is even")
    elif number == -1:
        print("Number is odd")
    else:
        is_even(number - 2)


is_even(1988)
# Number cant be larger than 1988 because of recursion limit
