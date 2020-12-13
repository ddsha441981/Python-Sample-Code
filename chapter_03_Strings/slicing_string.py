# Author: Deendayal Kumawat
""" Date: 11/12/19
Descriptions: String Slicing """
print('''
*************************
*   H   e   l   l   o   *
*   0   1   2   3   4   *
*   H   e   l   l   o   *
*   -4 -3  -2  -1  -0   *
*************************
''')
# String Slicing is part of String
print("**********Slicing***********")

name = "Deendayal"
greeting = "Hello "
c = greeting + name
print(type(name))
print(name)

print("**********Checking Length***********")
# name = name.__len__()  # Check length of String
print(name)

print("**********Checking Index***********")
print(name[0:4])
print(name[4:5])
print(name[5:7])
print(name[7:9])
# name[3] = "d" --> Does not work
# print(name[1:4])
# print(name[:4]) # is same as name[0:4]
# print(name[1:]) # is same as name[1:5]
c = name[-5:-1]  # is same is name[1:4]
print(c)
print("**********Negative Index***********")
name = name[-1]  # Last Character Print of Index
print(name)
