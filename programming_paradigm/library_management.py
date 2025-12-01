class Book(): 

    def __init__(self, title, author):
        self.title = title 
        self.author = author   
        self.__is_checked_out = False
    
    def __str__(self):
        return f"{self.title} {self.author}"

class Library:

    def __init__(self):
        self.__books = []
    
    def add_book(self, new_book): 
        self.__books.append(new_book)


    def list_available_books(self): 
        for books in self.__books:
            print(books)
        
    
    
    def check_out_book(self, title,
                       ):

        for book in self.__books:
            if book.title == title:
                book.is_checked_out = True
                return  book.is_checked_out
        return None

    #def return_book(title():


if __name__ == "__main__":
    library = Library()
    book = Book(title="Things Fall Apart", author="Chinu Achebe")
    library.add_book(book)
    print(library.check_out_book(title="Things Fall Apart"))
    print(library.list_available_books())