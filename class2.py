# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:35:28 2026

@author: kulde
"""

class Car:
    def __init__(self, model, price):
        print("I am a constructor..")
        self.model = model
        self.price = price
        
        
    def going_forward(self):
        print("Car is going forward....")
        
    
    def car_info(self):
        print(f"My car model is {self.model} and it's price is {self.price}")

# Creating an object.
car1 = Car("suzuki i30",20000)
car2 = Car("kia saltos",15000)
car3 = Car("ford endeavour", 35000)        


# Now, calling the methods associated with the objects.
car1.going_forward()
car2.going_forward()
car3.going_forward()



car1.car_info()
car2.car_info()
car3.car_info()
        