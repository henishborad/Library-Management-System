class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book} to the library.")

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f" - {book}")
        else:
            print("No books available.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You have borrowed {book}.")
                return
        print(f"Sorry, the book '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available:
                book.is_available = True
                print(f"You have returned {book}.")
                return
        print(f"The book '{title}' was not borrowed from this library.")


# Create some book instances
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Create a library instance
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# List available books
library.list_available_books()

# Borrow a book
library.borrow_book("1984")
library.list_available_books()

# Return a book
library.return_book("1984")
library.list_available_books()
