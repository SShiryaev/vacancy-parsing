from abc import ABC, abstractmethod

import requests

from src.vacancy import Vacancy


class MainAPI(ABC):
    """
    Абстрактный класс для работы с API.
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        """
        Получает список вакансий в формате json.
        """

        pass


class HeadHunterAPI(MainAPI):
    """
    Класс для работы с API hh.ru.
    """

    def get_vacancies(self, keyword: str):
        """
        Производит get запрос на сайт hh.ru.
        :url: Ссылка на запрашиваемый объект.
        :param keyword: Ключевое слово по вакансиям.
        :return: Возвращает объект response.
        """

        url = 'https://api.hh.ru/vacancies'
        response = requests.get(url, headers={'HH-User-Agent': 'vacancy-parsing/0.1.0 (shiryaev_fox@mail.ru)'},
                                params={'text': keyword})
        return response.json()


hh = HeadHunterAPI()
vacancies = hh.get_vacancies('python')
for vacancy in vacancies['items']:
    print(vacancy)
    vac = Vacancy(vacancy)
    print(vac)
    print(vac.city)
    print(vac.url)
    print(vac.requirement)
    print(vac.salary_from)
    print(vac.salary_to)
