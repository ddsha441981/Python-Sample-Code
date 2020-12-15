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

dic = {}  # Empty Dictionary
print(dic)

dic = {1: "abc", 2: "dd"}

dic[2]="Deendayal" # Updating value
print(dic)

dic = {
    "language": "Java",
    "py": "Very Simple Language",
    "marks": [1, 44, 56, 78, 67],
    "languages": {"Java": "Powerful Language", "Python": "For Hackers Language"}
}
print(dic['language'])
print(dic['py'])
print(dic['marks'])
dic['marks'] = 16,18 # No duplicate contains keys
print(dic['marks'])
print(dic['languages'])
print(dic['languages']['Python'])  # Nested Dictionary
# print(dic)
# print(dic[1])
# print(dic.keys()) # Print keys
# print(dic.values()) # Print Values
