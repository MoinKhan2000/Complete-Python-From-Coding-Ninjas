number = int(input("Enter the length \n"))
l = []
 

def sum(l):
    sum = 0
    for i in l:
        sum += i
    return sum


for i in range(number):
    num = int(input(f"Enter {i+1} Element "))
    l.append(num)
print(l)

print("The sum of these elements is", sum(l))
