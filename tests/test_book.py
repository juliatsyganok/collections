import sys
import pytest 
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from book import Book, Journal

import pytest
from book import LibraryItem, Book, Journal

def test_libraryitem():
    i = LibraryItem("Книга", "Автор", 2020)
    assert i.title == "Книга"
    assert i.author == "Автор"
    assert i.year == 2020

def test_book():
    b = Book("Роман", "Писатель", 1999, "Художественный", "123")
    assert b.title == "Роман"
    assert b.genre == "Художественный"
    assert b.isbn == "123"

def test_journal():
    j = Journal("Наука", "Редактор", 2023, 5, "Издатель")
    assert j.title == "Наука"
    assert j.issue == 5
    assert j.publisher == "Издатель"

def test_repr():
    b = Book("Тест", "Автор", 2000, "Жанр", "456")
    r = repr(b)
    assert "Тест" in r
    assert "456" in r

def test_inheritance():
    b = Book("К", "А", 2020, "Ж", "111")
    assert isinstance(b, LibraryItem)