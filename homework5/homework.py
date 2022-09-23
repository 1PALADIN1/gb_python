import random
import os


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
max_take_candies = 28


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
# Состояния игры
PLAYER1_TURN = 1  # ходит первый игрок
PLAYER2_TURN = 2  # ходит второй игрок
PLAYER1_WIN = 3  # первый игрок победил
PLAYER2_WIN = 4  # второй игрок победил
TIE = 5  # игра закончилась ничьёй

# Фигуры
CROSS = 1
ZERO = 2

EMPTY_CELL = "_"
CROSS_CELL = "X"
ZERO_CELL = "0"


def task3():
    turn_num = 1
    whose_turn = random.choice([1, 2])
    current_figure = CROSS
    field = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
    print("Начинает игрок", whose_turn)

    game_processed = True
    while game_processed:
        if turn_num > 1:
            cls()
            print("============== ХОД", turn_num, "==============")
            draw_field(field)
        else:
            print("============== ХОД", turn_num, "==============")

        tic_tac_toe_player_turn(whose_turn, current_figure, field)
        game_loop_result = validate_turn(whose_turn, field)
        turn_num += 1

        current_figure = CROSS if current_figure == ZERO else ZERO
        if game_loop_result == PLAYER1_TURN:
            whose_turn = 2
            continue

        if game_loop_result == PLAYER2_TURN:
            whose_turn = 1
            continue

        # игра окончена, нашёлся победитель (или ничья)
        draw_field(field)
        print("Игра окончена! Результат:")
        if game_loop_result == PLAYER1_WIN:
            print("Победил игрок 1")
        elif game_loop_result == PLAYER2_WIN:
            print("Победил игрок 2")
        else:
            print("Ничья")
        break


def tic_tac_toe_player_turn(player: int, figure: int, field: [[]]):
    cell = CROSS_CELL if figure == CROSS else ZERO_CELL
    print("Ходит игрок", player, "[" + cell + "]")

    while True:
        x = int(input("Введите координату x (от 0 до 2)\n"))
        y = int(input("Введите координату y (от 0 до 2)\n"))

        if x < 0 or x > 2:
            print("Некорректная координата x")
            continue

        if y < 0 or y > 2:
            print("Некорректная координата y")
            continue

        if field[y][x] != EMPTY_CELL:
            print("Ячейка уже занята")
            continue

        break

    # ставим на поле крестик или нолик
    if figure == CROSS:
        field[y][x] = CROSS_CELL
    else:
        field[y][x] = ZERO_CELL


def validate_turn(current_player_turn: int, field: [[]]) -> int:
    # проверяем есть ли победитель
    # проверяем по горизонтали
    for y in range(len(field)):
        cross_cells = 0
        zero_cells = 0

        for x in range(len(field)):
            if field[y][x] == CROSS_CELL:
                cross_cells += 1

            if field[y][x] == ZERO_CELL:
                zero_cells += 1

        if cross_cells == 3 or zero_cells == 3:
            # определился победитель после очередного хода
            return PLAYER1_WIN if current_player_turn == PLAYER1_TURN else PLAYER2_WIN

    # проверяем по вертикали
    for y in range(len(field)):
        cross_cells = 0
        zero_cells = 0

        for x in range(len(field)):
            if field[x][y] == CROSS_CELL:
                cross_cells += 1

            if field[x][y] == ZERO_CELL:
                zero_cells += 1

        if cross_cells == 3 or zero_cells == 3:
            # определился победитель после очередного хода
            return PLAYER1_WIN if current_player_turn == PLAYER1_TURN else PLAYER2_WIN

    # проверяем по диагонали
    # по основной диагонали
    if field[0][0] == field[1][1] and field[0][0] == field[2][2] and field[0][0] != EMPTY_CELL:
        # определился победитель после очередного хода
        return PLAYER1_WIN if current_player_turn == PLAYER1_TURN else PLAYER2_WIN

    # по второстепенной диагонали
    if field[2][0] == field[1][1] and field[2][0] == field[0][2] and field[2][0] != EMPTY_CELL:
        # определился победитель после очередного хода
        return PLAYER1_WIN if current_player_turn == PLAYER1_TURN else PLAYER2_WIN

    # проверяем полностью ли заполено поле (ничья)
    empty_cells = 0
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == EMPTY_CELL:
                empty_cells += 1

    # пустых ячеек не нашлось, ничья
    if empty_cells == 0:
        return TIE

    # передаём ход дальше
    return PLAYER1_TURN if current_player_turn == PLAYER2_TURN else PLAYER1_TURN


def draw_field(field: [[]]):
    for y in range(len(field)):
        for x in range(len(field[y])):
            print("|", field[y][x], "|", end="")
        print()


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
def task4():
    pass


# task1()
# task2(False)
# task2(True)
task3()
task4()
