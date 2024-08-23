"""
a = 5, 6, 7
a[2]=9
print(a)
"""
"""
a = 1, 2
b = (4, 5)
d = (a, b)
print(d[0])  # (1,2)
"""
"""
a = 1, 2
b = 4, 5
d = a + b
print(d[2])
"""
"""
a = ("ab", "abc", "def","a")
print(min(a))
"""

"""
def multiply(a, b, c, *more):
    value = a * b * c
    for i in more:
        value = value * i
    return value


V = multiply(1, 2, 3, 4, 5)
print(V)
"""

"""
def sum_multiply(a, b, *more):
    sum_value = a + b
    m_value = a * b
    for i in more:
        sum_value += i
        m_value *= i

    return sum_value, m_value


s_m = sum_multiply(2, 3, 4)
print(s_m)
"""

"""
d = {1: 2, "abc": 5, "def": 7}
print(d[0])  # Error
"""
"""
d = {1: 2, "abc": 5, "def": 7}
print(d.get(0, 5))
"""
"""
d = {1: 2, "abc": 5, "def": 7}
if 2 in d:
    print("Present")
else:
    print("Not Present")
"""
"""
a = {1: 2, "list": [1, 2], 3: 5}
b = {4: 5, 3: 7}
a.update(b)
print(a[3])
"""
"""
a={1:2, 'list':[1,2],3:5}
a.pop('list')
a['list']=[3,5]
print(a['list'])

"""
"""
s = {1, 2, 3, 4, 5, 2, 3, 1}
print(len(s), end=" ")
s.add(4)
s.add(3)
print(len(s))
"""

s = {}
s.add(4)
s.add(34)
print(len(s))
