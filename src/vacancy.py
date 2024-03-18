class Vacancy:

    def __init__(self, name, url, salary, snippet, **kwargs):
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
            return f'{value['from']} - {value['to']}'

    def __str__(self):
        return f'{self.name}, {self.url}, {self.salary}, {self.snippet}'


