# Author: Deendayal Kumawat
""" Date: 20/12/19
Descriptions: Dictionary and Sets """
# Sets is a collections of  non repetitive elements
# Sets can't contains duplicate values
# Sets is unordered because doesn't matter which order we'll use
# There is no way to change items in sets
# In set we can't access element by using index
# We can't use list in sets because list is hashable(updatable)
# We can't use dictionary in sets because dictionary is hashable(updatable)
# We can use tuples in sets

print("********* Dictionary and Sets *********")

num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))
num4 = int(input("Enter number 4\n"))
num5 = int(input("Enter number 5\n"))
num6 = int(input("Enter number 6\n"))
num7 = int(input("Enter number 7\n"))
num8 = int(input("Enter number 8\n"))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)