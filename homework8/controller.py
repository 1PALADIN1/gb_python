import view
import model


def run():
    while True:
        view.print_delimiter()
        result = view.show_menu()
        if result == 1:
            # Показать список сотрудников
            users = model.get_users()
            view.show_users_list(users)
        elif result == 2:
            # Добавить запись
            data = view.show_add_user()
            model.create_user(data)
            view.print_message("Запись успешно добавлена!")
        elif result == 3:
            # Удалить запись
            num = view.show_delete_user()
            try:
                model.delete_user(num)
                view.print_message("Сотрудник удалён!")
            except RuntimeError as ex:
                view.print_message(ex)

        elif result == 4:
            # Изменить запись
            num, data = view.show_update_user()
            try:
                model.update_user(num, data)
                view.print_message("Сотрудник изменён!")
            except RuntimeError as ex:
                view.print_message(ex)

        elif result == 5:
            # Экспортировать список
            view.print_delimiter()
            export_logic()
        elif result == 6:
            # Импортировать список
            view.print_delimiter()
            import_logic()
        elif result == 7:
            view.print_message("Bye, bye!")
            return
        else:
            view.print_message("Команда не распознана")


def export_logic():
    num = view.show_export_formats()

    if num == 1:
        model.export_data("csv")
    elif num == 2:
        model.export_data("json")
    elif num == 3:
        model.export_data("xml")
    else:
        return

    view.print_message("Список успешно экспортирован!")


def import_logic():
    num = view.show_export_formats()

    if num == 1:
        model.import_data("csv")
    elif num == 2:
        model.import_data("json")
    elif num == 3:
        model.import_data("xml")
    else:
        return

    view.print_message("Список успешно импортирован!")
