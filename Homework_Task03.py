# 3.	В заданном списке вещественных чисел найдите разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
numbers = [1.1, 1.2, 3.1, 5, 10.01]


def substract_fractional_parts(nums: list):
    frac_numbers = []
    for num in numbers:
        if type(num) != int:
            frac_numbers.append(round(num % 1, 2))
    return max(frac_numbers) - min(frac_numbers)


print(substract_fractional_parts(numbers))


