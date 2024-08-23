a = {"a": 2, 3: 4, "list": [1, 2, 3], "dict": {1: 2}}
print(a)

# print(a[0]) # Error (Key Error)
print(a["a"])
print(a["list"][0])  # 1
print(a.get("a"))  # 2
print(a.get("li"))  # None  (If key is not present then returns None)
print(a.get("list"))  # [1,2,3]
# print(a.get("li", True)) #If the a["li"] is not present then return True otw return the value
print(a.get("li", True))
print(a.keys())  # dict_keys(['a', 3, 'list', 'dict'])
print(a.values())  # dict_values([2, 4, [1, 2, 3], {1: 2}])
# print(a.items())  #dict_items([('a', 2), (3, 4), ('list', [1, 2, 3]), ('dict', {1: 2})])
print(a.items())

for i in a:
    print(i, a[i])

for i in a.values():
    print(i)


# How to check if the key exists
print("list" in a)  # True
