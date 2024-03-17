from src.headhunterapi import HeadHunterAPI
from  src.vacancy import Vacancy

def user_interface():
    vacancies = HeadHunterAPI().get_vacancy() #создаем список словарей с вакансиями
    return vacancies
#

print(user_interface())
# from_hh = user_interface()
# for i in from_hh:
#     print(i)

# vacancies = []
# for value in from_hh:
#     res = Vacancy(value)
#     vacancies.append(res)
#
# print(vacancies)