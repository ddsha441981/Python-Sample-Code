# Author: Deendayal Kumawat
""" Date: 02/03/20
Descriptions: File & IO"""

# Use open function to read the content of a file
'''
If we don't delecare file mode then python by deault mode is r(read)
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
# file = open("sample.txt","r")
file = open("sample.txt")  # By Default mode is r
#data = file.read() # Read a file content
data = file.read(5) # Read only first 5 Character of a file
print(data) # Display file content
file.close() # Close file
