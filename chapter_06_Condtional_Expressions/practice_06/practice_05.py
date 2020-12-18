# Author: Deendayal Kumawat
""" Date: 22/12/19
Descriptions: Conditionals"""
text = input("Enter name.....\n")
nameList = ['dd','abc','xyz','wxy','AtoZ','aToz']
if text in nameList:
    print("Yes" ,text,''' is Available in List''')
else:
    print("Not Found.......")