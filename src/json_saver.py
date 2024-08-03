import json

from config import DATA
from src.abstract_json_saver import abstract_json_saver


class json_saver(abstract_json_saver):

    def save_file(self, data: list):
        """Save file"""
        with open(DATA, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))

    def read_file(self):
        """Read file"""
        with open(DATA, encoding='utf-8') as file:
            return json.load(file)

    def add_vacancy_to_file(self, data: list):
        old_list = self.read_file()
        new_list = data + old_list
        self.save_file(new_list)

    def delete_vacancy(self, vacancy: str):
        new_list = []

        old_list = self.read_file()

        for params in old_list:
            if params['name'] != vacancy:
                new_list.append(params)

        self.save_file(new_list)