from book_class import Book

def main():
    # creating instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # demonstrating the __str__ method
    print(my_book)

    # demonstrating the __str__ method
    print(repr(my_book))

    # deleting a book instance to treger __del__
    del my_book

if __name__ == "__main__":
    main()
