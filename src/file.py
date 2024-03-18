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
        """сохраняет результат в JSON файл"""
        with open('vacancy_json.json', 'w') as file:
            json.dump(value, file)

    def get_data(self):
        pass

    def del_data(self):
        """очистка файла JSON"""
        with open("vacancy_json.json", "w") as f:
            pass
