class Book:

    def __init__(self, title="", author="", pages=0, book_type="r"):
        self.title = title.title()
        self.author = author.title()
        self.pages = pages
        self.book_type = book_type.lower()

    def __str__(self):
        return "{} by {}, {} pages".format(self.title, self.author, self.pages)

    def is_long(self):
        return int(self.pages) >= 500

    def mark_complete(self):
        self.book_type = "c"
