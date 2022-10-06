import xml.etree.ElementTree as ET
from os.path import exists


def export_data(path_file: str, data: [{}]):
    root = ET.Element("root")
    for row in data:
        record = ET.SubElement(root, "record")

        firstname = ET.SubElement(record, "firstname")
        firstname.text = row["firstname"]

        lastname = ET.SubElement(record, "lastname")
        lastname.text = row["lastname"]

        job_title = ET.SubElement(record, "job_title")
        job_title.text = row["job_title"]

        phone = ET.SubElement(record, "phone")
        phone.text = row["phone"]

    tree = ET.ElementTree(root)
    tree.write(path_file, encoding='utf-8', xml_declaration=True)


def import_data(path_file: str):
    if not exists(path_file):
        return []

    tree = ET.parse(path_file)
    root = tree.getroot()

    result_list = []
    for record in root:
        row = {}
        for field in record:
            if field.tag == "firstname":
                row["firstname"] = field.text
            elif field.tag == "lastname":
                row["lastname"] = field.text
            elif field.tag == "job_title":
                row["job_title"] = field.text
            elif field.tag == "phone":
                row["phone"] = field.text

        result_list.append(row)

    return result_list
