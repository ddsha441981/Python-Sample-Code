# Author: Deendayal Kumawat
""" Date: 11/12/19
Descriptions: List And Tuples """
# List is a just like container which store set of value of any data type
# Create a list using []
print("*********List and Tupples*********")
std1 = input("Enter marks of student 1 \n")
std2 = input("Enter marks of student 2 \n")
std3 = input("Enter marks of student 3 \n")
std4 = input("Enter marks of student 4 \n")
std5 = input("Enter marks of student 5 \n")
std6 = input("Enter marks of student 6 \n")
print("*******After Sorting Student Marks*********")

stdList = [std1,std2,std3,std4,std5,std6]
stdList.sort()
print(stdList)