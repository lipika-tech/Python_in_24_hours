cart = ["shirt","lamp","pen"]
print(cart)

#Empty List
mylist= []
print(mylist)


Vowels ="aeiou"
#Convert the string into the list
Vowels_list =list(Vowels)
print(Vowels_list)

#Access the item from the list
languages = ["python","java", "c++"]
print(languages[-1])

#Update the String
cart= ["shirt","lamp","pen"]

cart[0]="shoes"
print(cart)

#Addiing to the list
cart= ["shirt","lamp","pen"]
cart.append("Book")
print(cart)

#Adding two list
cart= ["shirt","lamp","pen"]
fav=["headphones","phone"]
cart.extend(fav)
print(cart)


#Inserting the item to the list
cart= ["shirt","lamp","pen"]
cart.insert(2, "Book")
print(cart)

# Remove the item from the list
cart= ['Shirt',"Lamp","Pen","Book","Crayons"]
cart.remove("Pen")
print(cart)

#Remove the last item from the list
cart= ['Shirt',"Lamp","Pen","Book","Crayons"]
last_item= cart.pop()
print(cart)
#print(last_item)



#Claer the list
cart= ['Shirt',"Lamp","Pen","Book","Crayons"]
cart.clear()
print(cart)


#Delete the item using indexing
cart= ['Shirt',"Lamp","Pen","Book","Crayons"]
del cart[2]
print(cart)

# delete the entire list
cart= ['Shirt',"Lamp","Pen","Book","Crayons"]
del cart
print(cart)

#slicing
cart= ['Shirt',"Lamp","Pen","Book","Crayons"]
del cart[:2]
print(cart)



























