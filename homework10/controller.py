import model.game as game
import model.ai as ai
from bot_token import token as TOKEN
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

TOTAL_CANDIES = 2021

_reply_lobby = [["/rules", "/play"]]
_lobby_markup = ReplyKeyboardMarkup(_reply_lobby, one_time_keyboard=False)
_reply_play_mode = [["/stop"]]
_play_mode_markup = ReplyKeyboardMarkup(_reply_play_mode, one_time_keyboard=False)


def run():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("rules", rules_command))

    play_handler = ConversationHandler(
        entry_points=[CommandHandler("play", play_command)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, player_input_command)],
        },
        fallbacks=[CommandHandler("stop", stop_command)]
    )
    dispatcher.add_handler(play_handler)

    updater.start_polling()
    updater.idle()


def start_command(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет! Добро пожаловать в игру, сыграем партейку? "
                                                       "Используете команду /rules, чтобы узнать правила. "
                                                       "Используйте /play, чтобы начать матч и "
                                                       "/stop, чтобы его закончить.",
                             reply_markup=_lobby_markup)


def rules_command(update, context):
    description = f'На столе лежит {TOTAL_CANDIES} конфета. Играют два игрока делая ход друг после друга. ' \
                  "Первый ход определяется жеребьёвкой. " \
                  f'За один ход можно забрать не более чем {game.MAX_TAKE_CANDIES} конфет. ' \
                  "Все конфеты оппонента достаются сделавшему последний ход. " \
                  "Побеждает игрок, который последним заберёт оставшиеся конфеты."

    context.bot.send_message(update.effective_chat.id, description)


def play_command(update, context):
    game.start_match(TOTAL_CANDIES)
    update.message.reply_text("Матч начат!", reply_markup=_play_mode_markup)
    return _next_turn(update, True)


# Main game loop
def player_input_command(update, context):
    return _next_turn(update)


def stop_command(update, context):
    update.message.reply_text("Игра прервана.", reply_markup=_lobby_markup)
    return ConversationHandler.END


def _next_turn(update, is_cmd=False):
    if is_cmd and game.get_whose_turn() == game.PLAYER1_TURN:
        # ожидаем ввод игрока сразу после старта игры (введена команда /play)
        _print_turn_info(update)
        update.message.reply_text(f'Введите количество конфет (max={game.get_limit_candies()}):',
                                  reply_markup=_play_mode_markup)
        return 1

    # ходит игрок
    if game.get_whose_turn() == game.PLAYER1_TURN:
        # обрабатываем ввод игрока
        try:
            player_candies = int(update.message.text)
            result = game.next_turn(player_candies)
            if _validate_turn(result, update):
                return ConversationHandler.END
        except ValueError:
            update.message.reply_text("Некорректное число конфет, повторите ввод.", reply_markup=_play_mode_markup)
            return 1

    # ходит бот
    _print_turn_info(update)
    bot_candies = ai.calculate_candies(game.get_candies_left(), game.MAX_TAKE_CANDIES)
    result = game.next_turn(bot_candies)
    update.message.reply_text(f'Бот забрал конфет {bot_candies}.', reply_markup=_play_mode_markup)

    if _validate_turn(result, update):
        return ConversationHandler.END

    # передаём ход игроку
    _print_turn_info(update)
    update.message.reply_text(f'Введите количество конфет (max={game.get_limit_candies()}):',
                              reply_markup=_play_mode_markup)

    return 1


def _print_turn_info(update):
    whose_turn = "ИГРОК" if game.get_whose_turn() == game.PLAYER1_TURN else "БОТ"
    update.message.reply_text(f'ХОД {game.get_turn_number()}. Ходит {whose_turn}, '
                              f'осталось конфет {game.get_candies_left()}.', reply_markup=_play_mode_markup)


def _validate_turn(result, update):
    if result == game.PLAYER1_WIN:
        update.message.reply_text("Игра окончена! Победил ИГРОК.", reply_markup=_lobby_markup)
        return True

    if result == game.PLAYER2_WIN:
        update.message.reply_text("Игра окончена! Победил БОТ.", reply_markup=_lobby_markup)
        return True

    return False
