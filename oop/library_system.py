class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title:str, author: str, file_size: int):
        super().__init__(title,author)
        self.file_size = file_size

class PrintBook(Book):

        def __init__(self, title:str, author:str, page_count:int):
            super().__init__(title, author)


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
            return book
        return None