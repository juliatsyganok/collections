import random 

class BookCollection:
    def __init__(self):
        self._books = []
    
    def __len__(self) -> int:
        return len(self._books)
    
    def __iter__(self):
        return iter(self._books)
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            new_collection = BookCollection()
            new_collection._books = self._books[key]
            return new_collection
        else:
            return self._books[key]
    
    def __contains__(self, book) -> bool:
        return book in self._books
    
    def __repr__(self):
        return f"BookCollection({len(self._books)} books)"
    
    def add_book(self, book):
        """Добавление книги в коллекцию"""
        self._books.append(book)
    
    def remove_book(self, index: int):
        """Удаление книги по индексу"""
        if 0 <= index < len(self._books):
            del self._books[index]
        else:
            raise IndexError("Индекс вне диапазона")
    
    def get_random_book(self):
        """Получить случайную книгу"""
        if len(self._books) == 0:
            raise ValueError("Коллекция пуста")
        return random.choice(self._books)


