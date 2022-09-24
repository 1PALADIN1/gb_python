# 1. Орел и решка
def task1():
    print("Задание 1")

    with open("task1.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            result = calc_tails(line)
            print(line.strip(), "->", result)


# eagle and tails
def calc_tails(input_str: str) -> int:
    tails_symbol = "Р"
    eagle_symbol = "О"

    result = 0
    tails_counter = 0
    for s in input_str:
        if s == tails_symbol:
            tails_counter += 1
            continue

        if s == eagle_symbol:
            result = max(result, tails_counter)
            tails_counter = 0
            continue

    result = max(result, tails_counter)
    return result


# 2. Измените код одной из решенных ранее задач (любой, с прошлых семинаров),
# применив лямбды, filter, map, zip, enumerate, списочные выражения.
def task2():
    print("Задание 2")
    # Задание 2 из домашней работы 3. Напишите программу, которая найдёт произведение пар чисел списка.
    # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    # Пример:
    # [2, 3, 4, 5, 6] => [12, 15, 16];
    # [2, 3, 5, 6] => [12, 15]
    input_string = input("Введите последовательность чисел через пробел (пример, 2 3 4 5 6):\n")
    ls = [int(i) for i in input_string.split()]

    ls_reversed = ls.copy()
    ls_reversed.reverse()

    size = len(ls)
    mid = int(size / 2) if size % 2 == 0 else int(size / 2) + 1

    print(
        list(map(lambda x: x[0] * x[1], list(zip(ls[:mid], ls_reversed[:mid]))))
    )


task1()
task2()
