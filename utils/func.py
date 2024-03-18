from src.headhunterapi import HeadHunterAPI
from  src.vacancy import Vacancy
from src.file import JSONsaver

def user_interface():
    vacancies = HeadHunterAPI().get_vacancy() #создаем список словарей с вакансиями
    return vacancies
#

vacancy_lst = user_interface()
vacancy_ex = []
for value in vacancy_lst:
    vacancy_ex.append(Vacancy.from_dict(value))

# for val in vacancy_ex:
#     print(val)

JSONsaver.save_data(vacancy_ex)
# from_hh = user_interface()
# for i in from_hh:
#     print(i)

# vacancies = []
# for value in from_hh:
#     res = Vacancy(value)
#     vacancies.append(res)
#
# print(vacancies)