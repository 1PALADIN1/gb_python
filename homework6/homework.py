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
    pass


task1()
# task2()
