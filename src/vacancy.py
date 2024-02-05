class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, requirement: str, city: str):
        """
        :param name: название вакансии.
        :param url: ссылка на вакансию.
        :param salary_from: зарплата от.
        :param salary_to: зарплата до.
        :param requirement: описание вакансии.
        :param city: место работы.
        """

        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement
        self.city = city

    def __repr__(self) -> str:
        """
        :return: название вакансии.
        """

        return f'Вакансия: {self.name}'

    def __lt__(self, other) -> bool:
        """
        Позволяет сравнивать зарплату меньше или равно между экземплярами класса Vacancy.
        :param other: поле с зарплатой другого сравниваемого объекта класса Vacancy.
        :return: bool значение.
        """

        return self.salary_from <= other.salary_from

    def __ge__(self, other) -> bool:
        """
        Позволяет сравнивать зарплату больше или равно между экземплярами класса Vacancy.
        :param other: поле с зарплатой другого сравниваемого объекта класса Vacancy.
        :return: bool значение.
        """

        return self.salary_from >= other.salary_from

    def validate_data(self) -> None:
        """
        Валидация данных из json файла.
        :return: None.
        """

        if self.name is None:
            self.name = ''
        elif self.url is None:
            self.url = ''
        elif self.salary_from is None or self.salary_from == 'null':
            self.salary_from = 0
        elif self.salary_to is None or self.salary_from == 'null':
            self.salary_to = 0
        elif self.requirement is None:
            self.requirement = ''
        elif self.city is None:
            self.city = ''
