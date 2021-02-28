from input_validation import *


def input_bin():
    bin_1 = first_binary_input()
    bin_2 = second_binary_input()
    return bin_1, bin_2


def input_dec():
    dec1 = first_decimal_input()
    dec2 = second_decimal_input()
    return dec1, dec2


def first_binary_input():
    binary = input("Enter your first binary number:")
    if not validate_bin(binary):
        first_binary_input()
    else:
        return binary


def second_binary_input():
    binary = input("Enter your second binary number:  ")
    if not validate_bin(binary):
        second_binary_input()
    else:
        return binary


def first_decimal_input():
    decimal = input("Enter your first decimal number:  ")
    if not validate_dec(decimal):
        first_decimal_input()
    else:
        return decimal


def second_decimal_input():
    decimal = input("Enter your second decimal number:  ")
    if not validate_dec(decimal):
        second_decimal_input()
    else:
        return decimal
