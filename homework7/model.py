import json
import xml.etree.ElementTree as ET

# справочник с данными
_data = []
_data_size = 4


# добавление новой записи в справочник
def add_record(first_name: str, last_name: str, phone: str, description: str):
    _data.append([first_name, last_name, phone, description])


# импорт справочников
def import_txt():
    global _data
    _data = []

    with open("db/model.txt", "r") as f:
        lines = f.readlines()

        i = 0
        record = []
        for line in lines:
            record.append(line.strip())

            i += 1
            if i == _data_size:
                _data.append(record)
                i = 0
                record = []


def import_csv():
    global _data
    _data = []

    with open("db/model.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            _data.append(
                list(map(lambda x: x.strip(), line.split(";")))
            )


def import_json():
    global _data
    with open("db/model.json", "r") as f:
        _data = json.loads(f.read())


def import_xml():
    global _data
    _data = []

    tree = ET.parse("db/model.xml")
    root = tree.getroot()

    for record in root:
        rs = ["", "", "", ""]
        for field in record:
            if field.tag == "first_name":
                rs[0] = field.text
            elif field.tag == "last_name":
                rs[1] = field.text
            elif field.tag == "phone":
                rs[2] = field.text
            else:
                rs[3] = field.text

        _data.append(rs)


# экспорт справочников
def export_txt():
    with open("db/model.txt", "w") as f:
        for lines in _data:
            f.write("\n".join(lines) + "\n")


def export_csv():
    with open("db/model.csv", "w") as f:
        for lines in _data:
            f.write(";".join(lines) + "\n")


def export_json():
    json_string = json.dumps(_data)
    with open("db/model.json", "w") as f:
        f.write(json_string)


def export_xml():
    root = ET.Element("root")

    for lines in _data:
        record = ET.SubElement(root, "record")
        first_name = ET.SubElement(record, "first_name")
        first_name.text = lines[0]
        last_name = ET.SubElement(record, "last_name")
        last_name.text = lines[1]
        phone = ET.SubElement(record, "phone")
        phone.text = lines[2]
        description = ET.SubElement(record, "description")
        description.text = lines[3]

    tree = ET.ElementTree(root)
    tree.write("db/model.xml", encoding='utf-8', xml_declaration=True)
