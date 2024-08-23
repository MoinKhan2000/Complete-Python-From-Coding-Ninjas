"""
li = ["abcd", "def"]
li.insert(4, 5)
print(li)
"""

"""
li=['abcd',5,'def',5]
li.remove(5)
print(li)
"""
"""
li = [5, 2, 6, 8]
li.pop(2)
print(li)
"""
"""
li = [1, 2, 3, 4, 5]
for i in li[1:4]:
    print(i, end=" ")
"""
"""
n = int(input())
li = []
for i in range(n):
    li.append(input())
print(li)
"""
"""
li = [x for x in input().split()]
print(li)
"""
"""
def change(li):
    li[1]=li[1]+2
li=[1,2,3,4,5]
change(li)
print(li)
"""


def change(li):
    li[1] += 2
    print(id(li))
    li = [2, 2, 2, 4, 5]
    print(id(li))

li = [1, 2, 3, 4, 5]
change(li)
print(id(li))
print(li)
print(id(li))