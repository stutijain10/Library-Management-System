# Library Management System
# --------------------------------
# This program allows users to add books, register students, 
# issue books, return them and view stored records.
# Everything is kept in simple dictionaries for easy access.

from book import Book
from student import Student 
from database import Database

db = Database()

def add_book():
    print("\n--- Add Book ---")
    book_id = input("Enter Book ID: ").strip()
    # Check if book already exists
    if book_id in db.books:
        print("A book with this ID already exists. Try a different ID.\n")
        return
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    try:
        qty = int(input("Enter Quantity: ").strip())
    except ValueError:
        print("Invalid quantity.\n")    
        return

    db.books[book_id] = Book(book_id, title, author, qty)
    print("Book Added Successfully!\n")

def add_student():
     print("\n--- Add Student ---")
     s_id = input("Enter Student ID: ").strip()
     # Check if student already exists 
     if s_id in db.students:
         print("A Student with this ID alredy exists.\n")
         return
     name = input("Enter Student Name: ").strip()
     db.students[s_id] = Student(s_id, name)
     print("Student Added Successfully!\n")

def issue_book():
    print("\n--- Issue Book ---")
    s_id = input("Enter Student ID: ").strip()
    # Check if student exists
    if s_id not in db.students:
        print("Student not found.\n")
        return

    b_id = input("Enter Book ID: ").strip()
    #Check if book exists
    if b_id not in db.books:
        print("Book not found.\n")
        return

    book = db.books[b_id]
    # Check quantity
    if book.quantity <= 0:
        print("No copies available.\n")
        return
    # Check if already issued
    if (s_id, b_id) in db.issued:
        print("Already issued to this student.\n")
        return
    # Issue the book
    book.quantity -= 1
    db.issued[(s_id, b_id)] = True
    print("Book issued successfully.\n")

def return_book():
    print("\n--- Return Book ---")
    s_id = input("Enter Student ID: ").strip()
    b_id = input("Enter Book ID: ").strip()

    if (s_id, b_id) not in db.issued:
        print("No matching record.\n")
        return
    # Add book back
    db.books[b_id].quantity +=1
    del db.issued[(s_id, b_id)]
    print("Book returned successfully.\n")

def view_books():
    if not db.books:
        print("No books added yet!")
    else:
        print("\n---- Book List ----")
        for book_id, book in db.books.items():
            book.display()
        print("----------------\n")

def view_students():
    print("\n--- Student List ---")
    if not db.students:
        print("No students found.\n")
        return
    
    for s in db.students.values():
        s.display()
    print()

def menu():
    while True:
        print("=====  Library Management System  =====")
        print("1. Add Book")
        print("2. Add Student")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            add_student()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_books()
        elif choice == "6":
            view_students()
        elif choice == "7":
            break
        else:
            print("Invalid option.\n")

menu()

