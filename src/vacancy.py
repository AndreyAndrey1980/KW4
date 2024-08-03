from src.json_saver import json_saver


class vacancy:
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
        Get list with vacancies dicts. This list with copy of class Vacancy
        :return: new lisrt with copy of class Vacancy
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