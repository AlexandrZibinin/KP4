from src.headhunterapi import HeadHunterAPI
from src.vacancy import Vacancy
from src.file import JSONsaver


def user_interface():
    keyword = input('Введите название вакансии или ключевое слово: ')
    count_vacancies = input('Введите количество вакансий: ')
    salary_range = input("Введите желаемую зарплату: ")
    vacancies = HeadHunterAPI().get_vacancy(keyword, count_vacancies, salary_range)  # создаем список словарей с
    # вакансиями

    # sort_vacancies = input('Произвести сортировку вакансий? да/нет ')
    # if sort_vacancies.lower() == 'да':
    #     vacancies = sorted(vacancies, key=lambda x: x['salary'], reverse=True)

    vacancy_lst_obj = Vacancy.get_obj_lst(vacancies)  # создаем список объектов вакансии
    for value in vacancy_lst_obj:
        print(value, end='\n')

    saver = JSONsaver()
    saver.save_data(vacancies)

    return f'Данные сохранены в файл vacancy_json.json'


user_interface()
