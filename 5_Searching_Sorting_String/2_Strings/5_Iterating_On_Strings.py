str = "Hello World"
for i in range(len(str)):
    print(str[i], end=" ")
print()

for el in str:
    print(el, end=" ")
print()


# In and Notin Operation on String
name = "Moin Khan"
if "Khan" in name:
    print("yes")

if "Mohsin" not in name:
    print("No not present")
