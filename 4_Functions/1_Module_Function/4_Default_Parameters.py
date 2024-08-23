def sum(a, b, c=0, d=0):
    print("d =", d, end=" ")
    print("c =", c, end=" ")
    return a + b + c + d


print(sum(1, 4))  # Right
print(sum(1, 4, 3))  # Right
print(sum(1, 2, 3, 4))  # Right

print(sum(1, 2, d=3, c=12))  # Right

# print(sum(1, d=2, c=4))  # Wrong ( b is required attribure )
