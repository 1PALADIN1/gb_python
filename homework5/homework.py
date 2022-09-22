import random
import os

max_take_candies = 28


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
def task2(play_with_bot: bool):
    candies = 2021
    turn_num = 1
    whose_turn = random.choice([1, 2])
    print("Начинает игрок", whose_turn)

    while candies > 0:
        print("============== ХОД", turn_num, "==============")

        if not play_with_bot:
            # играют два игрока
            take_candies = candy_player_turn(whose_turn, candies)

            candies -= take_candies
            if candies > 0:
                cls()
        else:
            # играем с ботом
            # 1 - игрок
            # 2 - бот
            if whose_turn == 1:
                take_candies = candy_player_turn(whose_turn, candies)
                if candies > 0:
                    cls()
            else:
                take_candies = candy_bot_turn(candies)
                print("Бот забрал", take_candies, "конфет")

        # переключаем на следующий ход
        candies -= take_candies
        if candies > 0:
            turn_num += 1
            whose_turn = 1 if whose_turn == 2 else 2

    if not play_with_bot:
        print("Игра окончена! Победил игрок", whose_turn)
        return

    winner = "Бот" if whose_turn == 2 else "Игрок"
    print("Игра окончена! Победил", winner)


# логика для игрока
def candy_player_turn(player: int, candies_left: int) -> int:
    print("Ходит игрок", player, "\nОсталось конфет:", candies_left)

    while True:
        max_candies = max_take_candies if max_take_candies < candies_left else candies_left
        result = int(input("Введите количество конфет (MAX: " + str(max_candies) + "):\n"))\

        if result > max_candies:
            print("Количество конфет не должно превышать " + str(max_candies) + "!")
            continue

        if result <= 0:
            print("Количество конфет должно быть больше 0!")
            continue

        break

    return result


# логика для бота
def candy_bot_turn(candies_left: int) -> int:
    print("Ходит бот\nОсталось конфет:", candies_left)
    if candies_left <= max_take_candies:
        # забираем оставшиеся конфеты и побеждаем
        return candies_left

    # стремимся оставить игроку такое число конфет
    target = 1 + max_take_candies
    if candies_left == target:
        # бот проиграл, выдаём любое число
        return random.randint(1, max_take_candies)

    # необходимо, чтобы у бота получалось 29 58 87 116 145 и т.д. для выигрыша
    ml = int(candies_left / target)
    next_win_number = target * ml
    if candies_left - next_win_number == 0:
        return max_take_candies

    return candies_left - next_win_number


def cls():
    # чтобы очистка заработала, нужно установить галочку в конфигурации "Emulate terminal in output console"
    os.system('cls' if os.name == 'nt' else 'clear')


# 3. Создайте программу для игры в "Крестики-нолики".
def task3():
    pass


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
def task4():
    pass


# task1()
# task2(False)
task2(True)
task3()
task4()
