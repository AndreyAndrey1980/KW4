import json
import os
from abc import ABC, abstractmethod
from config import DATA
from src.vacancy import Vacancies, Vacancy


class BaseSaver(ABC):
    """Базовый класс для записи и чтения полученных вакансий в файл json"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def write_to_file(self, vacs: Vacancies):
        pass

    @abstractmethod
    def read_from_file(self):
        pass


class JSONSaver(Vacancies, BaseSaver):
    """Запись и чтение json - файла"""

    def __init__(self, filename: str):
        super().__init__()
        self.__filename = filename
        self.__check_path_or_create()
        self.__filepath = os.path.join(DATA, self.__filename)

    @staticmethod
    def __check_path_or_create() -> None:
        """Проверяет, существует ли папка, если нет то создает."""
        if not os.path.isdir(DATA):
            os.makedirs(DATA)

    def write_to_file(self, vacs: Vacancies):
        """Сохраняет список вакансий в json-файл."""
        with open(self.__filepath, "w", encoding="utf-8") as file:
            # if isinstance(vacs, Vacancies):
            json.dump(vacs.to_list_dict(), file, indent=4, ensure_ascii=False)
            # else:
            #     print('Не удалось записать данные в файл')

    def read_from_file(self):
        """Загружает список вакансий из json-файла."""
        with open(self.__filepath, "r", encoding="UTF-8") as file:
            list_dict = json.load(file)
            self.__all_vacancies = []
            for vac in list_dict:
                self.__all_vacancies.append(Vacancy.to_list(vac))
