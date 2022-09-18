import math
import random


# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$
def task1():
    d = float(input("Введите d (пример, 0.001):\n"))

    # ищем количество знаков после запятой
    digits = 0
    while d < 1:
        if d == 0:
            break

        d *= 10
        digits += 1

    print("Результат:", round(math.pi, digits))


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def task2():
    n = int(input("Введите число:\n"))

    result = []
    i = 2
    while i <= math.sqrt(n):
        while n % i == 0:
            n = int(n / i)
            result.append(i)
        i += 1

    if n != 1:
        result.append(n)

    print(result)


# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
def task3():
    input_string = input("Введите последовательность чисел через пробел (пример, 2 3 5 9 3):\n")
    ls = [int(i) for i in input_string.split()]
    d = {}
    for x in ls:
        if not (x in d):
            d[x] = 0

        d[x] += 1

    result = []
    for key, value in d.items():
        if value == 1:
            result.append(key)

    print(result)


# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
def task4():
    k = int(input("Введите число k:\n"))

    result = ""
    while k >= 0:
        a = random.randint(0, 100)
        if a == 0:
            continue

        if k == 0:
            result += str(a)
        elif k == 1:
            result += str(a) + "x + "
        else:
            result += str(a) + "x^" + str(k) + " + "

        k -= 1

    result += " = 0"
    print(result)

    f = open("task4.txt", "w")
    f.write(result)
    f.close()


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
def task5():
    pass


# task1()
# task2()
# task3()
task4()
task5()
