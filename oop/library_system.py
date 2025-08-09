
# A Simple Library system Program

#Base Class Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
# SubClass Ebook
class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File size: {self.file_size}KB"
# Subclass PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page count: {self.page_count}"
# Composition Class Library
class Library:
    def __init__(self, books):
        self.books = []
    
    def add_book(self,book):
       self.books.append(book)
    def list_books(self):
        for book in self.books:
            print(book)
