# 2. Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
nums = [2, 3, 4, 5, 6]


def product_of_pairs(numbers: list):
    res = []
    for i, num in enumerate(numbers):
        if i == len(numbers)//2:
            if len(numbers) % i == 0:
                break
            else:
                res.append(numbers[i] * numbers[-i - 1])
                break
        else:
            res.append(numbers[i] * numbers[-i - 1])
    return res


print(product_of_pairs(nums))