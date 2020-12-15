# Author: Deendayal Kumawat
""" Date: 11/12/19
Descriptions: List And Tuples """
# List is a just like container which store set of value of any data type
# Creating a tuple using ()
# Cannot update the values of a tuple because tuples is immutable
print("*********List and Tupples*********")
t1 = (54,78,85)

t1[0] = 45 # TypeError: 'tuple' object does not support item assignment
print(t1)