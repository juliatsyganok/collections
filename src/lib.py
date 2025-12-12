from list_book import BookCollection
from dict_book import IndexDict
class Library:
    def __init__(self):
        self.books = BookCollection()
        self.index = IndexDict()
    
    def __len__(self):
        return len(self.books)
    
    def __repr__(self):
        return f"Библиотека (книг: {len(self.books)})"
    
    def add_book(self, book):
        self.books.add_book(book)
        self.index.add_book(book)
        print(f"Добавлена: {book}")
    
    def remove_book(self, index: int):
        if 0 <= index < len(self.books):
            book = self.books[index]
            self.books.remove_book(index)
            self.index.remove_book(book)
            print(f"Удалена: {book}")
        else:
            raise IndexError("Неверный индекс")
    
    def remove_book_by_isbn(self, isbn: str):
        if isbn in self.index:
            book = self.index[isbn]
            for i, b in enumerate(self.books):
                if b.isbn == isbn:
                    self.books.remove_book(i)
                    break
            self.index.remove_book(book)
            print(f"Удалена по ISBN {isbn}: {book}")
        else:
            print(f"Книга с ISBN {isbn} не найдена")
    
    def find_by_author(self, author: str):
        books = self.index.find_by_author(author)
        print(f"Автор '{author}': {len(books)} книг")
        return books
    
    def find_by_year(self, year: int):
        books = self.index.find_by_year(year)
        print(f"Год {year}: {len(books)} книг")
        return books
    
    def find_by_genre(self, genre: str):
        books = self.index.find_by_genre(genre)
        print(f"Жанр '{genre}': {len(books)} книг")
        return books
    
    def get_book_by_isbn(self, isbn: str):
        if isbn in self.index:
            book = self.index[isbn]
            print(f"Найдена по ISBN {isbn}: {book}")
            return book
        print(f"Книга с ISBN {isbn} не найдена")
        return None