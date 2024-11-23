class Book:
    def __init__(self, title, author, isbn):
        """
            initialize a new book with title,author,ISBN and availability
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = True  # set the availability as True(available)

    def check_out(self):
        """ Mark the book as checked out. """
        self.availability = False

    def check_in(self):
        """ Mark the book as available. """
        self.availability = True

    def __str__(self):
        """ Returns a string representation of the book """
        status = "Available" if self.availability else "Checked out"
        return f"{self.title} by {self.author} ({status})"


class Patron:
    def __init__(self, name, patron_id):
        """
            Initialize a new patron with name,ID and list of borrowed books
        """
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """ Allow the patron to borrow a book if it's available """
        if book.availability:
            self.borrowed_books.append(book)
            book.check_out()  # Mark the book as checked out.
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"{book.title} is currently not available")

    def return_book(self, book):
        """ Allow the patron to return the borrowed book """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.check_in()  # Mark the book as available.
            print(f"{self.name} has returned {book.title}")
        else:
            print(f"{self.name} doesn't have {book.title}")

    def __str__(self):
        """ Return a string presentation of the patron """
        return f"{self.name} (ID : {self.patron_id})"


class Library:
    """
        Initialize a new library with a list of books and patrons
    """

    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        """ Add a new book to the library """
        self.books.append(book)
        print(f"Added book: {book}")

    def register_patron(self,patron):
        """ Register a new patron in the library """
        self.patrons.append(patron)
        print(f"Registered patron: {patron}")

    def find_book(self,title):
        """ Find a book by its title """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book     # The book is found.
        return "Book not found."   # Return not found message.

    def find_patron(self,name):
        """ Find a patron by their name """
        for patron in self.patrons:
            if patron.name.lower() == name.lower():
                return patron      # The patron is found.
        return "Patron no found."  # Return not found message.

    def display_books(self):
        """ Display all the books in the library """
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library: ")
            for book in self.books:
                print(book)  # Calling the __str__ method of the book

    def display_patrons(self):
        """ Display all the patrons in the library """
        if not self.patrons:
            print("No patrons in the library")
        else:
            print("patrons in the library:")
            for patron in self.patrons:
                print(patron)  # Calling the __str__ method of the patron


def main():
    """ Main function to run the library management system """
    library = Library()    # Creating an instance of the Library class
    while True:
        # Displaying menu options to the user
        print("\nWelcome to the Library Management System!")
        print("1. Add Book")
        print("2. Register Patron")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Patrons")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()
        if choice == '1':  # Add Book
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)  # Create a new Book instance
            library.add_book(book)  # Add the book to the library

        elif choice == '2':  # Register Patron
            name = input("Enter patron name: ")
            patron_id = input("Enter patron ID: ")
            patron = Patron(name, patron_id)  # Create a new Patron instance
            library.register_patron(patron)  # Register the patron

        elif choice == '3':  # Borrow Book
            patron_id = input("Enter patron ID: ")
            patron = library.find_patron(patron_id)  # Find the patron
            if isinstance(patron, Patron):  # Check if the patron was found
                title = input("Enter book title to borrow: ")
                book = library.find_book(title)  # Find the book
                if isinstance(book, Book):  # Check if the book was found
                    patron.borrow_book(book)  # Borrow the book

        elif choice == '4':  # Return Book
            patron_id = input("Enter patron ID: ")
            patron = library.find_patron(patron_id)  # Find the patron
            if isinstance(patron, Patron):  # Check if the patron was found
                title = input("Enter book title to return: ")
                book = library.find_book(title)  # Find the book
                if isinstance(book, Book):  # Check if the book was found
                    patron.return_book(book)  # Return the book

        elif choice == '5':  # Display Books
            library.display_books()  # Show all books in the library

        elif choice == '6':  # Display Patrons
            library.display_patrons()  # Show all registered patrons

        elif choice == '7':  # Exit
            print("Goodbye!")  # Exit message
            break  # Break the loop to exit

        else:
            print("Invalid option. Please choose a number between 1 and 7.")


# Start the application
if __name__ == "__main__":
    main()
