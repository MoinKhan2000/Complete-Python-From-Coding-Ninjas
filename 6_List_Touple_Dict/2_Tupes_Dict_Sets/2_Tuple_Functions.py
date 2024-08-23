a = (1, 2, 3)
b = 4, 5
for i in a:
    print(i, end=" ")

# In - to check membership
print(1 in a)  # True Same as list
print(8 in a)  # False


# Concatination of two tuples
newTuple = a + b
print(newTuple)

# Tuple of tuples

anotherTuple = (a, b)  # (1, 2, 3, 4, 5)
print(anotherTuple)  # ((1, 2, 3), (4, 5))


# Repeating Tuples
repeatedTuple = a * 4
print(repeatedTuple)  # (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
l = [1, 2, 3, 4]
repeatedList = l * 3
print(repeatedList)  # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# min(a)
print(min(repeatedTuple))

# Mixing datatypes in single tuple
mixedTuple = (
    "Moin",
    True,
    bool,
    None,
    int,
    chr,
    23,
    "23",
    234.33,
    [2, 35, 2],
    (34, 32, 56, 3),
)
print(mixedTuple)
# ('Moin', True, <class 'bool'>, None, <class 'int'>, <built-in function chr>, 23, '23', 234.33)


lst = [1, 23, 3, 4]
tupleFromList = tuple(lst)
# tupleFromList[0] = 45  # Throw an error as tupleFromList is now a tuple
print(tupleFromList)


# min(a) within the strings - it will compare on the basis of the ASCII value
a = ("ib", "zbc", "zef", "i")
print(min(a))  # "i"
