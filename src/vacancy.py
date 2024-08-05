from src.json_saver import json_saver


class vacancy:
    """
    Данный код представляет собой определение класса vacancy, который используется для хранения информации о вакансиях.
    Класс имеет атрибут list_vacancies, который представляет собой список вакансий.
    Метод init является конструктором класса и принимает следующие параметры:
    1. name_vacancy: название вакансии;
    2. salary_from: минимальная зарплата по вакансии;
    3. salary_to: максимальная зарплата по вакансии;
    4. url: URL-адрес, связанный с вакансией;
    5. city: город, в котором находится вакансия.
    В методе init происходит добавление текущего объекта в список list_vacancies. Это позволяет хранить все вакансии в одном списке.
    """
    list_vacancies = []

    def __init__(self, name_vacancy: str, salary_from: int, salary_to: int, url: str, city: str):
        self.name_vacancy = name_vacancy
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.city = city
        self.list_vacancies.append(self)

    def __repr__(self):
        return (f"\nName of vacancy: {self.name_vacancy}\n"
                f"Salary from: {self.salary_from}\n"
                f"Salary to: {self.salary_to}\n"
                f"City: {self.city}\n"
                f"URL: {self.url}\n")

    def __lt__(self, other):
        if other.salary_to < self.salary_to:
            return True

    @classmethod
    def get_vacancy_list(cls, list_vacancy, city, salary_from) -> list:
        """
        Получить список с указанием вакансий. Этот список с копией вакансии класса
        ::return: новый список с копией вакансии класса
        """
        for vacancy in list_vacancy:
            name_vacancy = vacancy["name"]
            url = vacancy["alternate_url"]
            if vacancy["area"]["name"] == city:
                city = vacancy["area"]["name"]
            if vacancy["salary"] is None:
                continue
            elif vacancy["salary"]["to"] is not None and vacancy["salary"]["from"]:
                if vacancy["salary"]["from"] >= salary_from:
                    salary_from = vacancy["salary"]["from"]
                    salary_to = vacancy["salary"]["to"]
                    cls(name_vacancy, salary_from, salary_to, url, city)
                else:
                    continue
            else:
                continue
        return cls.list_vacancies
