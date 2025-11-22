class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def display(self):
        # Show basic information about the book.
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Qty: {self.quantity}")