# a1 = 23
# a2 = 3.4
# a3 = 4 + 4j
# print(a3)
# print(type(a1))
# print(type(a2))
# print(type(a3))

# print(id(a3))
# a3 = 3
# print(id(a3))

# # Id would be same if the two variables containing same nubmers ranges between -5 to 256 only
# x = 4
# y = 4
# print(id(x), id(y))
# y = 5
# print(id(y))
# y = 4
# print(id(y))


a=10
id1=id(a)
b=a+2-2
id2=id(b)

print(id1,id2)

