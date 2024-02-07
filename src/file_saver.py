import json
import os
from abc import ABC, abstractmethod


class MainSaver(ABC):
    """
    Абстрактный класс для работы с файлом.
    """

    @abstractmethod
    def add_vacancies(self, vacancies: list) -> None:
        """
        Абстрактный метод добавления вакансий в файл.
        :param vacancies: Список экземпляров класса Vacancy.
        :return: None.
        """

        pass

    @abstractmethod
    def get_vacancies(self, criterion: dict) -> list:
        """
        Абстрактный метод получения вакансий по критериям.
        :return: Список вакансий.
        """

        pass

    @abstractmethod
    def del_vacancies(self, vacancies: list) -> None:
        """
        Абстрактный метод удаления вакансий из списка.
        :param vacancies: Список экземпляров класса Vacancy.
        :return: None.
        """

        pass


class JSONSaver(MainSaver):
    """
    Класс для работы с json файлом.
    """

    def __init__(self, file_name: str):
        """
        :param file_name: Название json файла.
        """

        self.file_name = file_name

    def add_vacancies(self, vacancies: list) -> None:
        """
        Функция записи в json файл.
        :param vacancies: Список экземпляров класса Vacancy.
        :return: None
        """
        data = self.obj_list_to_json_list(vacancies)
        with open(os.path.join('data', self.file_name), 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))

    def get_vacancies(self, criterion: dict) -> str:
        """
        Абстрактный метод получения данных из файла по указанным критериям.
        :param criterion: Словарь с критериями.
        :return: Информация о вакансиях по критериям.
        """

        with open(os.path.join('data', self.file_name), 'r', encoding='utf-8') as file:
            data_for_filter = file.read()
        data = json.loads(data_for_filter)
        vacancies_list = []
        for vacancy in data:
            for key, value in criterion.items():
                if key == 'salary_input':
                    try:
                        int(vacancy['salary_from']) >= value
                    except TypeError:
                        continue
                    else:
                        vacancies_list.append(vacancy)
                else:
                    break
        for vac in vacancies_list:
            info_vacancy = (f'{vac['name']},\n'
                            f'{vac['city']},\n'
                            f'{vac['salary_from']},\n'
                            f'{vac['salary_to']},\n'
                            f'{vac['url']},\n'
                            f'{vac['requirement']},\n')
            return info_vacancy

    def del_vacancies(self, vacancies: list) -> None:
        """
        Абстрактный метод удаления вакансий из списка.
        :param vacancies: Список экземпляров класса Vacancy.
        :return: None.
        """

        with open(os.path.join('data', self.file_name), 'r', encoding='utf-8') as file:
            file_data = file.read()
            vacancies_list = json.loads(file_data)
        for vacancy in vacancies_list:
            if vacancy in vacancies:
                vacancies_list.remove(vacancy)
        with open(os.path.join('data', self.file_name), 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(vacancies_list, ensure_ascii=False, indent=4))

    @staticmethod
    def obj_list_to_json_list(vacancies: list) -> list:
        """
        Преобразует список экземпляров класса Vacancy в список словарей.
        :param vacancies: Список экземпляров класса Vacancy.
        :return: Список словарей с вакансиями.
        """

        vacancies_list = []
        for vacancy in vacancies:
            vacancy_dict = {
                'name': vacancy.name,
                'url': vacancy.url,
                'salary_from': vacancy.salary_from,
                'salary_to': vacancy.salary_to,
                'requirement': vacancy.requirement,
                'city': vacancy.city,
            }
            vacancies_list.append(vacancy_dict)
        return vacancies_list
