# Read It
# Demonstrates reading from a text file


# This read() function will read the whole file at a time and then iterate over every character one 
 # by one.

# This is not a good idea when dealing with a big file....
print("Opening and closing the file.")
text_file = open("read_it.txt", "r")
text_file.close()

print("\nReading characters from the file.")
text_file = open("read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nReading the entire file at once.")
text_file = open("read_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()



# readline() will read only one line at a time and then iterate over it till that line will not get 
 # finished

# Once, reading that line is finished then readline() method will move to the other line.
print("\nReading characters from a line.")
text_file = open("read_it.txt", "r")
print(text_file.readline(1))
print(text_file.readline(20))
print(text_file.readline(4))
text_file.close()



# If you do not pass any number in the function then it will return the whole current line 
print("\nReading one line at a time.")
text_file = open("read_it.txt", "r")

# If you do not pass any number in the readline() function then this function will read the whole 
 # current line where the cursor is present. 
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()




### radlines() function will read the whole file into the list 

# Each line will become a member in the list....
print("\nReading the entire file into a list.")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(lines) 
print(len(lines))


for line in lines:
    print(line)

text_file.close()



# This way you can simply read the whole file and print each line by iterating with the 
 # help of for loop.....
print("\nLooping through the file, line by line.")
text_file = open("read_it.txt", "r")
for line in text_file:
    print(line)
text_file.close()

input("\n\nPress the enter key to exit.")
