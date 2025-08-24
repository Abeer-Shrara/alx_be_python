# library_management.py

class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        """Mark the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # book was not checked out

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages multiple books."""
    
    def __init__(self):
        self._books = []  # private list to store Book objects

    def add_book(self, book):
        """Add a book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
        else:
            for book in available:
                print(f"{book.title} by {book.author}")
