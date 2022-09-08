import random


# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
def task1():
    num = input("Введите число:\n")
    sum = 0
    for n in num:
        if n.isdigit():
            sum += int(n)

    print("Сумма:", sum)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)
def task2():
    num = int(input("Введите число:\n"))
    if num < 1:
        print("Число должно быть больше 1!")
        return

    result = []
    seq = "("
    for n in range(1, num+1, 1):
        el = 1
        for i in range(1, n+1, 1):
            el *= i
            seq += str(i)

        result.append(el)
        if n < num:
            seq += ", "

    seq += ")"
    print(result, seq)


# 3. Задайте список из n чисел последовательности (1 + 1/n)^n выведите на экран их сумму.
def task3():
    num = int(input("Введите число:\n"))
    if num < 1:
        print("Число должно быть больше 1!")
        return

    result = 0
    for n in range(1, num+1, 1):
        result += (1 + 1/n) ** n

    print(result)


# 4. Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся
# в файле file.txt в одной строке одно число.
def task4():
    num = int(input("Введите число:\n"))
    if num < 1:
        print("Число должно быть больше 1!")
        return

    ls = []
    for n in range(-num, num+1, 1):
        ls.append(n)

    f = open("file.txt", "r")
    result = 1
    for line in f:
        line = line.strip()
        if not line.isdigit():
            print(line, " - не число!")
            continue
        index = int(line)

        if index >= len(ls):
            print("Некорректный индекс [", index, "], всего элементов", len(ls))
            continue

        result *= ls[index]

    f.close()
    print("Результат:", result)


# 5. Реализуйте алгоритм перемешивания списка.
def task5():
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    num_of_shuffles = len(seq)

    for _ in range(num_of_shuffles):
        first_index = random.randint(0, len(seq)-1)
        second_index = random.randint(0, len(seq)-1)

        if first_index == second_index:
            continue

        seq[first_index], seq[second_index] = seq[second_index], seq[first_index]

    print("Результат:", seq)


task1()
task2()
task3()
task4()
task5()
