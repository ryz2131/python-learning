a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.union(b))   
print(a | b)  # This is the same as a.union(b)
print(a.intersection(b))  # This will print the common elements between sets a and b
# print(a & b)  # This is the same as a.intersection(b)
# print(a.difference(b))  # This will print the elements that are in set a but not in set b
# print(a - b)  # This is the same as a.difference(b)
print(a.symmetric_difference(b))  # This will print the 
print(a ^ b)  # This is the same as a.symmetric_difference(b)
print(a.isdisjoint(b))  # This will print False because sets a and b have common elements
print(a.issubset(b))  # This will print False because set a is not a subset of set b
print(a.issuperset(b))  # This will print False because set a is not a superset of set b
print(a.copy())  # This will print a copy of set a
print(a.clear())  # This will clear all elements from set a
print(a)  # This will print an empty set because set a has been cleared
print(a.add(10))  # This will add the element 10 to set a
print(a)  # This will print the set a with the element 10 added
print(a.remove(10))  # This will remove the element 10 from set a   
print
