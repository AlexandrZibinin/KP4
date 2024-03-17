import json
from abc import ABC, abstractmethod
import requests


class Connect(ABC):
    """абстрактный класс для работы с API HH.ru"""

    @abstractmethod
    def get_vacancy(self):
        """абстрактный метод для получения вакансий"""
        pass

    @abstractmethod
    def get_params(self, keyword):
        """абстрактный метод для подготовки параметров"""
        pass


class HeadHunterAPI(Connect):
    """класс для работы с API HH.ru"""
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'

    def get_params(self, keyword):
        """метод для подготовки параметров для обращения к сервису
        :param :keyword значение для поиска в полях вакансии
        """
        params = {
            'page': 0,
            'per_page': 10,
            'text': keyword

        }
        return params

    def get_vacancy(self):
        """Получение списка вакансий с hh.ru - список словарей"""
        params = self.get_params(keyword=input('Введите название вакансии\n'))
        response = requests.get(self.__url, params).json()['items']
        result = []
        for value in response:
            result.append(value)
        return result


