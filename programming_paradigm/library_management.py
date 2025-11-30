class Book(): 

    def __init__(self, title, author):
        self.title = title 
        self.author = author   
        self.__is_checked_out = False
    
    def __str__(self):
        return (f"{self.title} {self.author}")


class Library():

    def __init__(self):
        self.__books = []
    
    def add_book(self, new_book): 
        self.__books.append(new_book)

    def display_books(self): 
        for books in self.__books:
            print(books)
        
    
    
    #def check_out_book(title):

        
book = Book(title="Things Fall Apart", author="Chinu Achebe")
library = Library()
library.add_book(book)

library.display_books()