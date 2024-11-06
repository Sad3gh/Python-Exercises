class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


    def info(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []        #A list to hold multiple Book instances

    def add_book(self,book):
        self.books.append(book)   #Add a Book instance to library

    def show_books(self):
        print("your books:\n")
        for book in self.books:
            print(book.info())    #Call the info method of each book in the list of our Book instances

    def input_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        new_book = Book(title,author)
        self.add_book(new_book)


my_library = Library()  #Create a Library instance

while True:
    my_library.input_book() #Get book details from user
    more = input("Do you want to add another book? (yes/no): ")
    if more.lower() != 'yes':
        break
my_library.show_books()  #Display all the books in the library
