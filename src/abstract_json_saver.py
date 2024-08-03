from abc import ABC, abstractmethod


class abstract_json_saver(ABC):

    @abstractmethod
    def save_file(self, data: list):
        pass

    @abstractmethod
    def read_file(self):
        pass