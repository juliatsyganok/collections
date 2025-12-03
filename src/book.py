class Book:
    "Класс книги"
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self):
        return f"'{self.title}' - {self.author} ({self.year})"

    def __str__(self):
        return f"{self.title} {self.author}"