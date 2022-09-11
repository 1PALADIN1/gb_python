# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def task1():
    print("Задание 1")

    ls = [2, 3, 5, 9, 3]
    result = 0
    for i in range(len(ls)):
        if i % 2 != 0:
            result += ls[i]

    print("Результат:", result)


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
def task2():
    print("Задание 2")
    print(pair_mul([2, 3, 4, 5, 6]))
    print(pair_mul([2, 3, 5, 6]))
    print(pair_mul([2]))


def pair_mul(ls: []) -> []:
    result = []

    for i in range(len(ls)):
        j = len(ls) - i - 1
        if i > j:
            break

        result.append(ls[i] * ls[j])

    return result


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def task3():
    print("Задание 3")


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
def task4():
    print("Задание 4")
    print(decimal_to_bin(45))
    print(decimal_to_bin(3))
    print(decimal_to_bin(2))
    print(decimal_to_bin(0))
    print(decimal_to_bin(15))


def decimal_to_bin(num) -> str:
    if num == 0:
        return "0"

    result = []
    while num > 0:
        bit = num % 2
        num = int(num / 2)
        result.append(bit)

    result_str = ""
    result.reverse()
    for i in range(len(result)):
        result_str += str(result[i])

    return result_str


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def task5():
    print("Задание 5")


# task1()
# task2()
# task3()
task4()
# task5()
