# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
def task1():
    num = int(input("Введите день недели:\n"))
    if num > 7 or num < 1:
        print("некорректный день недели")
        return

    if num == 6 or num == 7:
        print("да")
        return

    print("нет")


# 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def task2():
    for i in range(8):
        x = 1 if check_bitmask(i, 0) else 0
        y = 1 if check_bitmask(i, 1) else 0
        z = 1 if check_bitmask(i, 2) else 0

        result = "да" if validate_expr(x, y, z) else "нет"
        print("Утверждение истинно для набора (" + str(x) + ", " + str(y) + ", " + str(z) + ")? " + result)


def check_bitmask(num: int, bit_order: int) -> bool:
    mask = 1 << bit_order
    return (num & mask) == mask


def validate_expr(x: int, y: int, z: int) -> bool:
    return not (x or y or z) == (not x and not y and not z)


# task1()
task2()

