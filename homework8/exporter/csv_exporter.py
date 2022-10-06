import csv
from os.path import exists


def export_data(path_file: str, data: [{}]):
    with open(path_file, "w", encoding="UTF-8") as file:
        filewriter = csv.writer(file, delimiter=";", lineterminator="\r")
        for row in data:
            filewriter.writerow(row.values())


def import_data(path_file: str):
    if not exists(path_file):
        return []

    result_list = []

    with open(path_file, "r", encoding="UTF-8") as file:
        filereader = csv.reader(file, delimiter=";", lineterminator="\r")
        for row in filereader:
            result_list.append({
                "firstname": row[0],
                "lastname": row[1],
                "job_title": row[2],
                "phone": row[3],
            })

    return result_list
