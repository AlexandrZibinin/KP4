from src.headhunterapi import HeadHunterAPI
from  src.vacancy import Vacancy
from src.file import JSONsaver

def user_interface():
    keyword = input('Введите название вакансии\n')
    vacancies = HeadHunterAPI().get_vacancy(keyword) #создаем список словарей с вакансиями
    return vacancies

vacancy_lst = user_interface()
count_vacancies = input('Введите количество вакансий: ')
salary_range = input("Введите диапазон зарплат: ")
vacancy_ex = []
for value in vacancy_lst:
    vac_data = {
        'name': value.get('name'), 'url': value.get('url'), 'salary': value.get('salary'), 'snippet': value.get('snippet')
    }
    vacancy_ex.append(Vacancy.from_dict(vac_data))

for val in vacancy_ex:
    print(val)

saver = JSONsaver()
saver.save_data(vacancy_lst)
saver.del_data()
