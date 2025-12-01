class Book:

    def __init__(self, title, author):
        self.title = title 
        self.author = author   
        self.__is_checked_out = False
    
    def __str__(self):
        return f"{self.title} {self.author}"

    def return_book(self):   #

        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def is_available(self) -> bool:
        """Check if the book is available to be checked out."""
        return not self.__is_checked_out


class Library:

    def __init__(self):
        self.__books = []
    
    def add_book(self, new_book): 
        self.__books.append(new_book)


    def list_available_books(self): 
        for books in self.__books:
            print(books)








if __name__ == "__main__":
    library = Library()
    book = Book(title="Things Fall Apart", author="Chinu Achebe")
    library.add_book(book)
    print(library.check_out_book(title="Things Fall Apart"))
    print(library.list_available_books())