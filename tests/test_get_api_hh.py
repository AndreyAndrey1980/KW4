from abc import ABC

from src.abstract_api_hh import abstract_get_api_hh
from src.get_api_hh import get_api_hh


def test_issubclass():
    assert issubclass(get_api_hh, ABC)
    assert issubclass(get_api_hh, abstract_get_api_hh)


def test_get_vacancy_from_api(fixture_class_get_hh_valid, fixture_class_get_hh_negative):
    assert len(fixture_class_get_hh_valid) > 0
    assert fixture_class_get_hh_negative == "Такая вакансия не найдена"


def test_all_vacancy():
    get_api = get_api_hh()
    get_api.get_vacancy_from_api('python')

    assert len(get_api.all_vacancy) > 0