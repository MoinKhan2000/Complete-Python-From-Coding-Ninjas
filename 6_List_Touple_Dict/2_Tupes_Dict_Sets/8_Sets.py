a = {
    2,
    3,
    452,
    234,
    23,
    23,
}
print(a)
print(type(a))

# Iterating through set
for el in a:
    print(el)

# is key preset
print(23 in a)  # True

# Len(set)
print(len(a))  # 5

# Add / Update
a.add(23)
print(a)
b = {12, 32, 53423, 53, 32, 1}
a.update(b)
print(a)

# Remove function is used to remove the element from the set if not present - Key Error
# a.remove(45)    # Key Error (value not present)
print(a)
a.remove(12)
print(a)


# Discard function is used to remove the element from the set if not present - Don't do anything
a.discard(34)
print(a)

a.pop()  # remove first element
print(a)

a.clear()
print(a)
