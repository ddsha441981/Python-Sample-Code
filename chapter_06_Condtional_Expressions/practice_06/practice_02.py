# Author: Deendayal Kumawat
""" Date: 22/12/19
Descriptions: Conditionals"""

subject1 = int(input("Enter First Subject of Marks \n " ))
subject2 = int(input("Enter Second Subject of Marks \n " ))
subject3 = int(input("Enter Third Subject of Marks \n " ))
if(subject1 < 33 or subject2 < 33 or subject3 < 33):
    print("You are fail because you gain less 33%")
elif(subject1+subject2+subject3) / 3 < 40 :

    print("You are fail due to total percentage less than 40")
else:
    print("You are Passed")