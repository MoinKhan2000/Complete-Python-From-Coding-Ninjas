a = {1, 2, 3, 4}
b = {2, 3, 4, 5}

print(a.intersection(b))  # {2, 3, 4}
print(a.__xor__(b))  # {1,5}
print(a.__and__(b))  # {2, 3, 4}
print(a.__contains__(2))  # True
print(a.difference(b))  # 1
print(b.difference(a))  # 5
print(a.symmetric_difference(b))  # Union-Intersection {1,5}

# Updating the a by the intersection of a and b
a.intersection_update(b)
print(a)  # {2,3,4}

# Updating the a by the difference_update of a and b
a.difference_update(b)
print(a)  # set()

# Updating the a by the symmetrci difference of a and b
a.symmetric_difference_update(b)
print(a)  # {2,3,4,5}

# Updating the a by the union of a and b
a = a.union(b)  # There is no union_update()
print(a)  # {2,3,4,5}

print(a.issubset(b))  # True

b = {1}
c = {1, 2}

print(c.issuperset(b))  # True
print(c.isdisjoint(b))  # False

