# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:13:05 2026

@author: kulde
"""

class Animal:
    def __init__(self, name):
        self.name = name
        
        
    def speak(self):
        print("Some common sound of the animal")
        
        

# Defining the child class
# I am telling python that this Animal class is parent class to the Dog class.
class Dog(Animal):
    def attack(self):
        print("Attack by a dog")



class Cat(Animal):
    def speak(self):
       print(f"{self.name} says Meowwww")      
       
       
dog1 = Dog("Buddy") 
cat1 = Cat("Kitty")


dog1.attack() 

# dog1 object will be able to borrow the method from the animal parent class     
dog1.speak()


# This method speak() from the Cat class will be able to override the method of parent class
 # as the method of child class already exists in Cat class.
cat1.speak()


print(dog1.name)
print(cat1.name)
###############################################



# Many times I do not want to access the properties directly with the help of object

# So, we can make the properties to be private and anything that is private needs to be accessed
 # through their method only.
 
 
 
class Animal1:
    def __init__(self, name):
         self.__name = name      # making this property to be private
         
         
    def speak(self):
        print("Some common sound of the animal")
         
         

 # Defining the child class
 # I am telling python that this Animal class is parent class to the Dog class.
class Dog1(Animal1):
    def attack(self):
         print("Attack by a dog")



class Cat1(Animal1):
    def speak(self):
        print(self.__name,"says Meowwww")      
        
        
dog1 = Dog1("Buddy") 
cat1 = Cat1("Kitty")



# Trying to access the property directly using object.
dog1.__name
dog1.speak()
cat1.speak()
