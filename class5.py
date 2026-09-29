# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:46:24 2026

@author: kulde
"""
## Using lists inside the class
"""
Using a List in a Class
A list is useful when you want to store multiple items in order.
"""

class Student:
    def __init__(self,name):
        self.name = name
        self.subjects = []
        
        
    def add_subjects(self, subject):
        self.subjects.append(subject)
        
        
    def display(self):
        print(f"Student:{self.name}")
        print(f"Subjects:{self.subjects}")
        
      
        
# Initializing the object:
stu1 = Student("kuldeep")      

stu1.display()        


# Adding subjects for stu1
stu1.add_subjects("Mathematics")
stu1.add_subjects("Machine Learning")
stu1.add_subjects("Agentic AI")


stu1.display()



###===========================================================================

## Using dictionary inside the class
"""
Suppose a school has many students and each student has multiple details.
"""

class Student:
    def __init__(self):
        # Dictionary to store student details
        self.students = {}

    def add_student(self, roll_no, name):
        self.students[roll_no] = name
        print(f"Student '{name}' added successfully.")

    def display_students(self):
        print("\nStudent Records:")
        for roll_no, name in self.students.items():
            print(f"Roll No: {roll_no}, Name: {name}")

    def search_student(self, roll_no):
        if roll_no in self.students:
            print(f"Student Found: {self.students[roll_no]}")
        else:
            print("Student not found.")

    def delete_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]
            print("Student deleted successfully.")
        else:
            print("Student not found.")


# Creating object of class
s = Student()

# Adding students
s.add_student(101, "Rahul")
s.add_student(102, "Priya")
s.add_student(103, "Amit")

# Display all students
s.display_students()

# Search a student
s.search_student(102)

# Delete a student
s.delete_student(101)

# Display again
s.display_students() 