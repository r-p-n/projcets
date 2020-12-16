from book import Book
from operator import attrgetter


class BookList:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book_from_title(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                return book

    def get_completed_pages(self):
        completed_pages = 0
        for book in self.books:
            if book.book_type == "c":
                completed_pages += int(book.pages)
        return str(completed_pages)

    def get_required_pages(self):
        required_pages = 0
        for book in self.books:
            if book.book_type == "r":
                required_pages += int(book.pages)
        return str(required_pages)

    def is_empty(self, book_type):
        book_count = 0
        for book in self.books:
            if book.book_type == book_type:
                book_count += 1
        return book_count

    def load_books(self, file):
        with open(file) as book_file:
            for line in book_file:
                parts = line.strip().split(",")
                self.add_book(Book(parts[0], parts[1], parts[2], parts[3]))

    def save_books(self, file):
        with open(file, "w") as book_file:
            for book in self.books:
                line = "{},{},{},{}{}".format(book.title, book.author, book.pages, book.book_type, "\n")
                book_file.write(line)

    def sort_books(self):
        self.books.sort(key=attrgetter("author"))
