from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button, Label
from book import Book
from booklist import BookList


class ReadingListApp(App):
    BOOK_FILE = "books.csv"
    # file of books
    LONG_COLOUR = (0, 1, 1, 1)
    # colour for books 500 pages or over
    SHORT_COLOUR = (1, 1, 0, 1)
    # colour for books under 500 pages

    def __init__(self):
        super(ReadingListApp, self).__init__()
        self.book_list = BookList()
        self.top_status_bar = Label(id="top_status_bar", text="total pages", size_hint_y=None, height=50)
        self.bottom_status_bar = Label(id="bottom_status_bar", text="click books to mark them as complete",
                                       size_hint_y=None, height=50)

    def build(self):
        self.title = "Reading List 2.0"
        self.root = Builder.load_file("app.kv")
        self.book_list.load_books(self.BOOK_FILE)
        self.create_buttons("r")
        # creates buttons for required books
        return self.root

    def create_buttons(self, book_type):
        self.get_list_type(book_type)
        # changes what menu widget is highlighted and what the status bars say depending on the type of book chosen
        self.clear_buttons()
        self.book_list.sort_books()
        self.root.ids.books.add_widget(self.top_status_bar)
        if self.book_list.is_empty(book_type) == 0:
            empty_label = Label()
            self.root.ids.books.add_widget(empty_label)
            # creates a filler label if there aren't any books that match the chosen type
        self.create_book_buttons(book_type)
        self.root.ids.books.add_widget(self.bottom_status_bar)

    def add_book(self, title, author, pages):
        valid = 0
        while valid == 0:
            if self.root.ids.title_input.text == "" or self.root.ids.author_input.text == "" \
                    or self.root.ids.pages_input.text == "":
                self.bottom_status_bar.text = "All fields must be complete"
                break
            try:
                book = Book(title, author, int(pages))
            except ValueError:
                self.bottom_status_bar.text = "Please enter a valid number"
                break
            if book.pages < 0:
                self.bottom_status_bar.text = "Pages must be >= 0"
                break
            else:
                self.bottom_status_bar.text = "{} {}".format(str(book), "was added")
                self.book_list.add_book(Book(self.root.ids.title_input.text, self.root.ids.author_input.text,
                                             self.root.ids.pages_input.text))
                valid = 1
                self.clear_buttons()
                self.create_buttons("r")
                self.clear_text()

    def clear_buttons(self):
        self.root.ids.books.clear_widgets()

    def clear_text(self):
        self.root.ids.title_input.text = ""
        self.root.ids.author_input.text = ""
        self.root.ids.pages_input.text = ""

    def completed_button_information(self, instance):
        book = self.book_list.get_book_from_title(instance.text)
        self.bottom_status_bar.text = "{} {}".format(book, "(completed)")

    def create_book_buttons(self, book_type):
        for book in self.book_list.books:
            if book.book_type == book_type:
                # splits up required and completed books
                temp_button = Button(text=str(book.title))
                if book.book_type == "r":
                    temp_button.bind(on_release=self.mark_completed)
                    if book.is_long():
                        temp_button.background_color = self.LONG_COLOUR
                    else:
                        temp_button.background_color = self.SHORT_COLOUR
                # buttons for required books
                else:
                    temp_button.bind(on_release=self.completed_button_information)
                self.root.ids.books.add_widget(temp_button)
                # buttons for completed books

    def get_list_type(self, book_type):
        if book_type == "r":
            self.top_status_bar.text = "{}{}".format("Total pages to read: ", self.book_list.get_required_pages())
            self.bottom_status_bar.text = "Click books to mark them as completed"
            self.root.ids.list_required.state = "down"
            self.root.ids.list_complete.state = "normal"
        else:
            self.top_status_bar.text = "{}{}".format("Total pages completed: ", self.book_list.get_completed_pages())
            self.bottom_status_bar.text = "Click books to view details"
            self.root.ids.list_complete.state = "down"
            self.root.ids.list_required.state = "normal"

    def mark_completed(self, button):
        book = self.book_list.get_book_from_title(button.text)
        Book.mark_complete(book)
        self.create_buttons("r")
        self.bottom_status_bar.text = "{}{}".format("Completed: ", str(book))

    def on_stop(self):
        self.book_list.save_books(self.BOOK_FILE)

ReadingListApp().run()
