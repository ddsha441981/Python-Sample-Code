# Author: Deendayal Kumawat
""" Date: 22/12/19
Descriptions: Loop"""

'''
f example
we can define f statement to print a string in print 
method and we can also declare variables with help of  {} braces
print(f"Hello {Variable Name} Python {Variable Name}")
'''

num = int(input("Enter any Number.....\n"))
# for i in range(0,11):
#     i = i * num
#     print(i)

i = 0
while i <= num:
    i = i * num
    i = i + 1
    # print(i)
    print(f"Table is {i} X {num} = {i * num} ")
