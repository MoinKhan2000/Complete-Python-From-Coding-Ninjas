s = "Moin Khan"
print(s, id(s))
for el in s:
    print(el, id(el))

name = "Moin Khan"
print(name, id(name))
for el in name:
    print(el, id(el))

# Both s, and name have the same storage location even each character has the same storage

"""                     Strings are Immutable                       """
# s[1] = "m"  # This will throw an error

s = "Mohsin khan"  # This is valid
print(s)
