# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:09:57 2026

@author: kulde
"""

class Car:
    def __init__(self):
        print("I am a constructor..")
        
        
    def going_forward(self):
        print("Car is going forward....")


# Creating an object.
car1 = Car()
car2 = Car()
car3 = Car()        


# Now, calling the methods associated with the objects.
car1.going_forward()
car2.going_forward()
car3.going_forward()
        