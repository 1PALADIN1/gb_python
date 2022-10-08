import random


def calculate_candies(candies_left, max_take_candies):
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
