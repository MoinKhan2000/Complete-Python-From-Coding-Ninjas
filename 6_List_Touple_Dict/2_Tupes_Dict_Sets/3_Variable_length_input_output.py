# Variable Length IN Input

"""
def sum(a, b, *more):
    add = 0
    for i in more:
        add += i
    return a + b + add


print(sum(2, 3, 4, 5, 2, 4, 3, 324))
"""

# Variable Length IN Input


def sum_add_multiply(a, b):
    return a + b, a - b, a * b


sum, add, multple = sum_add_multiply(3, 4)
print(sum_add_multiply(2, 3))
print(sum, add, multple)
