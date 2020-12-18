# Author: Deendayal Kumawat
""" Date: 22/12/19
Descriptions: Conditionals"""
text = input("Enter name........")
if (text in "dD"):
    flag = True
    print(flag)
elif text in "DD":
    flag = True
    print(flag)
else:
    flag = False
    print(flag)
