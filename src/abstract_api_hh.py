from abc import ABC, abstractmethod


class abstract_get_api_hh(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_vacancy_from_api(self, name_vacancy):
        pass