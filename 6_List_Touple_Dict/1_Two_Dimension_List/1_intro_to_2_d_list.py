li = [
    [1, 2, 3, 4],
    [11, 21, 31, 41],
    [12, 2, 23, 42],
    [13, 2, 33, 43],
]

print(id(li))
for el in li:
    print(id(el))
    for i in el:
        print(i, id(i), end=" ")
    print()
