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
'''
# file = open("writing.txt","w") # Writing mode
file = open("writing.txt", "a")  # Appending mode
# text = file.write("Welcome To ")
text = file.write(" \n Python")
file.close()
