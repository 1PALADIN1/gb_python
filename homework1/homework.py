import math


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


# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3
def task3():
    print("Плоскость для точки (34, -30) =", define_plane(34, -30))
    print("Плоскость для точки (2, 4) =", define_plane(2, 4))
    print("Плоскость для точки (-34, -30) =", define_plane(-34, -30))
    print("Плоскость для точки (2, -4) =", define_plane(2, -4))

    result = define_plane(0, -4)
    result_string = "точка находится на оси" if result == 0 else str(result)
    print("Плоскость для точки (0, -4) =", result_string)

    result = define_plane(1, 0)
    result_string = "точка находится на оси" if result == 0 else str(result)
    print("Плоскость для точки (1, 0) =", result_string)


def define_plane(x: int, y: int) -> int:
    if x > 0 and y > 0:
        return 1

    if x < 0 and y > 0:
        return 2

    if x < 0 and y < 0:
        return 3

    if x > 0 and y < 0:
        return 4

    return 0


# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
def task4():
    q = int(input("Введите номер четверти:\n"))
    output = {
        1: "x > 0 и y > 0",
        2: "x < 0 и y > 0",
        3: "x < 0 и y < 0",
        4: "x > 0 и y < 0"
    }

    if not (q in output):
        print("Некорректный номер четверти!")
        return

    print("Для четверти", q, "диапазон значений:", output[q])


# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
def task5():
    print("Расстояние между точками A(3,6) и B(2,1):", distance(3, 6, 2, 1))
    print("Расстояние между точками A(7,-5) и B(1,-1):", distance(7, -5, 1, -1))


def distance(ax: float, ay: float, bx: float, by: float) -> float:
    sqr_magnitude = (bx - ax)**2 + (by - ay)**2
    return math.sqrt(sqr_magnitude)


task1()
task2()
task3()
task4()
task5()
