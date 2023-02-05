class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def autor(self) -> str:
        return self._autor

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

        @property
        def pages(self) -> int:
            return self._pages

        @pages.setter
        def pages(self, pages_selected: int) -> None:
            if not isinstance(pages_selected, int):
                raise TypeError ("Кол-во страниц должно иметь тип данных int")
            if pages_selected <= 0:
                raise TypeError("Кол-во страниц должно быть положительным числом")
            self._pages = pages_selected

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super ().__innit__(name, author)
        self.duration = duration

        @property
        def duration(self) -> float:
            return self._duration

        @duration.setter
        def duration(self, duration_selected: float) -> None:
            if not isinstance(duration_selected, float):
                raise TypeError("Продолжительность должна иметь тип данных float")
            if duration_selected <= 0:
                raise TypeError("Продолжительность должна быть положительным числом")
            self._duration = duration_selected

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.duration!r})"
