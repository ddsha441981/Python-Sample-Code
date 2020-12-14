# Author: Deendayal Kumawat
""" Date: 11/12/19
Descriptions: List And Tuples """
# List is a just like container which store set of value of any data type
# Create a list using []
print("*********List and Tupples*********")

abc = [1, 2, 5, 7, 9, 2, 5, 4]  # Without sort List
print(abc)
print("**********After Sorting********")
abc.sort()  # sorts the list
print(abc)
print("**********After Reversing********")
abc.reverse()  # Reverse the list
print(abc)

print("**********After Append end of the list********")
abc.append(58)  # Append end of the list
print(abc)

print("**********Add in middle in list********")
abc.insert(2, 585)  # inserts 585 at index 2
print(abc)

print("**********Remove Element from the list********")
abc.pop(4)  # removes element at index 4
print(abc)

print("**********Remove  from the list********")
abc.remove(2)  # removes 2 from the list
print(abc)
