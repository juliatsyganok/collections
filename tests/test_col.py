import sys
import pytest 
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from book import Book
from list_book import BookCollection

class TestBookCollection:
    def test_empty(self):
        c = BookCollection()
        assert len(c) == 0

    def test_add(self):
        c = BookCollection()
        b = Book("Книга", "Автор", 2000, "Жанр", "1")
        c.add_book(b)
        assert len(c) == 1
        assert c[0] == b

    def test_iter(self):
        c = BookCollection()
        b1 = Book("К1", "А", 2000, "Ж", "3")
        b2 = Book("К2", "А", 2001, "Ж", "4")
        c.add_book(b1)
        c.add_book(b2)
        books = list(c)
        assert len(books) == 2

    def test_slice(self):
        c = BookCollection()
        for i in range(5):
            c.add_book(Book(f"К{i}", "А", 2000+i, "Ж", str(i)))
        s = c[1:3]
        assert len(s) == 2