from abc import ABC, abstractmethod


class BaseVacancy(ABC):
    """Базовый класс для вакансии"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass


class BaseVacancies(ABC):
    """Базовый класс для списка вакансий"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_vacancy(self, new_vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vac_id: int):
        pass


class Vacancy(BaseVacancy):
    """Класс для работы с вакансией"""

    def __init__(
        self,
        vac_id: int,
        name: str,
        city: str,
        salary_from: float,
        salary_to: float,
        currency: str,
        employment: str,
        url: str,
    ):
        self.id = vac_id
        self.name: str = name
        self.city: str = city
        self.salary_from: float = salary_from
        self.salary_to: float = salary_to
        self.currency = currency
        self.employment: str = employment
        self.url: str = url

    def __str__(self) -> str:
        return (
            f"id: {self.id}\n"
            f"Название вакансии: {self.name}\n"
            f"Город: {self.city}\n"
            f"Зарплата\nот: {self.salary_from} {self.currency}\nдо: {self.salary_to} {self.currency}\n"
            f"Тип занятости: {self.employment}\n"
            f"Ссылка на вакансию: {self.url}\n"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией!")
        return (self.salary_from, self.salary_to) == (other.salary_from, other.salary_to)

    def __ne__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией!")
        return (self.salary_from, self.salary_to) != (other.salary_from, other.salary_to)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией!")
        return (self.salary_from, self.salary_to) < (other.salary_from, other.salary_to)

    def __gt__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией!")
        return (self.salary_from, self.salary_to) > (other.salary_from, other.salary_to)

    def to_dict(self):
        """Возвращает вакансию в виде словаря"""
        return self.__dict__

    @staticmethod
    def to_list(vacancy_dict):
        """Возвращает вакансию в виде списка"""
        return Vacancy(
            vacancy_dict["vacancy_title"],
            vacancy_dict["town"],
            vacancy_dict["salary_from"],
            vacancy_dict["salary_to"],
            vacancy_dict["currency"],
            vacancy_dict["employment"],
            vacancy_dict["url"],
        )


class Vacancies(BaseVacancies):
    """Класс для работы со списком вакансий"""

    def __init__(self):
        self.__all_vacancies = []
        self.cursor = 0

    def __len__(self):
        return len(self.all_vacancies)

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor >= len(self.__all_vacancies):
            raise StopIteration
        else:
            result = self.__all_vacancies[self.cursor]
            self.cursor += 1
            return result

    def __getitem__(self, index):
        return self.__all_vacancies[index]

    def __str__(self):
        str_vac = ""
        if len(self.__all_vacancies) > 0:
            for vac in self.all_vacancies:
                str_vac += str(vac)
        return str_vac

    def get_top_n_vacancy(self, top_n: int):
        """Принимает число, возвращает список top-n вакансий."""
        if len(self.__all_vacancies) <= top_n:
            return self.__all_vacancies
        top_n_vacs = Vacancies()
        self.sort_vacancies_by_salary()
        for vac in self.__all_vacancies[:top_n]:
            top_n_vacs.add_vacancy(vac)

        return top_n_vacs

    def add_vacancy(self, new_vacancy):
        """Добавляет вакансию к списку вакансий."""
        if isinstance(new_vacancy, Vacancy):
            self.__all_vacancies.append(new_vacancy)
        else:
            raise TypeError("Можно добавить только экземпляр класса Vacancy")

    def delete_vacancy(self, vac_id: int):
        """Удаляет вакансию из списка вакансий."""
        new_vacancies = Vacancies()
        for vac in self.__all_vacancies:
            v = vac.to_dict()["id"]
            if v.isdigit():
                v = int(v)
            else:
                return self.all_vacancies
            if v != vac_id:
                new_vacancies.add_vacancy(vac)
        self.__all_vacancies = new_vacancies
        return self.all_vacancies

    def sort_vacancies_by_salary(self):
        """Сортирует список вакансий по убыванию ЗП."""
        self.__all_vacancies = sorted(self.__all_vacancies, reverse=True)

    @property
    def all_vacancies(self):
        """Возвращает список вакансий."""
        return self.__all_vacancies

    def to_list_dict(self):
        """Возвращает список словарей с вакансиями."""
        my_list = []
        for vac in self.__all_vacancies:
            my_list.append(vac.to_dict())
        return my_list

    def filtered_by_city(self, city: str):
        """Принимает название города, возвращает список вакансий в этом городе."""
        by_city = Vacancies()
        for vac in self.__all_vacancies:
            if vac.to_dict()["city"].lower() == city:
                by_city.add_vacancy(vac)
        self.__all_vacancies = by_city
        return self.__all_vacancies

    def filtered_by_salary(self, salary_from: int):
        """Принимает начальный размер ЗП, возвращает список вакансий ЗП в которых больше либо равны указанной сумме."""
        by_salary = Vacancies()
        for vac in self.__all_vacancies:
            salary = vac.to_dict()["salary_from"]
            if isinstance(salary, int) and (salary >= salary_from):
                by_salary.add_vacancy(vac)
        self.__all_vacancies = by_salary
        return self.__all_vacancies
