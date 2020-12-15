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
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))