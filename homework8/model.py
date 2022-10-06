import csv

PATH_FILE = "db/data.csv"

_user_list = []


def create_user(row: {}):
    _user_list.append(row)


def delete_user(num):
    del _user_list[num - 1]


def get_users():
    return _user_list


def update_user(num: int, data: {}):
    _user_list[num - 1] = data


def export_csv():
    with open(PATH_FILE, "w", encoding="UTF-8") as file:
        filewriter = csv.writer(file, delimiter=";", lineterminator="\r")
        for row in _user_list:
            filewriter.writerow(row.values())


def import_csv():
    global _user_list
    _user_list = []

    with open(PATH_FILE, "r", encoding="UTF-8") as file:
        filereader = csv.reader(file, delimiter=";", lineterminator="\r")
        for row in filereader:
            _user_list.append({
                "firstname": row[0],
                "lastname": row[1],
                "job_title": row[2],
                "phone": row[3],
            })
