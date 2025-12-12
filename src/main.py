import random
from book import Book
from list_book import BookCollection
from dict_book import IndexDict
from lib import Library

def run(steps=20, seed=None):
    if seed is not None:
        random.seed(seed)
    
    lib = Library()
    kn = [
        Book("Война и мир", "Толстой", 1869, "Роман", "111"),
        Book("Анна Каренина", "Толстой", 1877, "Роман", "112"),
        Book("Преступление", "Достоевский", 1866, "Роман", "222"),
        Book("Идиот", "Достоевский", 1869, "Роман", "223"),
        Book("Мастер", "Булгаков", 1967, "Роман", "333")
    ]
    
    for book in kn:
        lib.add_book(book)
    
    print(f"Начало: {len(lib.books)} книг")
    def e1():
        print("Добавить книгу")
        new = Book("Новая", "Автор", 2020, "Жанр", str(random.randint(500, 999)))
        lib.add_book(new)
    
    def e2():
        if len(lib.books) > 0:
            print("Удалить книгу")
            if lib.index._by_isbn:
                isbn = random.choice(list(lib.index._by_isbn.keys()))
                lib.remove_book_by_isbn(isbn)
        else:
            print("Нет книг для удаления")
    
    def e3():
        print("Поиск по автору")
        a = random.choice(["Толстой", "Достоевский", "Булгаков"])
        r = lib.find_by_author(a)
        if r:
            print(f"Найдено: {len(r)} книг")
    
    def e4():
        print("Поиск по году")
        g = random.choice([1869, 1866, 1967])
        r = lib.find_by_year(g)
        if r:
            print(f"Найдено: {len(r)} книг")
    
    def e5():
        print("Поиск по ISBN")
        if lib.index._by_isbn:
            isbn = random.choice(list(lib.index._by_isbn.keys()))
            b = lib.get_book_by_isbn(isbn)
            if b:
                print(f"Найдена: {b.title}")
        else:
            print("Нет книг")
    
    def e6():
        print("Попытка найти несуществующую книгу")
        lib.get_book_by_isbn("000")
    
    def e7():
        print("Статистика")
        print(f"Всего книг: {len(lib.books)}")
        if lib.index._by_isbn:
            print(f"Авторов: {len(lib.index._by_author)}")
    
    es = [e1, e2, e3, e4, e5, e6, e7]
    
    for s in range(steps):
        print(f"\nШаг {s+1}/{steps}")
        print("-"*20)
        random.choice(es)()

def main():
    print("Симуляция библиотеки")
    print("1. Запуск (20 шагов)")
    print("2. Свой seed")
    print("3. Выйти")
    
    c = input("> ")
    
    if c == "1":
        run()
    elif c == "2":
        try:
            seed = int(input("Seed: "))
            run(seed=seed)
        except:
            print("Ошибка seed")
    elif c == "3":
        return
    else:
        print("Неправильный выбор")

if __name__ == "__main__":
    main()