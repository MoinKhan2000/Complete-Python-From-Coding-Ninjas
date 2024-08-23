n = int(input(""))
i = 1
k = n
while i <= n:
    j = n - i + 1
    while j != 0:
        print(k, end="")
        j -= 1
    print("")
    k -= 1
    i += 1
