class Library:
    def __init__(self, book_name, author_name, book_date):
        self.book = book_name
        self.author = author_name
        self.date = book_date
        self.books = [book_name]  # Add initial book to the list
    
    def new_book(self, new_book):
        self.books.append(new_book)
        return f'"{new_book}" added.'

    def del_book(self, del_book):
        if del_book in self.books:
            self.books.remove(del_book)
            return f'"{del_book}" removed.'
        else:
            return f'"{del_book}" not found in collection.'

# Create instance
lib1 = Library("Harry Potter", "Salman", "10/12/2020")

# Add new books
print(lib1.new_book("The Lord of the Rings"))

# Remove a book
print(lib1.del_book("Harry Potter"))

# View current books
print("Books in library:", lib1.books)

# Print author of the original book
print("Author:", lib1.author)
