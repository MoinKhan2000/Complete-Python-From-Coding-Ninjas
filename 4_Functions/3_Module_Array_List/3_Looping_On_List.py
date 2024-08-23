l = [23, "Moin Khan", 52, 235, True, "C", False, 23.253, None]

# If index is required then use for in loop with range
for i in range(len(l)):
    print(i, l[i])

# If index is not required then use this one
for i in l:
    print(i, end="  ")
print()

# If index is not required and we have to start from particular number then use this one
for i in l[2:]:
    print(i, end="  ")
