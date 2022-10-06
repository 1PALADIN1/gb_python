def show_menu():
    menu = [
        "Показать сотрудников",
        "Добавить сотрудника",
        "Удалить сотрудника",
        "Изменить запись сотрудника",
        "Экспортировать список",
        "Импортировать список",
        "Выход",
    ]

    for item in enumerate(menu, 1):
        print(item[0], "-", item[1])

    while True:
        try:
            input_result = int(input("Выберете пункт меню:\n"))
            if input_result < 1 or input_result > len(menu):
                raise ValueError

            return input_result
        except ValueError:
            print_message("Некорректный пункт меню, повторите ввод")


def show_add_user():
    firstname = input("Введите имя пользователя:\n")
    lastname = input("Введите фамилию пользователя:\n")
    job_title = input("Введите должность:\n")
    phone = input("Введите телефон:\n")

    return {
        "firstname": firstname,
        "lastname": lastname,
        "job_title": job_title,
        "phone": phone,
    }


def show_delete_user():
    return int(input("Укажите номер записи:\n"))


def show_update_user():
    num = int(input("Укажите номер записи:\n"))
    return num, show_add_user()


def show_users_list(data: [{}]):
    if len(data) == 0:
        print("Список пуст")
        return

    index = 1
    for row in data:
        print(f'{index}. {row["firstname"]}', row["lastname"], row["job_title"], row["phone"], sep='|')
        index += 1


def show_export_formats():
    formats = [
        "csv",
        "json",
        "xml",
        "Назад",
    ]

    for item in enumerate(formats, 1):
        print(item[0], "-", item[1])

    while True:
        try:
            input_result = int(input("Выберете формат:\n"))
            if input_result < 1 or input_result > len(formats):
                raise ValueError

            return input_result
        except ValueError:
            print_message("Некорректный пункт меню, повторите ввод")


def print_message(msg):
    print(">>", msg)


def print_delimiter():
    print("=======================================")
