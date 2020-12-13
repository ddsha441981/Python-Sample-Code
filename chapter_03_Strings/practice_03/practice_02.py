# Author: Deendayal Kumawat
""" Date: 11/12/19
Descriptions: String Practice 02 """
print('''
*************************
*   H   e   l   l   o   *
*   0   1   2   3   4   *
*   H   e   l   l   o   *
*   -4 -3  -2  -1  -0   *
*************************
''')

print("*************Üsing Input Method**************")

letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''

name = input("Enter Name....\n")
date = input("Enter Date....\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)