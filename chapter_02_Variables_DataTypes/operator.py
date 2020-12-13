# Author: Deendayal Kumawat
""" Date: 11/12/19
Descriptions: Operators"""

# Arithmetic Operator
print("*********Arithmetic Operators*********")
a = 3
b = 5
print("Value is 3+5 = ", 3 + 5)  # Arithmetic Operator
print("Value is 3+5 = ", 3 - 5)  # Arithmetic Operator
print("Value is 3+5 = ", 3 * 5)  # Arithmetic Operator
print("Value is 3+5 = ", 3 / 5)  # Arithmetic Operator

# Assignment Operators
print("*********Assignment Operators*********")
a = 20
a += 25
a -= 25
a *= 25
a /= 25
print(a)  # Assignment Operators

# Comparison Operators
print("*********Comparison Operators*********")
f0 = (50 > 100)
f1 = (50 < 100)
f2 = (50 <= 100)
f3 = (50 >= 100)
f4 = (100 == 100)
f5 = (100 != 100)

print(f0)  # Result is False
print(f1)  # Result is True
print(f2)  # Result is True
print(f3)  # Result is False
print(f4)  # Result is True
print(f5)  # Result is False

# Logical Operators
print("*********Logical Operators*********")
bool1 = True
bool2 = False
print("Value is bool1 and bool2 is " ,(bool1 and bool2)) # Result False
print("Value is bool1 or bool2 is " ,(bool1 or bool2)) # Result True
print("Value is not bool2 is " ,( not bool2)) # Result True