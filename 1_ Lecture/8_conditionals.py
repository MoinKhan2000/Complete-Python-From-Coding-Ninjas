a = True
print(type(a))

# Relational Operators

a = 10
b = 20
# print(a == b)  # False
# print(a < b)  # True
# print(a > b)  # False
# print(a <= b)  # True
# print(a >= b)
# print(a != b)

c1 = a > 10
c2 = b > 10
print(c1, c2)  # False True
print(c1 or c2)  # True
print(c1 & c2)  #False
print(c1 and c2)  # False
print(not (c1))