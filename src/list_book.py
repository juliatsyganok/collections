class BookCollection:
    def __init__(self):
        self._books = []
    
    def __len__(self) -> int:
        return len(self._books)
    
    def __iter__(self):
        return iter(self._books)
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            new_col = BookCollection()
            new_col._books = self._books[key]
            return new_col
        else:
            return self._books[key]
    
    def __contains__(self, book) -> bool:
        return book in self._books
    
    def __repr__(self):
        return f"Всего {len(self._books)} книг"
    
    def add_book(self, book):
        """Добавление книги в коллекцию"""
        self._books.append(book)
    
    def remove_book(self, index: int):
        """Удаление книги по индексу"""
        if 0 <= index < len(self._books):
            del self._books[index]
        else:
            raise IndexError("Ошибка индекса")

