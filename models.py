import json
from typing import List

DATA_FILE = 'data.json'

# Модель для книг
class Book:
    def __init__ (
            self,
            id: int,
            title: str,
            author: str,
            year: int,
            status: str
        ):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
    

    """Превращает объект книги в словарь"""
    def to_dict (self) -> dict:
        return vars(self)
    

    """Создаёт объект книги из словаря"""
    @staticmethod
    def from_dict (data: dict) -> 'Book':
        return Book(**data)
    

# Модель для библиотеки
class Library:
    DATA_FILE = 'data.json'

    def __init__(self):
        self.books: List[Book] = self.load_books()
    
    def load_books(self) -> List[Book]:
        try:
            with open(self.DATA_FILE, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        except FileNotFoundError:
            return []
    
    def save_books(self):
        with open(self.DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)
