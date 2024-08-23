lst = [1, 2, 3, 4, 54, 2, 23, 21, 12, 3, 1, 1]
uniqueNumbers = set(lst)
print(uniqueNumbers)

sum = 0
for el in uniqueNumbers:
    sum += el
print(sum)


s = {}
print(type(s))  # dict

s = ()
print(type(s))  # tuple

s = set()
print(type(s))  # set
