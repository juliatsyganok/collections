from list_book import BookCollection
class IndexDict():
    def __init__(self):
        self._by_isbn = {}
        self._by_author = {}
        self._by_year = {}
        self._by_genre = {}
    
    def __len__(self) -> int:
        return len(self._by_isbn)
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return self._by_isbn[key]
        elif isinstance(key, int):
            return self._by_year.get(key, [])
        else:
            raise KeyError("Неверный тип")
    
    def __iter__(self):
        return iter(self._by_isbn.values())
    
    def __contains__(self, isbn: str) -> bool:
        return isbn in self._by_isbn
    
    def __repr__(self):
        return f"Всего {len(self._by_isbn)} книг с индексом"
    
    def add_book(self, book):
        """добавление по разным ключам"""
        self._by_isbn[book.isbn] = book
        if book.author not in self._by_author:
            self._by_author[book.author] = []
        self._by_author[book.author].append(book)
        
        if book.year not in self._by_year:
            self._by_year[book.year] = []
        self._by_year[book.year].append(book)

        if book.genre not in self._by_genre:
            self._by_genre[book.genre] = []
        self._by_genre[book.genre].append(book)
    
    def remove_book(self, book):
        """удаление по раным ключам"""
        if book.isbn in self._by_isbn:
            del self._by_isbn[book.isbn]

        if book.author in self._by_author:
            self._by_author[book.author].remove(book)
            if not self._by_author[book.author]:
                del self._by_author[book.author]

        if book.year in self._by_year:
            self._by_year[book.year].remove(book)
            if not self._by_year[book.year]:
                del self._by_year[book.year]

        if book.genre in self._by_genre:
            self._by_genre[book.genre].remove(book)
            if not self._by_genre[book.genre]:
                del self._by_genre[book.genre]
    
    def find_by_author(self, author: str):
        """Поиск книг по автору"""
        books_list = self._by_author.get(author, [])
        result = BookCollection()
        for book in books_list:
            result.add_book(book)
        return result
        
    def find_by_year(self, year: int):
        """Поиск книг по году"""
        books_list = self._by_year.get(year, [])
        result = BookCollection()
        for book in books_list:
            result.add_book(book)
        return result
        
    def find_by_year(self, year: int):
        """Поиск книг по году"""
        books_list = self._by_year.get(year, [])
        result = BookCollection()
        for book in books_list:
            result.add_book(book)
        return result