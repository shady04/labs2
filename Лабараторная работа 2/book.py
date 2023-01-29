BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовкаа к работе объекта "Книга"

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть целым числом")
        if id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Кол-во страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Кол-во страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
