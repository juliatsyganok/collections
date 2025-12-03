from list_book import BookCollection
from dict_book import IndexDict

class Library:
    "Класс библиотеки"
    def __init__(self):
        self.books = BookCollection()
        self.index = IndexDict()
    
    def __len__(self):
        return len(self.books)
    
    def __repr__(self):
        return f"Library({len(self.books)} books)"
    
    def add_book(self, book):
        """Добавить книгу в библиотеку"""
        self.books.add_book(book)
        self.index.add_book(book)
        print(f"Добавлена книга: {book}")
    
    def remove_book(self, index: int):
        """Удалить книгу по индексу из коллекции"""
        if 0 <= index < len(self.books):
            book_to_remove = self.books[index]
            self.books.remove_book(index)
            self.index.remove_book(book_to_remove)
            print(f"Удалена книга: {book_to_remove}")
        else:
            print("Неверный индекс для удаления")
    
    def remove_book_by_isbn(self, isbn: str):
        """Удалить книгу по ISBN"""
        if isbn in self.index:
            book_to_remove = self.index[isbn]
            for i, book in enumerate(self.books):
                if book.isbn == isbn:
                    self.books.remove_book(i)
                    break
            self.index.remove_book(book_to_remove)
            print(f"Удалена по ISBN {isbn}: {book_to_remove}")
        else:
            print(f"Книга с ISBN {isbn} не найдена")
    
    def find_by_author(self, author: str):
        """Поиск книг по автору"""
        books = self.index.find_by_author(author)
        print(f"По автору '{author}': найдено {len(books)} книг")
        for book in books:
            print(f"   - {book}")
        return books
    
    def find_by_year(self, year: int):
        """Поиск книг по году"""
        books = self.index.find_by_year(year)
        print(f"Поиск по году {year}: найдено {len(books)} книг")
        for book in books:
            print(f"   - {book}")
        return books
    
    def find_by_genre(self, genre: str):
        """Поиск книг по жанру"""
        books = self.index.find_by_genre(genre)
        print(f"По жанру '{genre}': найдено {len(books)} книг")
        for book in books:
            print(f"{book}")
        return books
    
    def get_book_by_isbn(self, isbn: str):
        """Получить книгу по ISBN"""
        try:
            book = self.index[isbn]
            print(f"Найдена по ISBN {isbn}: {book}")
            return book
        except KeyError:
            print(f"нига с ISBN {isbn} не найдена")
            return None
    
    def display_stats(self):
        print(f"Всего: {len(self.books)}")
        print(f"Проиндексировано: {len(self.index)}")
        
        # Статистика по авторам
        authors = list(self.index._by_author.keys())
        print(f"Количество авторов: {len(authors)}")
        
        # Статистика по годам
        years = list(self.index._by_year.keys())
        print(f"Годы публикаций: {sorted(years)}")
        
        # Статистика по жанрам
        genres = list(self.index._by_genre.keys())
        print(f"Жанры: {genres}")