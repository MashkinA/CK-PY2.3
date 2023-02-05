class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name  # защищенный атрибут
        self._author = author  # защищенный атрибут

    @property
    def name(self) -> str:
        """Получаем название книги."""
        return self._name

    @name.setter
    def name(self, name) -> None:
        """Меняем название книги."""
        if not isinstance(name, str):  # Проверка
            raise TypeError('Название книги должно быть строкой')
        self._name = name

    @property
    def author(self) -> str:
        """Получаем автора книги."""
        return self._author

    @author.setter
    def author(self, author) -> None:
        """Меняем автора книги."""
        if not isinstance(author, str):  # Проверка
            raise TypeError('Имя автора должно быть стокой')
        self._author = author

    def __str__(self):  # Используем наследование
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):  # В данном случае не используем наследование, а заново задаем метод
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):  # Используем наследование от Book
    """Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        """Получаем число страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Меняем число страниц в книге."""
        if not isinstance(pages, int):  # Проверка
            raise TypeError('Число страниц должно быть целочисленным')
        if pages <= 0:
            raise ValueError('Число страниц должно быть правильным')
        self._pages = pages

    def __repr__(self):  # В данном случае не используем наследование, а заново задаем метод
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):  # Используем наследование от Book
    """Аудио книга"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """Получаем длительность аудио книги."""
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """Меняем длительность аудио книги."""
        if not isinstance(duration, float):  # Проверка
            raise TypeError('Продолжительность книги должна быть вещественным числом')
        if duration <= 0:
            raise ValueError('Продолжительность книги должна быть правильной')
        self._duration = duration

    def __repr__(self):  # В данном случае не используем наследование, а заново задаем метод
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
