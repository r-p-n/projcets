from booklist import BookList
from book import Book

# test empty BookList
book_list = BookList()
print(book_list)
assert len(book_list.books) == 0

# test loading books
book_list.load_books('books.csv')
print(book_list)
assert len(book_list.books) > 0  # assuming CSV file is not empty

# test sorting books

# test adding a new Book

# test saving books (check CSV file manually to see results)
