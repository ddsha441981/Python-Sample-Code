# Author: Deendayal Kumawat
""" Date: 20/12/19
Descriptions: Dictionary and Sets """
# Dictionary is a collections of key and value pair
# In dictionary we can't use duplicate key but we can use duplicate value
# Dictionary is unordered
# Dictionary is mutable
# Dictionary is indexed

# Create a dictionary using {}
print("********* Dictionary and Sets *********")
favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
favLang['shubham'] = a
favLang['ankit'] = b
favLang['sonali'] = c
favLang['harshita'] = d

print(favLang)