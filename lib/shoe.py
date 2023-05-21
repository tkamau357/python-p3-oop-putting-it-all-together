#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def set_values(self, brand, size):
        self.brand = brand
        self.size = size

    def get_brand(self):
        return self.brand

    def get_size(self):
        return self.size
    
    def print_size_error(size):
        if not isinstance(size, int):
            print("size must be an integer")

    print_size_error(10)
    print_size_error("not an integer")

    
    def __init__(self, name):
        self.name = name
        self.condition = 'Used'  # Initial condition is 'Used'

    def repair(self):
        self.condition = 'New'  # Set condition to 'New' after repair


        # Example usage:
        item = Shoe('Laptop')
        print(item.condition)  # Output: Used

        # item.repair()
        # print(item.condition)  # Output: New


product = Shoe("Nike", "L")
print(product.get_brand())  # Output: Nike
print(product.get_size())   # Output: L

product.set_values("Adidas", "M")
print(product.get_brand())  # Output: Adidas
print(product.get_size())   # Output: M
