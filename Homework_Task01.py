# 1.	Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4
n = 10


def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)


print(sum_of_odds(n))