lst1 = [1, 2, 3, 4, 5, 6]
touple = (1, 2, 3, 4, 5, 6)

# print(id(lst1), id(touple), lst1, touple)
# 1927611127552 1927611281952 [1, 2, 3, 4, 5, 6] (1, 2, 3, 4, 5, 6)

print(id(lst1[0]), id(touple[0]))
# 1927609843952 1927609843952

# print(type(lst1), type(touple))
# <class 'list'> <class 'tuple'>


a = 3, 5, 23, 2, 2
# print(a, type(a))
# (3, 5, 23, 2, 2) <class 'tuple'>

a, b = 2, (2, 4, 23, 6, 2, 3)
# print(a, b)
# 2 (2, 4, 23, 6, 2, 3)


# print(b)
# (2, 4, 23, 6, 2, 3)
# print(b[::-1])
# (3, 2, 6, 23, 4, 2)

""" Touples are immutable / lists are Mutable"""

newTouple = (1, 3, 4, 5)
# newTouple[0] = 2
# TypeError: 'tuple' object does not support item assignment

del newTouple
print(newTouple)
# touple is not defined
 