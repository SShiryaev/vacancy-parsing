import json
from abc import ABC, abstractmethod


class MainSaver(ABC):
    """
    Абстрактный класс для работы с файлом.
    """

    @abstractmethod
    def add_vacancies_to_file(self, vacancies: list) -> None:
        """
        Абстрактный метод добавления вакансий в файл.
        :param vacancies: Список объектов класса Vacancy.
        :return: None.
        """

        pass

    @abstractmethod
    def get_vacancies_by_criteria(self) -> list:
        """
        Абстрактный метод получения вакансий по критериям.
        :return: Список вакансий.
        """

        pass

    @abstractmethod
    def del_vacancies(self, vacancies: list) -> None:
        """
        Абстрактный метод удаления вакансий из списка.
        :param vacancies: Список объектов класса Vacancy.
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

    def add_vacancies_to_file(self, vacancies: list) -> None:
        """
        Функция записи в json файл.
        :param vacancies: Список объектов класса Vacancy.
        :return: None
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

        with open(self.file_name, 'w', encoding='utf-8') as file:
            file.write(json.dumps(vacancies_list, ensure_ascii=False, indent=4))

    def get_vacancies_by_criteria(self):
        """
        Абстрактный метод получения данных из файла по указанным критериям.
        """

        pass

    def del_vacancies(self, vacancies: list) -> None:
        """
        Абстрактный метод удаления вакансий из списка.
        :param vacancies: Список объектов класса Vacancy.
        :return: None.
        """

        with open(self.file_name, 'r', encoding='utf-8') as file:
            file_data = file.read()
            vacancies_list = json.loads(file_data)
        for vacancy in vacancies_list:
            if vacancy in vacancies:
                vacancies_list.remove(vacancy)
        with open(self.file_name, 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(vacancies_list, ensure_ascii=False, indent=4))
