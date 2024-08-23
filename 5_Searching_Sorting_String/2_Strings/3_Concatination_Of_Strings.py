"""             It not like that we are changing the string we are just crating a new string (Strings are immutable)           """


a = "red"
print(id(a))

a = a + " blue"
print(id(a))

a = a + " blue" + " green"
print(id(a))

a += " white"
print(id(a))

a = a * 4  # Appending the same string four times
print(id(a))
print(a)

a = a + "3"
a = a + str(23)
print(a)
