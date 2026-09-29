# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:59:46 2020

@author: StormBreaker
"""


# Trying to read and write both with the different modes
# The pointer will be placed at the beginning of the file....

# Opens the file for both reading and writing.
# Does not truncate (erase) the file—keeps existing content.
# Requires that the file must exist; otherwise, it raises an error.
# The file pointer starts at the beginning of the file.

print("Reading and Writing the file with the r+ method")


# If you simply open and close the file then nothing will happen to the file
file_1 = open('write_it.txt','r+')
file_1.close()



# reopening the file 
file_1 = open('write_it.txt','r+')

# reading the whole file
print(file_1.read())


# Now, trying to write the file
file_1.write("Hello")


file_1.write("How are you ?")


file_1.close()




# First start writing the file rather than reading
file_1 = open('write_it.txt','r+')

# data will be written in the beginning as the pointer is at the beginning
file_1.write("lets try this one\n tried")

file_1.read()
file_1.close()


# ==================================================================================

# Opens the file for both reading and writing.
# Truncates (deletes) the existing content when the file is opened.
# If the file doesn’t exist, it creates a new one.
# The file pointer starts at the beginning of the empty file.

### Now, Trying the w+ method
file_2 = open('write_it_2.txt','w+')

file_2.write('i think i am writing\n this is the second line')

# This will not read anything as the cursor will be on last line
print(file_2.read())

file_2.close()




# writing first and then reading, this will create a new file and last data has been over written
file_2 = open('write_it_2.txt','w+')

file_2.readline()
file_2.readline()

file_2.write('writing third line\n')

file_2.close()




