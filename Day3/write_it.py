# Write It
# Demonstrates writing to a text file


# Writing a file, if file is not present then file will get created and if file is present then
 # file will be overwritten....
print("Creating a text file with the write() method.")
text_file = open("write_it.txt", "w")

# Result will not shown until the file is closed....
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close()



# Now, reading the file as discussed in reading part
print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()


# This is just the opposite of the reallines function.
# Here, you can write the list into a file. 
print("\nCreating a text file with the writelines() method.")
text_file = open("write_it.txt", "w")
lines1 = ["Line 1\n",
         "This is line 2\n",
         "That makes this line 3\n"]

# All the content of the list will be writtne in one line only
lines2 = ["Line 1",
         "This is line 2",
         "That makes this line 3"]

text_file.writelines(lines1)
text_file.writelines(lines2)
text_file.close()




print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()

input("\n\nPress the enter key to exit.")
