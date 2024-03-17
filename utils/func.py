from src.headhunterapi import HeadHunterAPI
from  src.vacancy import Vacancy

def user_interface():
    vacancies = HeadHunterAPI().get_vacancy() #создаем список словарей с вакансиями
    return vacancies
#

# print(user_interface())
data = user_interface()
print(type(data))
# vacancies = []
# for value in data:
#     vacancies.append(Vacancy(**value))
#
# vac = Vacancy(**data)
# print(vac)