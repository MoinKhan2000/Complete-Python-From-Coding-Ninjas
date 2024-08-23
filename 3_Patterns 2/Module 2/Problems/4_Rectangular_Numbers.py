"""num=int(input())

for i in range(1, num + 1, 1):
    for j in range(1, i + 1, 1):
        print(num - j + 1, end="")

    for k in range(num - i, 0, -1):
        print(num - i + 1, end="")
    
    l = num + 1 - i
    for m in range(num - 1 - i, -1, -1):
        print(l, end="")

    for n in range(1,i+1):
        if n==1:
            continue
        print(num-i+n, end="")


    print()



for i in range(num-1, 0, -1):
    for j in range(1, i + 1, 1):
        print(num - j + 1, end="")

    for k in range(num - i, 0, -1):
        print(num - i + 1, end="")
    

    l = num + 1 - i
    for m in range(num - 1 - i, -1, -1):
        print(l, end="")
    # print(l)
    for n in range(1,i+1):
        if n==1:
            continue
        if n==num+1:
            continue
        print(num-i+n, end="")

    print()


"""


# Coding Ninja's Solution
n = int(input())
for i in range(1,n+1):
    temp = n
    for j in range(1,i):
        print(temp,end="")
        temp = temp -1
    for j in range(1,(2*n) - (2*i) + 2):
        print(n-i+1,end="")
    for j in range(1,i):
        temp = temp+1
        print(temp,end="")
    print()
for i in range(n-1,0,-1):
    temp = n
    for j in range(1,i):
        print(temp,end="")
        temp = temp - 1
    for j in range(1,(2*n) - (2*i) + 2):
        print(n-i+1,end="")
    for j in range(1,i):
        temp = temp+1
        print(temp,end="")
    print()