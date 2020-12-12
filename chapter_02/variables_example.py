# Author: Deendayal Kumawat
""" Date: 11/12/20
Descriptions: Variables"""
'''
Python understand automatically data type 
if we don't define data type,
Python understand automatically it's type
that which data type we define
'''
'''
Note 
Python Support case sensitive variable
like 
a = 56
A = 35
print(a) # Result is 56
print(A) # Resuld is 35'''

a = 10  # Int Value
b = 20  # Int Value
c = 45.20523  # float value
sum = 0
# Different Method to define String
# name = "Python"  # String
# name = 'Welcome to Python'  # String

# Printing the variables
print("****************Printing the variables**************")

name = '''Welcome to Python Programming Language.
 Python language is a very simple 
 and it's just like  a English Language'''
sum = a + b + c
print(sum)
print(name)

# Boolean
print("****************Printing the Boolean**************")
flag1 = True
flag2 = False
d = None # None = Null
print(flag1)
print(flag2)
print(d)

# Printing the type of variables
print("****************Printing the type of variables**************")
# type() method is used to identify type of variable
print(type(a)) # Integer Type
print(type(b)) # Integer Type
print(type(c)) # Float Type
print(type(sum)) # Float Type
print(type(name)) # String Type
print(type(d)) # None Type
print(type(flag1)) # Boolean Type
print(type(flag2)) # Boolean Type

'''
Note 
Small x and Capital X are different because
Python Support case sensitive variable
'''
print("****************Python Support case sensitive variable**************")
x = 56
X = 35
print(x) # Result is 56
print(X) # Resuld is 35
