from models import Library
from services import LibraryService


def start_ui():
    library = Library()
    service = LibraryService(library)

    while True:
        print("\nДоступные команды:\nadd - Добавить книгу\n"
                "delete - Удалить книгу\nsearch - Поиск\n"
                "display - Показать список книг\n"
                "update - Изменить статус книги\n"
                "exit - Выход"
            )
        command = input("Введите команду: ").strip().lower()

        if command == "add":
            title = input("Название книги: ").strip()
            author = input("Автор книги: ").strip()
            year = int(input("Год издания: ").strip())
            print(service.add_book(title, author, year))

        elif command == "delete":
            book_id = int(input("ID книги для удаления: ").strip())
            print(service.delete_book(book_id))

        elif command == "search":
            field = input("Искать по (title, author, year): ").strip().lower()
            query = input("Запрос: ").strip()
            results = service.search_books(query, field)
            if results:
                for book in results:
                    print(book)
            else:
                print("Книг по запросу не найдено")

        elif command == "display":
            books = service.display_books()
            if books:
                for book in books:
                    print(book)
            else:
                print("Библиотека пуста")

        elif command == "update":
            book_id = int(input("ID книги: ").strip())
            status = input("Новый статус (в наличии/выдана): ").strip()
            print(service.update_status(book_id, status))

        elif command == "exit":
            print("Завершение работы")
            break

        else:
            print("Неизвестная команда")
