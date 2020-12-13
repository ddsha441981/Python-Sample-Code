# Author: Deendayal Kumawat
""" Date: 11/12/19
Descriptions: TypeCasting """
# Typecasting
print("*********Typecasting*********")

a = "4545"
b = 456
c = 45.20
print("*********Printing DataType of Variable*********")
print(type(a))
print(type(b))
print(type(c))
print("*********Converting DataType*********")
a = int(a)
print(a + 5)  # Convert String to Integer
b = str(b)
print(b + " Deendayal")  # Convert Integer to String
c = int(c)
print(c + 4)  # Convert Float to Integer

print("*********After Converting Printing DataType of Variable*********")
print(type(a))
print(type(b))
print(type(c))