import math
from ext import e_decimal_ext

e_decimal_default = math.exp(1)


def remove_whitespace(string):
    s = string.replace(" ", "")

    return s


ext = remove_whitespace(e_decimal_ext)


def get_e_decimals():
    no_of_decimal_place = 0

    while no_of_decimal_place < 1 or no_of_decimal_place > 1000:
        try:
            no_of_decimal_place = int(input("Enter the number of decimals you want for e(Euler's number): "))
        except ValueError:
            print("Input must be a digit!")

        if no_of_decimal_place < 1 or no_of_decimal_place > 1000:
            print("Input must be between 1 and 10001")

    if no_of_decimal_place == 15:

        return f"Result: {e_decimal_default}"
    elif no_of_decimal_place < 15:
        whole_no = str(e_decimal_default)[:2]
        mantissa = str(e_decimal_default)[2:no_of_decimal_place+2]

        return "Result: " + whole_no + mantissa
    else:
        extended = str(e_decimal_default) + ext

        return f"Result: {extended[:no_of_decimal_place+2]}"


result = get_e_decimals()
print(result)


