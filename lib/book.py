#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def check_page_count(page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")

    page_count = "20"
    check_page_count(page_count)  # Prints "page_count must be an integer" since "20" is not an integer

    def turn_page():
        print("Flipping the page...wow, you read fast!")
        
    turn_page()

# Creating a new instance of the Book class
my_book = Book("Python Programming", 400)

# Accessing the attributes
print(my_book.title)       # Output: Python Programming
print(my_book.page_count)  # Output: 400


    
        