def binary_to_decimal(num):
    total = 0
    length = len(num)-1
    for value in num:
        total += int(value) * (2 ** length)
        length = length - 1
    return total


def dec_to_bin(num_):
    num = int(num_)
    binary_value = ['0', '0', '0', '0', '0', '0', '0', '0']
    iteration = 7
    while num > 0:
        remainder = str(num % 2)
        binary_value[iteration] = str(remainder)
        iteration = iteration - 1
        num = int(num / 2)
    return "".join(binary_value)
