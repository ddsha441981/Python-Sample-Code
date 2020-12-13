# Author: Deendayal Kumawat
""" Date: 11/12/19
Descriptions: String Methods """
print('''
*************************
*   H   e   l   l   o   *
*   0   1   2   3   4   *
*   H   e   l   l   o   *
*   -4 -3  -2  -1  -0   *
*************************
\n''')

print("***********Strings Methods***********")
name = "deendayal kumawat"
print(name)
print("***********Strings Length***********")
c = len(name)
print(c)
print("***********Strings endswith***********")
c = name.endswith("day")  # False
c = name.endswith("yal")  # True
print(c)
print("***********Strings Count***********")
c = name.count("e") # Count of String
print(c)
print("***********Strings Capitalize***********")
c = name.capitalize() # Capitalize of First Character of String
print(c)
print("***********Strings Find***********")
c = name.find("dayal") # Find the word and return Index of the string
print(c)
print("***********Strings Replace***********")
c = name.replace("deendayal","Hello User")
print(c)
print("***********Strings Spilt***********")
c = name.split()
print(c)
print("***********Strings SwapCase***********")
c  = name.swapcase()
print(c)