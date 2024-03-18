import json
from abc import ABC, abstractmethod

class File(ABC):
    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass


class JSONsaver(File):

    def save_data(self, value):
        """сохраняет результату в JSON файл"""
        to_json = {'result': value}
        with open('vacancy_json.json', mode='w') as file:
            json.dump(to_json)
        return file

    def get_data(self):
        pass

    def del_data(self):
        pass

