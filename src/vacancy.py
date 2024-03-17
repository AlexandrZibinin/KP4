
class Vacancy:

    def __init__(self, name, url, salary, snippet):
        self.name = name
        self.url = url
        self.salary_from = self.is_salary(salary)
        self.salary_to = self.is_salary(salary)
        self.snippet = snippet
    # @classmethod
    # def from_dict(cls, data):
    #     data = is_salary(data)
    #     return cls(**data)


    def is_salary(self, value):
        if value is None:
            return 'Значение не указано'
        else:
            return value
        return 0

    def __str__(self):
        return f'{self.name}, {self.url}, {self.salary_from}-{self.salary_to}, {self.snippet}'




