from src.api import HeadHunterAPI
from src.vacancy import Vacancy
from src.file_saver import JSONSaver

hh = HeadHunterAPI()
json_saver = JSONSaver('json_vacancies.json')


def get_vacancies_by_city(vacancies_list: list, user_input: str) -> list:
    """
    Сортировка вакансий по городу.
    :param vacancies_list: Список экземпляров класса Vacancy.
    :param user_input: Название города.
    :return: Список вакансий отсортированных по городу.
    """

    vacancies_by_city_list = []
    for vacancy in vacancies_list:
        if vacancy.city == user_input.capitalize().strip():
            vacancies_by_city_list.append(vacancy)

    if not vacancies_by_city_list:
        print('Вакансий по этому городу не найдено.')
    else:
        return vacancies_by_city_list


def get_top_vacancies(vacancies_list: list, user_input: int) -> list:
    """
    Сортировка указанного количества вакансий по зарплате.
    :param vacancies_list: Список экземпляров класса Vacancy.
    :param user_input: Количество вакансий.
    :return: Список вакансий отсортированных по зарплате.
    """

    sorted_vacancies = sorted(vacancies_list, key=lambda elem: elem.salary_from, reverse=True)[:user_input]
    return sorted_vacancies


def get_vacancies_by_salary(vacancies_list: list) -> None:
    """
    Функция сортирующая вакансии по выбору действий пользователя.
    :param vacancies_list: Список экземпляров класса Vacancy.
    :return: None
    """

    print('Выберете действие:\n'
          '1 - Получить топ-N вакансий по зарплате\n'
          '2 - Получить вакансии от заданной суммы\n'
          '0 - Выйти'
          )
    while True:
        user_input = input()
        if user_input in ('1', '2', '0'):
            if user_input == '1':
                thirst_input = int(input('Введите количество вакансий для вывода: '))
                top_n = get_top_vacancies(vacancies_list, thirst_input)
                try:
                    for vacancy in top_n:
                        print(vacancy)
                except TypeError:
                    continue
                break
            elif user_input == '2':
                second_input = int(input('Введите минимальную зарплату: '))
                min_salary = json_saver.get_vacancies({'salary_input': second_input})
                for vac in min_salary:
                    print(vac)
                break
            elif user_input == '0':
                break
        else:
            print('Некорректный запрос. Попробуйте еще раз')


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем. Функция взаимодействует с пользователем через консоль
    :return: None
    """

    search_query = input('Введите поисковый запрос по вакансиям: ')
    hh_vacancies = hh.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    json_saver.add_vacancies(vacancies_list)
    while True:
        user_input = input('Выберите действие:\n'
                           '1 - Отфильтровать вакансии по городу\n'
                           '2 - Отфильтровать вакансии по зарплате\n'
                           '3 - Вывести все найденные.\n'
                           '4 - Редактор файла.\n'
                           '0 - Выйти.\n'
                           )
        if user_input in ('1', '2', '3', '4', '0'):
            if user_input == '1':
                user_input_city = input('Введите название города: ')
                print(get_vacancies_by_city(vacancies_list, user_input_city))

            elif user_input == '2':
                get_vacancies_by_salary(vacancies_list)

            elif user_input == '3':
                print(vacancies_list)

            elif user_input == '4':
                user_input_file = input('Выберите действие:\n'
                                        '1 - Очистить файл.\n')
                if user_input_file == '1':
                    json_saver.del_vacancies(vacancies_list)
                else:
                    print('Некорректный запрос. Попробуйте еще.')
            elif user_input == '0':
                break
        else:
            print('Некорректный запрос. Попробуйте еще.')


if __name__ == '__main__':
    user_interaction()
