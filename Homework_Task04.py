# 4.	Написать программу преобразования десятичного числа в двоичное
number = 45


def dex_to_num_converter(num):
    bin_num = ""
    while num > 0:
        bin_num = f"{num % 2}{bin_num}"
        num //= 2
    return bin_num


print(dex_to_num_converter(number))