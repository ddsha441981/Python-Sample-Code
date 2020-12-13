# Author: Deendayal Kumawat
""" Date: 11/12/19
Descriptions: String Practice 04 """
print('''
*************************
*   H   e   l   l   o   *
*   0   1   2   3   4   *
*   H   e   l   l   o   *
*   -4 -3  -2  -1  -0   *
*************************
''')

print("*************Üsing Input Method**************")
# name = "This is a string with double  spaces  ok"
name = input("Enter String..With space \n ")
name = name.replace("  ", " ")
print(name)