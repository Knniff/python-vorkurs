def isEven(number):
    if number == 0:
        print("Number is even")
    elif number == -1:
        print("Number is odd")
    else:
        isEven(number-2)

isEven(1988)
#Nummer darf nicht größer als 1988 sein!