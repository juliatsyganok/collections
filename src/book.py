class LibraryItem:
    """Базовый класс"""
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    
    def __repr__(self):
        """Информация"""
        return f"{self.__class__.__name__}('{self.title}', '{self.author}', {self.year})"


class Book(LibraryItem):
    """Наследующий класс книга"""
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        super().__init__(title, author, year)
        self.genre = genre
        self.isbn = isbn
    
    def __repr__(self):
        return f"'{self.title}', '{self.author}', {self.year}, '{self.genre}', '{self.isbn}'"
    
class Journal(LibraryItem):
    """наследующий класс журнал"""
    def __init__(self, title: str, editor: str, year: int, issue: int, publisher: str):
        super().__init__(title, editor, year)
        self.issue = issue
        self.publisher = publisher
    
    def __repr__(self):
        return f"'{self.title}', '{self.author}', {self.year}, {self.issue}, '{self.publisher}'"