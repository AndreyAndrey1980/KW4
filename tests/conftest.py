import json

import pytest

from config import DATA_TEST
from src.get_api_hh import get_api_hh
from src.json_saver import json_saver


@pytest.fixture
def fixture_class_get_hh_valid():
    return get_api_hh().get_vacancy_from_api('python')


@pytest.fixture
def fixture_class_get_hh_negative():
    return get_api_hh().get_vacancy_from_api("1")


@pytest.fixture
def fixture_class_json_saver():
    return json_saver()

@pytest.fixture
def fixture_class_list():
    json_saver = json_saver()
    json_saver.save_file([{'name': 'Kris'}])
    return json_saver


@pytest.fixture
def new_file():
    with open(DATA_TEST, encoding='utf-8') as file:
        return json.load(file)