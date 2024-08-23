def linearSearch(l, num):
    index = -1
    for elem in range(len(l)):
        if l[elem] == num:
            index = elem
    return index


l = []
num = int(input("Enter number of elements \n"))
for i in range(num):
    n = int(input(f"Enter {i} element \n"))
    l.append(n)


number = int(input("Enter the number to be find \n"))

index=linearSearch(l,number)
if(index!=-1):
    print(f"{number} is present at index {index}.")
else:
    print("Number is not present")