from abc import ABC, abstractmethod
import requests


class MainAPI(ABC):
    """
    Абстрактный класс для работы с API.
    """

    @abstractmethod
    def get_vacancies(self):
        """
        Получает список вакансий в формате json.
        """

        pass


class HeadHunterAPI(MainAPI):
    """
    Класс для работы с API hh.ru.
    """

    def __init__(self, keyword: str):
        """
        :param keyword: ключевое слово по которому будут отобраны вакансии.
        """

        self.keyword = keyword

    def get_vacancies(self):
        """
        Производит get запрос на сайт hh.ru.
        :return: Возвращает список вакансий в формате json.
        """

        url = 'https://api.hh.ru/vacancies'
        response = requests.get(url, headers={'HH-User-Agent': 'pythonVacancyParsing/0.1.0 (shiryaev_fox@mail.ru)'},
                                params={'text': self.keyword})
        return response.json()
