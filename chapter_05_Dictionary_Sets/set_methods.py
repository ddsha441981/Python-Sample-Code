# Author: Deendayal Kumawat
""" Date: 20/12/19
Descriptions: Dictionary and Sets """
# Sets is a collections of  non repetitive elements
# Sets can't contains duplicate values
# Sets is unordered because doesn't matter which order we'll use
# There is no way to change items in sets
# In set we can't access element by using index
# We can't use list in sets because list is hashable(updatable)
# We can't use dictionary in sets because dictionary is hashable(updatable)
# We can use tuples in sets

print("********* Dictionary and Sets *********")

# Creating an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)
## Length of the Set
print(len(b)) # Prints the length of this set

## Removal of an Item
b.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop())
print(b)