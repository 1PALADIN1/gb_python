# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
def task1():
    result = []
    with open("task1.txt", "r") as f:
        input_lines = f.readlines()
        for line in input_lines:
            rs = " ".join(filter(lambda word: "абв" not in word, line.split()))
            result.append(rs)

    with open("task1_result.txt", "w") as f:
        for line in result:
            f.write(line)
            f.write("\n")


# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно
# взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
def task2():
    pass


# Создайте программу для игры в "Крестики-нолики".
def task3():
    pass


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
def task4():
    pass


task1()
task2()
task3()
task4()
