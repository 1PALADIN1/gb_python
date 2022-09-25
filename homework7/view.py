import os

menu_items = {
    1: "Добавить запись",
    2: "Импортировать справочник",
    3: "Экспортировать",
    4: "Выход",
}

format_items = {
    1: "txt",
    2: "csv",
    3: "json",
    4: "xml",
    5: "Назад",
}


def show_menu() -> int:
    print("Выберите пункт меню:")
    for i in range(1, len(menu_items) + 1, 1):
        print(i, "-", menu_items[i])

    while True:
        try:
            input_result = int(input())
            if input_result not in menu_items:
                raise ValueError

            return input_result
        except ValueError:
            print("Некорректный пункт меню, повторите ввод")


def show_format_menu() -> int:
    print("Выберите формат:")
    for i in range(1, len(format_items) + 1, 1):
        print(i, "-", format_items[i])

    while True:
        try:
            input_result = int(input())
            if input_result not in format_items:
                raise ValueError

            return input_result
        except ValueError:
            print("Некорректный пункт меню, повторите ввод")


def show_add_record() -> (str, str, str, str):
    first_name = input("Введитие имя:\n")
    last_name = input("Введитие фамилию:\n")
    phone = input("Введитие телефон:\n")
    description = input("Введитие описание:\n")
    return first_name, last_name, phone, description


def print_message(msg: str):
    print(msg)


def cls():
    # чтобы очистка заработала, нужно установить галочку в конфигурации "Emulate terminal in output console"
    os.system('cls' if os.name == 'nt' else 'clear')
