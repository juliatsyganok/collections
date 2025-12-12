import sys
import pytest 
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from book import Book
from dict_book import IndexDict

class TestIndexDict:
    def test_empty(self):
        i = IndexDict()
        assert len(i) == 0

    def test_add(self):
        i = IndexDict()
        b = Book("Книга", "Автор", 2020, "Жанр", "100")
        i.add_book(b)
        assert len(i) == 1
        assert "100" in i

    def test_find_author(self):
        i = IndexDict()
        b1 = Book("К1", "Автор", 2020, "Ж", "101")
        b2 = Book("К2", "Автор", 2021, "Ж", "102")
        i.add_book(b1)
        i.add_book(b2)
        r = i.find_by_author("Автор")
        assert len(r) == 2

    def test_remove(self):
        i = IndexDict()
        b = Book("К", "А", 2020, "Ж", "103")
        i.add_book(b)
        i.remove_book(b)
        assert len(i) == 0

    def test_find_year(self):
        i = IndexDict()
        b = Book("К", "А", 2022, "Ж", "104")
        i.add_book(b)
        r = i.find_by_year(2022)
        assert len(r) == 1