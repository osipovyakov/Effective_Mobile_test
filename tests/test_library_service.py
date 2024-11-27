import unittest
from models import Book, Library
from services import LibraryService

class TestLibraryService(unittest.TestCase):

    def setUp(self):
        """Инициализация тестовых данных"""
        self.library = Library()
        self.library.books = [
            Book(1, "Преступление и наказание", "Ф.М. Достоевский", 1866, "в наличии"),
            Book(2, "Война и мир", "Л.Н. Толстой", 1869, "выдана"),
        ]
        self.service = LibraryService(self.library)

    def test_add_book(self):
        """Тест добавления новой книги"""
        result = self.service.add_book("Мастер и Маргарита", "М.А. Булгаков", 1940)
        self.assertEqual(result, "Книга добавлена: Мастер и Маргарита")
        self.assertEqual(len(self.library.books), 3)
        self.assertEqual(self.library.books[-1].title, "Мастер и Маргарита")

    def test_delete_book(self):
        """Тест удаления книги"""
        result = self.service.delete_book(1)
        self.assertEqual(result, "Книга удалена: Преступление и наказание")
        self.assertEqual(len(self.library.books), 1)

    def test_delete_nonexistent_book(self):
        """Тест удаления несуществующей книги"""
        result = self.service.delete_book(999)
        self.assertEqual(result, "Ошибка: Книга с таким ID не найдена")

    def test_search_books(self):
        """Тест поиска книг по автору"""
        results = self.service.search_books("Л.Н. Толстой", "author")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Война и мир")

    def test_update_status(self):
        """Тест обновления статуса книги"""
        result = self.service.update_status(2, "в наличии")
        self.assertEqual(result, "Статус книги обновлён: Война и мир -> в наличии")
        self.assertEqual(self.library.books[1].status, "в наличии")

    def test_update_status_invalid(self):
        """Тест обновления статуса на некорректный"""
        result = self.service.update_status(2, "утеряна")
        self.assertEqual(result, "Ошибка: Неверный статус")

    def test_update_status_nonexistent_book(self):
        """Тест обновления статуса несуществующей книги"""
        result = self.service.update_status(999, "в наличии")
        self.assertEqual(result, "Ошибка: Книга с таким ID не найдена")

    def test_display_books(self):
        """Тест отображения всех книг"""
        results = self.service.display_books()
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["title"], "Преступление и наказание")

if __name__ == "__main__":
    unittest.main()
