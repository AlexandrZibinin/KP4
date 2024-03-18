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
    def is_salary(value):
        """метод валидации salary"""
        if value is None:
            return 'Значение не указано'
        else:
            return f'{value.get('from', 0) if value.get('from') is not None else "Неизвестно"} - {value.get('to') if value.get('to') is not None else "Неизвестно"}'

    def __str__(self):
        return f'{self.name}, {self.url}, {self.salary}, {self.snippet}'

    def __lt__(self, other):
        # self.salary
        """split('-') int, проверка значений, """




