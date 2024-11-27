from models import Library, Book
from typing import Union, List


class LibraryService:
    def __init__(self, library: Library):
        self.library = library
    
    """Добавляет новую книгу в библиотеку"""
    def add_book(self, title: str, author: str, year: int, status: str = "в наличии"):
        if title and author and year:
            new_id = max((book.id for book in self.library.books), default=0) + 1
            new_book = Book(new_id, title, author, year, status)
            self.library.books.append(new_book)
            self.library.save_books()
            return f"Книга добавлена: {new_book.title}"
        else:
            return f"Ошибка: Не все поля были заполнены"
    
    """Удаляет книгу по ID"""
    def delete_book(self, book_id: int) -> str:
        book = self.find_book_by_id(book_id)
        if book:
            self.library.books.remove(book)
            self.library.save_books()
            return f"Книга удалена: {book.title}"
        return "Ошибка: Книга с таким ID не найдена"
    
    """Ищет книги по указанному полю"""
    def search_books(self, query: Union[str, int], field: str) -> List[dict]:
        results = [book.to_dict() for book in self.library.books if str(getattr(book, field)).lower() == str(query).lower()]
        return results
    
    """Возвращает список всех книг"""
    def display_books(self) -> List[dict]:
        return [book.to_dict() for book in self.library.books]
    
    """Обновляет статус книги"""
    def update_status(self, book_id: int, status: str) -> str:
        book = self.find_book_by_id(book_id)
        if not book:
            return "Ошибка: Книга с таким ID не найдена"
        elif status not in ["в наличии", "выдана"]:
            return "Ошибка: Неверный статус"
        else:
            book.status = status
            self.library.save_books()
            return f"Статус книги обновлён: {book.title} -> {status}"
    
    """Ищет книгу по ID для удаления и обновления статуса"""
    def find_book_by_id(self, book_id: int) -> Union[Book, None]:
        return next((book for book in self.library.books if book.id == book_id), None)
    