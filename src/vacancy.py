class Vacancy:

    def __init__(self, name, url, salary, snippet):
        self.name = name
        self.url = url
        self.salary = self.is_salary(salary)
        self.snippet = snippet

    @classmethod
    def from_dict(cls, data):
        """создание экземпляра класса"""
        return cls(**data)

    @staticmethod
    def get_obj_lst(data):
        """метод создает список экземпляров класса с вакансиями"""
        vacancy_ex = []
        for value in data:
            vac_data = {
                'name': value.get('name'), 'url': value.get('url'), 'salary': value.get('salary'),
                'snippet': value.get('snippet')
            }
            vacancy_ex.append(Vacancy.from_dict(vac_data))
        return vacancy_ex

    @staticmethod
    def is_salary(value):
        """метод валидации salary"""
        if value is None:
            return 'Значение не указано'
        else:
            return (f'{value.get('from', 0) if value.get('from') is not None else "Неизвестно"} - '
                    f'{value.get('to') if value.get('to') is not None else "Неизвестно"}')

    def __str__(self):
        return (f'Название вакансии: {self.name}, '
                f'Ссылка: {self.url}, '
                f'Зарплата: {self.salary}, '
                f'Описание:{self.snippet.get('requirement', 'responsibility')}')

    def __lt__(self, other):
        """метод сравнения зарплат"""
        max_salary = max(int(self.salary.split(' ')))
        return max_salary < other
