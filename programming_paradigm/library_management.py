
class Book:
    def __init__(self, title, author):
        self.title =  title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
        
class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        """Adding books to the lsit book to setup the collection"""
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Available books after setup: {book.title} by {book.author}")
        else:
            print("Invalid Object type. Only object with Book can be added")


    def check_out_book(self, title ):
        """Check out a book by title and know if its available"""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                print(f"Available books after checking out '1984': {book.title} by {book.author}")
                return
        print(f"Book '{title}' is not available or does not exist.")

    def return_book(self, title):
        """Return a book by a title and make it available"""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                print(f"Available books after returning '1984': {book.title} by {book.author}")
                return
        print("Available books not return")
            
    def list_available_books(self):
        """Prints a list of all available books."""
        available_books = [book for book in self._books if not book._is_checked_out]
        if not available_books:
            print("No books are currently available.")
            return
        print("Available Books:")
        for book in available_books:
            print(f"- '{book.title}' by {book.author}")