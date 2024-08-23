# Adding new element
a = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, "list": [1, 23, 3]}
print(a)
# {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 'list': [1, 23, 3]}

a["Name"] = "Moin Khan"
print(a)
# {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 'list': [1, 23, 3], 'Name': 'Moin Khan'}

# Using Update Function
# Updating the value of key where key=1 if value not present then adding as a new key
a.update({12: "one"})
print(a)

a.pop("list")
print(a)

del a["Name"]
print(a)

a.clear() 
print(a)
del a
print(a)

