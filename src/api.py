import requests
from abc import ABC, abstractmethod
from src.vacancy import Vacancies, Vacancy


class GetVacancies(ABC):
    """Абстрактный класс для получения вакансий"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, pages: int):
        pass


class HH_Api(GetVacancies):
    """Класс для получения вакансий с HH.ru"""

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__params = {"text": "", "per_page": "10", "page": 0, "area": 113}

    def get_vacancies(self, keyword: str, pages: int):
        """Получает вакансии с hh.ru по ключевому слову. Возвращает список вакансий."""
        hh_list = Vacancies()
        for page in range(pages):
            self.__params["text"] = keyword
            self.__params["page"] = page

            response = requests.get(self.__base_url, params=self.__params)
            response_json = response.json()

            for vac in response_json["items"]:
                vac_id = vac.get("id")
                name = vac.get("name", "")
                city = vac.get("area", "").get("name", "")

                if vac["salary"]:
                    salary = vac["salary"]
                    currency = salary.get("currency", "RUR")  # Используем "RUR" по умолчанию, если валюта не указана

                    salary_from = salary.get("from", 0)  # Используем 0 по умолчанию, если значение не указано
                    salary_to = salary.get("to", 0)  # Используем 0 по умолчанию, если значение не указано
                else:
                    salary_from = 0
                    salary_to = 0
                    currency = "RUR"

                employment = vac["employment"]["name"]
                url = vac["alternate_url"]

                # Создаем словарь salary
                salary_dict = {'from': salary_from, 'to': salary_to}

                # Передаем словарь salary в конструктор
                new_vac = Vacancy(vac_id, name, city, salary_dict, currency, employment, url)
                hh_list.add_vacancy(new_vacancy=new_vac)
        return hh_list
