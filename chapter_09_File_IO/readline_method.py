# Author: Deendayal Kumawat
""" Date: 02/03/20
Descriptions: File & IO"""
'''
readline() method
We can also use readline() method to read a line of a file at same time
'''
file = open("sample.txt")
# Read first line of a file
text = file.readline()
print(text)

# Read second line of a file so on.....
text = file.readline()
print(text)

# Read 3rd line of a file
text = file.readline()
print(text)

# Read 4th line of a file
text = file.readline()
print(text)

file.close()
