# Author: Deendayal Kumawat
""" Date: 02/03/20
Descriptions: File & IO"""

# Use open function to read the content of a file
'''
If we don't declare file mode then python by default mode is r(read)
We can also specify the number of character in read() function :
file.read(5) Read only first 5 Character of a file

Mode of Files
r = open for reading
w = open for writing
a = open for appending
+ = open for updating and reading

Binary Files Mode
rb = will open for binary mode
rt = will open for read in text mode

syntax
with open("filename.txt","r") as f:
file = f.read()
print(file)
file.close()

In file handling using with we don't need to close file because with automatically it's close

'''

# Reading Mode
with open("with_file.txt", "r") as f:
    file = f.read()
print(file)
# file.close()

# Writing Mode
with open("with_file_writing.txt", "w") as file:
    myFile = file.write("Hello This is example of with syntax..... in Writing mode")
