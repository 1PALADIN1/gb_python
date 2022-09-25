import model
import view


def run():
    logic = {
        1: _add,
        2: _import_records,
        3: _export_records,
    }

    while True:
        input_result = view.show_menu()
        if input_result == 4:
            break

        view.cls()
        logic[input_result]()


def _add():
    first_name, last_name, phone, description = view.show_add_record()
    model.add_record(first_name, last_name, phone, description)
    view.print_message("Запись успешно добавлена!")


def _import_records():
    input_result = view.show_format_menu()
    if input_result == 5:
        view.cls()
        return

    logic = {
        1: model.import_txt,
        2: model.import_csv,
        3: model.import_json,
        4: model.import_xml,
    }
    logic[input_result]()
    view.print_message("Список успешно импортирован!")


def _export_records():
    input_result = view.show_format_menu()
    if input_result == 5:
        view.cls()
        return

    logic = {
        1: model.export_txt,
        2: model.export_csv,
        3: model.export_json,
        4: model.export_xml,
    }
    logic[input_result]()
    view.print_message("Список успешно экспортирован!")
