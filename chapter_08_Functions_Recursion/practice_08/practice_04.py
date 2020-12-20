# Author: Deendayal Kumawat
""" Date: 22/12/19
Descriptions: Functions & Recursion"""

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Harry is a good      "
n = remove_and_split(this, "DD")
print(n)
# print(this)
# print(this.strip())
