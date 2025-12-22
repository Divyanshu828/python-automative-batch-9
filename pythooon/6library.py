class Library:
    def __init__(self, library_name):
        self.library_name = library_name   # property
        self.books = []                    # property (list of books)

    # behavior: add a book
    def add_book(self, book_name):
        self.books.append(book_name)
        print(book_name, "added to the library")

    # behavior: remove a book
    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(book_name, "removed from the library")
        else:
            print(book_name, "not found")

    # behavior: display books
    def show_books(self):
        if not self.books:
            print("No books available")
        else:
            print("Books in", self.library_name)
            for book in self.books:
                print("-", book)


lib = Library("Central Library")

lib.add_book("Harry Potter")
lib.add_book("Lord of the Rings")
lib.show_books()

lib.remove_book("Lord of the Rings")
lib.show_books()
