class Database:
    def __init__(self):
        # Store everything in dictionaries for simplicity
        self.books = {}
        self.students = {}
        self.issued = {}   # (student_id, book_id) → True 