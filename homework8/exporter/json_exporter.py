import json
from os.path import exists


def export_data(path_file: str, data: [{}]):
    json_string = json.dumps(data)
    with open(path_file, "w") as f:
        f.write(json_string)


def import_data(path_file: str):
    if not exists(path_file):
        return []

    with open(path_file, "r") as f:
        return json.loads(f.read())
