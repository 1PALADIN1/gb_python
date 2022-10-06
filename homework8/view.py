def show_menu():
    menu = [
        "Показать сотрудников",
        "Добавить сотрудника",
        "Удалить сотрудников",
        "Изменить запись сотрудника",
        "Экспортировать список",
        "Импортировать список",
        "Выход",
    ]

    for item in enumerate(menu, 1):
        print(item[0], "-", item[1])

    return int(input("Выберете пункт меню:\n"))


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
        print(str(index) + ". " + row["firstname"], row["lastname"], row["job_title"], row["phone"], sep='|')
        index += 1


def show_export_formats():
    pass


def print_message(msg):
    print(">>", msg)


def print_delimiter():
    print("=======================================")
