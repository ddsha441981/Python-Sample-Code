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

myDict = {
    "fast": "In a Quick Manner",
    "dd": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'}
}
# Dictionary Methods
# We can convert dictionary in list format
print(list(myDict.keys()))  # Prints the keys of the dictionary
print(myDict.values())  # Prints the keys of the dictionary
print(myDict.items())  # Prints the (key, value) for all contents of the dictionary
print(myDict)

updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "dd": "A Dancer"
}
myDict.update(updateDict)  # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("dd"))  # Prints value associated with key "dd"
print(myDict["dd"])  # Prints value associated with key "dd"

# The difference between .get and [] sytax in Dictionaries?
# print(myDict.get("dd2"))  # Returns None as dd2 is not present in the dictionary
# print(myDict["dd2"])  # throws an error as dd2 is not present in the dictionary
