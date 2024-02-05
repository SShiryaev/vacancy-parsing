from abc import ABC, abstractmethod
import requests
import json


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
        :return: Возвращает список вакансий в формате json.
        """

        url = 'https://api.hh.ru/vacancies'
        response = requests.get(url, headers={'HH-User-Agent': 'pythonVacancyParsing/0.1.0 (shiryaev_fox@mail.ru)'},
                                params={'text': keyword})
        print(json.dumps(response.json(), indent=4))
        return response.json()


hh = HeadHunterAPI()
hh.get_vacancies('python')
