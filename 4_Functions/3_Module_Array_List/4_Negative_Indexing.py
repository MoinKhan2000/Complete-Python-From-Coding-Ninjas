l = [1, 2, 3, 4, 5]
print(l[-1])  # 5
print(l[-2])  # 4
print(l[-3])  # 3
print(l[-4])  # 2
print(l[-5])  # 1
# print(l[-6])  # IndexError

# print(l[-len(l)])  # 1
print(l[100:1:-1])  # [5, 4, 3]
print(l[::-1])  # [5, 4, 3, 2, 1]
print(l[-1:])  # [5]
print(l[-1:-6:-1])  # [5, 4, 3, 2, 1]
