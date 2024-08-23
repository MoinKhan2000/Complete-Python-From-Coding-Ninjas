n = int(input(""))
i = 1
dig = 2
while i <= n:
    j = 1
    while j <= i:
        if i == 1 and j == 1:
            print(1, end="")
        elif j == 1:
            print(1, end="")
        elif i == j:
            print(1, end="")
        else:
            print(dig, end="")
        j += 1
    print("")
    i += 1
