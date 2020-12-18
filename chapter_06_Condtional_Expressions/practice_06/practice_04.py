# Author: Deendayal Kumawat
""" Date: 22/12/19
Descriptions: Conditionals"""

text = input("Enter Username Minimum 10 Character.....\n")
if (len(text) < 10):
    print("Error............Enter 10 Character of Username....")
else:
    print(text)
