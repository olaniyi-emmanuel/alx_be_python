class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title:str, author: str, file_size: int):
        super().__init__(title,author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} with {self.file_size} bytes"

class PrintBook(Book):

    def __init__(self, title:str, author:str, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"{self.title} by {self.author} with total pages of {self.page_count}"


class Library:
    books = []
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Cannot add a book that is not a book, EBook or PrintBook")

    def list_books(self):
        for book in self.books:
            if isinstance(book, Book):
                print(f"This is a book with the title {book.title}")
            elif isinstance(book, EBook):
                print(f"This is an ebook with the title {book.title}")
            elif isinstance(book, PrintBook):
                print(f"This is an printbook with the title {book.title}")
            else:
                print("This is not a book")


