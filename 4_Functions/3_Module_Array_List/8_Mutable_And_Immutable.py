"""                 VARIABLES ARE IMMUTABLE               """
a = 5  # Here a is pointing to a memory location (2309709496688) where 5 is stored
# print(id(a))
a = 6  # Now a is pointing to a memory location (2309709496720) where 6 is stored
# print(id(a))  # Means a is not changing even a is pointing to a new location
a = 5  # Again a started to point previous memory location (2309709496688) where 5 was stored before changing the value
# print(id(a))

"""
l = [12, 43, "Moin Khan"]
# print(id(l))  # 2672185874176

for i in range(len(l)):
    print(id(l[i]), f"{l[i]}")

l[2] = "Mohsin Khan"
for i in range(len(l)):
    print(id(l[i]), f"{l[i]}")

l[2] = "Moin Khan"
for i in range(len(l)):
    print(id(l[i]), f"{l[i]}")
"""

"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 90]
print(id(l))
for i in range(1, 5):
    l.append(i)
print(id(l))
print(l)
"""
# Variables are immutable
a = 4
print(id(a))
x = a
print(id(x))
x = 5
print(id(x))


"""                 Lists Are Mutable           """
l1 = [1, 2, 3, 4]
l2 = l1
l2[2] = "Moin Khan"  # Changing the l2 will reflect in l1
print(l1[2])
