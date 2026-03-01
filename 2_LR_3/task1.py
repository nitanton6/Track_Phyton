class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        """Название книги (только для чтения)."""
        return self.name

    @property
    def author(self):
        """Автор книги (только для чтения)."""
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    @property
    def pages(self):
        """Количество страниц (целое положительное число)."""
        return self.pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
            raise ValueError("Количество страниц должно быть целым положительным числом")
        self.pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    @property
    def duration(self):
        """Длительность в часах (положительное число)."""
        return self.duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self.duration = float(value)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"