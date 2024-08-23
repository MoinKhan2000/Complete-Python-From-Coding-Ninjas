"""         Lists Are Mutable           """

"""
def inc(l):
    for i in range(len(l)):
        l[i] += i


l = [1, 2, 3, 4]
print(l)  # [1, 2, 3, 4]
inc(l)
print(l)  # [1, 3, 5, 7]

"""


def inc(l):
    l = [1, 2, 3]
    # Here the reference is changed so that the original l will not change


l = [1, 2, 3, 4]
print(l)  # [1, 2, 3, 4]
inc(l)
print(l)  # [1, 2, 3, 4]
