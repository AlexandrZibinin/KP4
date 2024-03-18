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

    def get_params(self, keyword, count_vacancies, salary):
        """метод для подготовки параметров для обращения к сервису
        :param :keyword значение для поиска в полях вакансии
        """
        params = {
            'page': 0,
            'per_page': count_vacancies,
            'text': keyword,
            'salary': salary

        }
        return params

    def get_vacancy(self, keyword, count_vacancies, salary):
        """Получение списка вакансий с hh.ru - список словарей"""
        params = self.get_params(keyword, count_vacancies, salary)
        response = requests.get(self.__url, params).json()
        vacancies = response['items']
        return vacancies
