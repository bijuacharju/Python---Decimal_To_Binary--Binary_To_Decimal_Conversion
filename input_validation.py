def validate_bin(bin_):
    binary_value = bin_
    if binary_value.strip() == "":
        print("Empty input found. Please enter binary digits.")
        return False
    try:
        binary = int(binary_value)
    except:
        print("Error: Special character or alphabets found!.")
        return False
    if binary < 0 or binary > 11111111:
        print("Error: Input value out of range.")
        return False

    while binary > 0:
        r = binary % 10
        binary = int(binary / 10)
        if r not in [0, 1]:
            print("Error: Only 0 and 1 integers valid.")
            return False
    return True


def validate_dec(dec_):
    decimal_value = dec_
    if decimal_value.strip() == "":
        print("Empty input found. Please enter binary digits.")
        return False
    try:
        decimal = int(decimal_value)
    except:
        print("Error: Special character or alphabets found!.")
        return False
    if decimal < 0 or decimal > 255:
        print("Error: Input value out of range.")
        return False

    return True
