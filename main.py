from input import *
from conversion import *


bin1 = ""
bin2 = ""
dec1 = ""
dec2 = ""


def take_input():
    type_of_addition = input("Type 'b' for binary addition and 'd' for decimal addition. (b/d):  ")
    if type_of_addition == "b":
        for_binary_input()

    elif type_of_addition == "d":
        for_decimal_input()
    else:
        print("Error: Please enter valid input.")
        take_input()
    re_run()


def for_binary_input():
    global bin1
    global bin2
    global dec1
    global dec2
    bin1, bin2 = input_bin()
    dec1 = binary_to_decimal(bin1)
    dec2 = binary_to_decimal(bin2)
    bin1 = dec_to_bin(dec1)
    bin2 = dec_to_bin(dec2)
    print("\n", bin1, "\n", bin2)
    print(" --------")
    print()
    print("\n", dec1, "\n", dec2)
    print(" ---")
    print()
    if dec1 + dec2 > 255:
        print("Error: Total Value out of range. Please enter values whose total is less or equal to 255.")
        for_binary_input()


def for_decimal_input():
    global bin1
    global bin2
    global dec1
    global dec2
    dec1, dec2 = input_dec()
    bin1 = dec_to_bin(dec1)
    bin2 = dec_to_bin(dec2)
    print("\n", bin1, "\n", bin2)
    print(" --------")
    print()
    print("\n", dec1, "\n", dec2)
    print(" ---")
    print()
    if int(dec1) + int(dec2) > 255:
        print("Error: Total Value out of range. Please enter values whose total is less or equal to 255.")
        for_decimal_input()


def re_run():
    run = input("Do you want to make another calculation? Type 'y' for yes and 'n' for no. (y/n):  ")
    if run == "y":
        take_input()
    elif run == "n":
        return
    else:
        print("Error: Please enter valid input.")
        re_run()


if __name__ == '__main__':
    print("Welcome to addition calculator.")
    take_input()
