import json
from pathlib import Path
from classes.classes import Operation
from testings import b


def read_json(file_name) -> list[dict]:
    """Читает JSON файл"""
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = json.load(file)

    return result


def create_list_class(file_name):
    """Создаёт экземпляры класса"""
    list_operations: list = read_json(file_name)

    list_operations.sort(key=lambda d: d.get('date', 'a'), reverse=True)

    list_class = []
    for operation in list_operations:
        try:
            if operation['state'] == "CANCELED":
                raise KeyError

            list_class.append(Operation(**operation))

        except KeyError:
            continue

    return list_class
