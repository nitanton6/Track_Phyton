import doctest
from typing import Union, Optional

# TODO Написать 3 класса с документацией и аннотацией типов
class Book:
    """
    Класс, представляющий книгу.
    Атрибуты:
        title (str): Название книги
        pages (int): Количество страниц
        author (str): Автор книги
    """

    def __init__(self, title: str, pages: int, author: str):
        """
        Создание и подготовка к работе объекта "Книга"
        :param title: Название книги
        :param pages: Количество страниц
        :param author: Автор книги
        Примеры:
        >>> book = Book("Война и мир", 1225, "Лев Толстой")
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if len(title.strip()) == 0:
            raise ValueError("Название книги не может быть пустым")
        self.title = title.strip()

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if len(author.strip()) == 0:
            raise ValueError("Автор книги не может быть пустым")
        self.author = author.strip()

    def get_reading_time(self, pages_per_hour: int = 30) -> float:
        """
        Расчет примерного времени чтения книги.
        :param pages_per_hour: Количество страниц, читаемых в час (по умолчанию 30)
        :return: Время чтения в часах
        Примеры:
        >>> book = Book("Война и мир", 1225, "Лев Толстой")
        >>> book.get_reading_time(30)
        """
        if not isinstance(pages_per_hour, int):
            raise TypeError("Скорость чтения должна быть целым числом")
        if pages_per_hour <= 0:
            raise ValueError("Скорость чтения должна быть положительным числом")
        ...

    def get_summary(self, max_length: int = 500) -> str:
        """
        Получение краткого описания книги.
        :param max_length: Максимальная длина описания в символах
        :return: Краткое описание книги
        Примеры:
        >>> book = Book("Война и мир", 1225, "Лев Толстой")
        >>> book.get_summary(200)
        """
class Smartphone:
    """
    Класс, представляющий смартфон.
    Атрибуты:
        brand (str): Бренд смартфона
        battery_capacity (int): Емкость аккумулятора в мАч
        ram (int): Объем оперативной памяти в ГБ
    """

    def __init__(self, brand: str, battery_capacity: int, ram: int):
        """
        Создание и подготовка к работе объекта "Смартфон"
        :param brand: Бренд смартфона
        :param battery_capacity: Емкость аккумулятора в мАч
        :param ram: Объем оперативной памяти в ГБ
        Примеры:
        >>> phone = Smartphone("Samsung", 5000, 8)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if len(brand.strip()) == 0:
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand.strip()

        if not isinstance(battery_capacity, int):
            raise TypeError("Емкость аккумулятора должна быть целым числом")
        if battery_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительным числом")
        self.battery_capacity = battery_capacity

        if not isinstance(ram, int):
            raise TypeError("Объем оперативной памяти должен быть целым числом")
        if ram <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным числом")
        self.ram = ram

    def estimate_battery_life(self, screen_time_hours: float) -> Optional[float]:
        """
        Оценка времени работы от аккумулятора.
        :param screen_time_hours: Среднее время работы экрана в часах в день
        :return: Примерное количество дней работы от одного заряда или None если расчет невозможен
        Примеры:
        >>> phone = Smartphone("Samsung", 5000, 8)
        >>> phone.estimate_battery_life(6.5)
        """
        if not isinstance(screen_time_hours, (int, float)):
            raise TypeError("Время работы экрана должно быть числом")
        if screen_time_hours <= 0:
            raise ValueError("Время работы экрана должно быть положительным числом")
        ...

    def can_run_app(self, app_ram_requirements: int, current_usage: int = 0) -> bool:
        """
        Проверка возможности запуска приложения.
        :param app_ram_requirements: Требования приложения к оперативной памяти в ГБ
        :param current_usage: Текущее использование оперативной памяти в ГБ
        :return: Может ли приложение быть запущено
        Примеры:
        >>> phone = Smartphone("Samsung", 5000, 8)
        >>> phone.can_run_app(4, 2)
        """
        if not isinstance(app_ram_requirements, int):
            raise TypeError("Требования к оперативной памяти должны быть целым числом")
        if app_ram_requirements <= 0:
            raise ValueError("Требования к оперативной памяти должны быть положительным числом")
        ...

class SocialNetwork:
    """
    Класс, представляющий социальную сеть.
    Атрибуты:
        name (str): Название социальной сети
        users_count (int): Количество пользователей
        year_founded (int): Год основания
    """
    def __init__(self, name: str, users_count: int, year_founded: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"
        :param name: Название социальной сети
        :param users_count: Количество пользователей
        :param year_founded: Год основания
        Примеры:
        >>> network = SocialNetwork("Facebook", 2_800_000_000, 2004)
        """
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть строкой")
        if len(name.strip()) == 0:
            raise ValueError("Название социальной сети не может быть пустым")
        self.name = name.strip()

        if not isinstance(users_count, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self.users_count = users_count

        if not isinstance(year_founded, int):
            raise TypeError("Год основания должен быть целым числом")
        if year_founded < 1990 or year_founded > 2026:  # реалистичный диапазон
            raise ValueError("Год основания должен быть реалистичным")
        self.year_founded = year_founded


    def calculate_growth_rate(self, previous_year_users: int) -> float:
        """
        Расчет темпов роста пользовательской базы.
        :param previous_year_users: Количество пользователей в предыдущем году
        :return: Темп роста в процентах
        Примеры:
        >>> network = SocialNetwork("Facebook", 2_800_000_000, 2004)
        >>> network.calculate_growth_rate(2_500_000_000)
        """
        if not isinstance(previous_year_users, int):
            raise TypeError("Количество пользователей в прошлом году должно быть целым числом")
        if previous_year_users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        ...

    def estimate_ad_revenue(self, arpu: float) -> float:
        """
        Оценка дохода от рекламы.
        :param arpu: Средний доход с одного пользователя (ARPU)
        :return: Общий ожидаемый доход от рекламы
        Примеры:
        >>> network = SocialNetwork("Facebook", 2_800_000_000, 2004)
        >>> network.estimate_ad_revenue(30.5)
        """
        if not isinstance(arpu, (int, float)):
            raise TypeError("ARPU должен быть числом")
        if arpu < 0:
            raise ValueError("ARPU не может быть отрицательным")
        ...



if __name__ == "__main__":
    doctest.testmod(verbose=True)
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
