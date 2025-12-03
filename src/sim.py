import random 
from book import Book
from lib import Library
SAMPLE_BOOKS = [
    Book("Война и мир", "Лев Толстой", 1869, "Роман-эпопея", "111-111"),
    Book("Анна Каренина", "Лев Толстой", 1877, "Роман", "111-112"),
    Book("Преступление и наказание", "Федор Достоевский", 1866, "Роман", "222-222"),
    Book("Идиот", "Федор Достоевский", 1869, "Роман", "222-223"),
    Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", "333-333"),
    Book("Собачье сердце", "Михаил Булгаков", 1925, "Повесть", "333-334"),
    Book("Евгений Онегин", "Александр Пушкин", 1833, "Роман в стихах", "444-444"),
    Book("Герой нашего времени", "Михаил Лермонтов", 1840, "Роман", "555-555"),
    Book("Отцы и дети", "Иван Тургенев", 1862, "Роман", "666-666"),
    Book("Мертвые души", "Николай Гоголь", 1842, "Поэма", "777-777"),
]

def event_add_new_book(library):
    """Событие: добавление новой случайной книги"""
    template_book = random.choice(SAMPLE_BOOKS)
    new_isbn = f"ISBN-{random.randint(100000, 999999)}"
    new_book = Book(
        title=template_book.title,
        author=template_book.author,
        year=template_book.year,
        genre=template_book.genre,
        isbn=new_isbn
    )
    library.add_book(new_book)

def event_remove_random_book(library):
    """Событие: удаление случайной книги"""
    if len(library.books) > 0:
        try:
            random_isbn = library.index.get_random_isbn()
            library.remove_book_by_isbn(random_isbn)
        except ValueError:
            print("Ошибка удаления")
    else:
        print("Ошибка удаления")

def event_search_by_author(library):
    """Событие: поиск книг по случайному автору"""
    authors = ["Лев Толстой", "Федор Достоевский", "Михаил Булгаков", 
               "Александр Пушкин", "Михаил Лермонтов", "Иван Тургенев"]
    author = random.choice(authors)
    library.find_by_author(author)

def event_search_by_year(library):
    """Событие: поиск книг по случайному году"""
    years = [1869, 1866, 1967, 1833, 1840, 1862, 1842]
    year = random.choice(years)
    library.find_by_year(year)

def event_search_by_genre(library):
    """Событие: поиск книг по случайному жанру"""
    genres = ["Роман", "Роман-эпопея", "Повесть", "Роман в стихах", "Поэма"]
    genre = random.choice(genres)
    library.find_by_genre(genre)

def event_try_find_nonexistent_book(library):
    """Событие: попытка найти несуществующую книгу"""
    fake_isbn = "000-000-000"
    print(f"🔎 Попытка найти книгу с несуществующим ISBN: {fake_isbn}")
    library.get_book_by_isbn(fake_isbn)

def event_display_library_stats(library):
    """Событие: отображение статистики библиотеки"""
    library.display_stats()

def event_update_index(library):
    """Событие: сообщение об обновлении индекса"""
    print(f" - Проиндексировано: {len(library.index)}")
    print(f" - Уникальных авторов: {len(library.index._by_author)}")
    print(f" - Лет издания: {len(library.index._by_year)}")

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """
    Запуск псевдослучайной симуляции библиотеки
    
    Args:
        steps: Количество шагов симуляции
        seed: Seed для генератора случайных чисел
    """
    print("🚀 ЗАПУСК СИМУЛЯЦИИ БИБЛИОТЕКИ")
    print("=" * 50)
    
    if seed is not None:
        random.seed(seed)
        print(f"📊 Seed установлен: {seed}")
    
    library = Library()
    
    events = [
        event_add_new_book,
        event_remove_random_book,
        event_search_by_author,
        event_search_by_year,
        event_search_by_genre,
        event_try_find_nonexistent_book,
        event_display_library_stats,
        event_update_index
    ]

    for step in range(steps):
        print(f"\n🎯 ШАГ {step + 1}/{steps}")
        print("-" * 30)

        event = random.choice(events)
        event(library)
    library.display_stats()
