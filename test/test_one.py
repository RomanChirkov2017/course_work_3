from pathlib import Path
import pytest
from classes.classes import Operation

from funktions.funktions import *

project = Path(__file__).parent
file_name = Path(project.parent, 'side_file', 'operations.json')


def test_read_json():
    assert read_json(file_name) is not None
    assert type(read_json(file_name)[1]) == dict


def test_create_list_class():
    assert len(create_list_class(file_name)) > 0


def test_class_create(jsons):
    ex_class = Operation(**jsons)
    ex_class.format_card(ex_class.to)
    ex_class.format_card(ex_class.from_)

    assert ex_class.beautiful_output() is None
    assert ex_class.id == 619287771
    assert ex_class.to[-4:] == '7621'
    assert ex_class.from_[-4:] == '4901'

