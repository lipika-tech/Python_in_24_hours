# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:30:03 2026

@author: kulde
"""

# Using super() in the python
class Employee:
    def __init__(self,name):
        self.name = name
        
        
    def show_details(self):
        print(f"Employee: {self.name}")
        
        
class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language  
        
        
    def show_details(self):
        print(f"Developer:{self.name}")
        print(f"Language:{self.language}")
        
        
emp1 = Employee("kuldeep")        
emp1.show_details()

dev1 = Developer("bertram","python")
dev1.show_details()



############################################

