# Question 4: Library Management System (OOP) Create a Python program for a simple library 
# management system using object-oriented programming. The system should have classes for books,
# members, and a library. Books can be borrowed and returned by members.

# Example scenario:

# Books have attributes like title, author, and availability.
# Members have attributes like name, ID, and borrowed books.
# The library should have methods for adding books, adding members, borrowing books, and returning books.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Member:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def add_member(self, name, ID):
        member = Member(name, ID)
        self.members.append(member)

    def borrow_book(self, member_id, book_title):
        for member in self.members:
            if member.ID == member_id:
                for book in self.books:
                    if book.title == book_title and book.available:
                        book.available = False
                        member.borrowed_books.append(book)
                        print(f"{book.title} borrowed by {member.name}")
                        return
                print(f"Book '{book_title}' is not available")
                return
        print(f"Member with ID '{member_id}' not found")

    def return_book(self, member_id, book_title):
        for member in self.members:
            if member.ID == member_id:
                for book in member.borrowed_books:
                    if book.title == book_title:
                        book.available = True
                        member.borrowed_books.remove(book)
                        print(f"{book.title} returned by {member.name}")
                        return
                print(f"Book '{book_title}' not found in {member.name}'s borrowed list")
                return
        print(f"Member with ID '{member_id}' not found")

# Example usage
library = Library()

library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")

library.add_member("John Doe", 123)
library.add_member("Jane Smith", 456)

library.borrow_book(123, "The Great Gatsby")
library.borrow_book(456, "1984")

library.return_book(123, "The Great Gatsby")
library.return_book(456, "1984")
