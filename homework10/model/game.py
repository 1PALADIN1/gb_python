import random

# game states
PLAYER1_TURN = 1  # игрок
PLAYER2_TURN = 2  # ИИ
PLAYER1_WIN = 3
PLAYER2_WIN = 4

MAX_TAKE_CANDIES = 28

_candies_left = 0
_turn_number = 0
_whose_turn = 0


def start_match(max_candies):
    global _candies_left, _turn_number, _whose_turn
    _candies_left = max_candies
    _turn_number = 1
    _whose_turn = random.choice([PLAYER1_TURN, PLAYER2_TURN])


def get_turn_number():
    return _turn_number


def get_candies_left():
    return _candies_left


def get_whose_turn():
    return _whose_turn


def get_limit_candies():
    return MAX_TAKE_CANDIES if MAX_TAKE_CANDIES < _candies_left else _candies_left


def next_turn(take_candies):
    global _turn_number, _whose_turn, _candies_left
    limit_candies = get_limit_candies()
    if take_candies > limit_candies:
        raise ValueError(f'Количество конфет не должно превышать {limit_candies}!')

    _candies_left -= take_candies
    if _candies_left == 0:
        return PLAYER1_WIN if _whose_turn == PLAYER1_TURN else PLAYER2_WIN

    _turn_number += 1
    _whose_turn = PLAYER1_TURN if _whose_turn == PLAYER2_TURN else PLAYER2_TURN
    return _whose_turn
