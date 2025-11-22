class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display(self):
        # Display the student's details.
        print(f"Student ID: {self.student_id}, Name: {self.name}")