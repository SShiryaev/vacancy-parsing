class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, data):
        """
        :param data: объект response.
        """

        self.name = None
        self.url = None
        self.salary_from = None
        self.salary_to = None
        self.requirement = None
        self.city = None
        self.get_params(data)

    def __repr__(self) -> str:
        """
        :return: Атрибуты класса Vacancy.
        """

        return (f'Вакансия: {self.name},\n'
                f'Город: {self.city},\n'
                f'Зарплата от: {self.salary_from},\n'
                f'Зарплата до: {self.salary_to},\n'
                f'Ссылка на вакансию: {self.url},\n'
                f'Описание: {self.requirement}\n'
                f'-------------------------------\n')

    def __lt__(self, other) -> bool:
        """
        Позволяет сравнивать зарплату меньше или равно между экземплярами класса Vacancy.
        :param other: Поле с зарплатой другого сравниваемого объекта класса Vacancy.
        :return: Bool значение.
        """

        return self.salary_from <= other.salary_from

    def __ge__(self, other) -> bool:
        """
        Позволяет сравнивать зарплату больше или равно между экземплярами класса Vacancy.
        :param other: Поле с зарплатой другого сравниваемого объекта класса Vacancy.
        :return: Bool значение.
        """

        return self.salary_from >= other.salary_from

    def get_params(self, data) -> None:
        """
        Получение атрибутов класса Vacancy из объекта response.
        """

        if data['name']:
            self.name = data['name']
        else:
            self.name = 'Без названия'

        if data['alternate_url']:
            self.url = data['alternate_url']
        else:
            self.url = 'Без ссылки'

        if data['salary']:
            if data['salary']['from'] and data['salary']['from'] != 'null':
                self.salary_from = data['salary']['from']
            else:
                self.salary_from = 0
            if data['salary']['to'] and data['salary']['to'] != 'null':
                self.salary_to = data['salary']['to']
            else:
                self.salary_to = 0
        else:
            self.salary_from = 0
            self.salary_to = 0

        if data['snippet'] and data['snippet']['requirement']:
            self.requirement = data['snippet']['requirement']
        else:
            self.requirement = 'Без описания'

        if data['address'] and data['address']['city']:
            self.city = data['address']['city']
        else:
            self.city = 'Без города'

    @staticmethod
    def cast_to_object_list(vacancies: dict) -> list:
        """
        Статический метод для записи экземпляров класса Vacancy в список.
        :param vacancies: Объект response.
        :return: Список вакансий.
        """

        vacancies_list = []
        for vacancy in vacancies['items']:
            vac = Vacancy(vacancy)
            vacancies_list.append(vac)
        return vacancies_list
