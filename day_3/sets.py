# Sets are used to store multiple items in a single variable
# frequently used in math operations such as unions, intersections
# and differences (these are also keywords when using set)
# Like lists, sets are mutable, but the elements are immutable.
# Sets cannot have two items with the same value.

my_set = {1,2,3,4,5}
other_set = {3,5,5,6,7}
print(my_set.intersection(other_set)) # prints out which values are similar from both sets
print(my_set.union(other_set)) # prints out a combination of the set, starting with my_set and then other_set, no repeat of values
print(my_set.difference(other_set)) # prints out what is different/ unique within both sets