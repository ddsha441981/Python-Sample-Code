# Author: Deendayal Kumawat
""" Date: 22/12/19
Descriptions: Conditionals"""
sub1 = int(input("Enter 1st subject marks....\n"))
sub2 = int(input("Enter 2nd subject marks....\n"))
sub3 = int(input("Enter 3rd subject marks....\n"))
sub4 = int(input("Enter 4th subject marks....\n"))
sub5 = int(input("Enter 5th subject marks....\n"))
sub6 = int(input("Enter 6st subject marks....\n"))
total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
percentage = total * 100 / 600
print("Your Percentage is " ,percentage)
if percentage > 90:
    print("Grade Excellent")
elif percentage > 80:
    print("Grade A")
elif percentage > 70:
    print("Grade B")
elif percentage > 60:
    print("Grade C")
elif percentage > 50:
    print("Grade D")
else:
    print("Fail")
