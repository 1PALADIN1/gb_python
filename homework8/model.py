from exporter import csv_exporter as csv
from exporter import json_exporter as json
from exporter import xml_exporter as xml

CSV_FILE = "exporter/db/data.csv"
JSON_FILE = "exporter/db/data.json"
XML_FILE = "exporter/db/data.xml"

_user_list = []


def create_user(row: {}):
    _user_list.append(row)


def delete_user(num):
    if num < 1 or num > len(_user_list):
        raise RuntimeError("Пользователь с указанным id не существует")

    del _user_list[num - 1]


def get_users():
    return _user_list


def update_user(num: int, data: {}):
    if num < 1 or num > len(_user_list):
        raise RuntimeError("Пользователь с указанным id не существует")

    _user_list[num - 1] = data


def export_data(export_format):
    if export_format == "csv":
        csv.export_data(CSV_FILE, _user_list)
    elif export_format == "json":
        json.export_data(JSON_FILE, _user_list)
    elif export_format == "xml":
        xml.export_data(XML_FILE, _user_list)


def import_data(import_format):
    global _user_list

    if import_format == "csv":
        _user_list = csv.import_data(CSV_FILE)
    elif import_format == "json":
        _user_list = json.import_data(JSON_FILE)
    elif import_format == "xml":
        _user_list = xml.import_data(XML_FILE)
