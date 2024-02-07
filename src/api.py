from abc import ABC, abstractmethod

import requests


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
                                params={'text': keyword, 'per_page': 100})
        return response.json()
