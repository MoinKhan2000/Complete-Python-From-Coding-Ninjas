str = input().split()
n, m = int(str[0]), int(str[1])
b = input().split()
# arr = [[int(b[i * m + j]) for j in range(m)] for i in range(n)]
arr = [[int(b[i * m + j]) for j in range(m)] for i in range(n)]
print(arr)
# print(b)


# str = input().split()
# n = int(str[0])
# m = int(str[1])
# b = str[2:]

# arr = [[int(b[i * m + j]) for j in range(m)] for i in range(n)]
# print(arr)
