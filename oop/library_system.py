
# A Simple Library system Program

#Base Class Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# SubClass Ebook
class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
# Subclass PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
# Composition Class Library
class Library:
    def __init__(self, books):
        self.books = []
    
    def add_book(self,book):
       self.books.append(book)
       if isinstance(book,EBook):
           print(f"EBook: {book.title} by {book.author}, File size: {book.file_size}KB")
           return
       elif isinstance(book, PrintBook):
            print(f"PrintBook: {book.title} by {book.author}, Page count: {book.page_count}")
            return
       elif isinstance(book, Book):
           print(f"Book: {book.title} by {book.author}")
           return
       else:
           print("Please enter a Book, Ebook or a PrintBook")
            
    def list_books(self):
        for book in self.books:
            print(book)
