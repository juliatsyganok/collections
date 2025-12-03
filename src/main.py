from sim import run_simulation, SAMPLE_BOOKS
from lib import Library
if __name__ == "__main__":
    run_simulation(steps=15, seed=42)
    demo_library = Library()
    demo_library.add_book(SAMPLE_BOOKS[0])
    demo_library.add_book(SAMPLE_BOOKS[1])
    demo_library.add_book(SAMPLE_BOOKS[2])
    print(f"Количество книг: {len(demo_library.books)}")
    print(f"Первая книга: {demo_library.books[0]}")
    print(f"Все книги в коллекции:")
    for i, book in enumerate(demo_library.books):
        print(f"  {i+1}. {book}")
    
    tolstoy_books = demo_library.find_by_author("Лев Толстой")
    print(f"Найдено книг Толстого: {len(tolstoy_books)}")

    first_two_books = demo_library.books[0:2]
    print(f"Первые две книги: {first_two_books}")