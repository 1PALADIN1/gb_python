# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def task1():
    print("Задание 1")
    input_string = input("Введите последовательность чисел через пробел (пример, 2 3 5 9 3):\n")
    ls = [int(i) for i in input_string.split()]
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
    input_string = input("Введите последовательность чисел через пробел (пример, 2 3 4 5 6):\n")
    ls = [int(i) for i in input_string.split()]
    print(pair_mul(ls))

    # tst
    # print(pair_mul([2, 3, 4, 5, 6]))
    # print(pair_mul([2, 3, 5, 6]))
    # print(pair_mul([2]))


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
    input_string = input("Введите последовательность чисел через пробел (пример, 1.1 1.2 3.1 5 10.01):\n")
    ls = [float(i) for i in input_string.split()]

    min_fr = 1
    max_fr = 0

    for el in ls:
        fract = el - int(el)

        if fract < min_fr:
            min_fr = fract

        if fract > max_fr:
            max_fr = fract

    if min_fr >= 1:
        min_fr = 0

    print("Результат:", max_fr - min_fr)


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
def task4():
    print("Задание 4")
    num = int(input("Введите число:\n"))
    print(decimal_to_bin(num))

    # tst
    # print(decimal_to_bin(45))
    # print(decimal_to_bin(3))
    # print(decimal_to_bin(2))
    # print(decimal_to_bin(0))
    # print(decimal_to_bin(15))


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
    num = int(input("Введите число:\n"))
    print(fibo(num))


def fibo(n: int) -> []:
    fibo_list = []
    negofibo_list = []

    for i in range(n + 1):
        if i == 0:
            fibo_list.append(i)
            continue

        if i == 1:
            fibo_list.append(i)
            negofibo_list.append(i)
            continue

        fibo_num = fibo_list[i - 1] + fibo_list[i - 2]
        fibo_list.append(fibo_num)
        negofibo_list.append(negofibo(fibo_num, i))

    negofibo_list.reverse()
    return negofibo_list + fibo_list


# F(-n) = (-1) ^ (n + 1) * F(n)
def negofibo(fn: int, i: int) -> int:
    sign = (-1) ** (i + 1)
    return sign * fn


task1()
task2()
task3()
task4()
task5()
