import sys
import pytest 
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from book import Book
from lib import Library

class TestLibrary:
    def test_create(self):
        l = Library()
        assert len(l) == 0

    def test_add(self):
        l = Library()
        b = Book("Книга", "Автор", 2020, "Жанр", "200")
        l.add_book(b)
        assert len(l) == 1
        assert "200" in l.index

    def test_remove(self):
        l = Library()
        b = Book("К", "А", 2020, "Ж", "201")
        l.add_book(b)
        l.remove_book_by_isbn("201")
        assert len(l) == 0

    def test_find(self):
        l = Library()
        b = Book("Книга", "Иванов", 2021, "Роман", "202")
        l.add_book(b)
        r = l.find_by_author("Иванов")
        assert len(r) == 1

    def test_get(self):
        l = Library()
        b = Book("К", "А", 2020, "Ж", "203")
        l.add_book(b)
        g = l.get_book_by_isbn("203")
        assert g == b