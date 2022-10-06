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
            model.delete_user(num)
        elif result == 4:
            # Изменить запись
            num, data = view.show_update_user()
            model.update_user(num, data)
        elif result == 5:
            # Экспортировать список
            model.export_csv()
            view.print_message("Список успешно экспортирован!")
        elif result == 6:
            # Импортировать список
            model.import_csv()
            view.print_message("Список успешно импортирован!")
        elif result == 7:
            view.print_message("Bye, bye!")
            return
        else:
            view.print_message("Команда не распознана")
