number = int(input("enter your number\n"))
i = 1
while i <= number:
    j = 1
    while j <= i:
        if j == i:
            print("*", end="")
        else:
            print("0", end="")
        j += 1

    k = number - i
    while k != 0:
        print("0", end="")
        k -= 1

    l = 1
    while l <= 1:
        print("*", end="")
        l += 1
    m = number - i
    while m != 0:
        print("0", end="")
        m -= 1

    l = 1
    while l <= 1:
        print("*", end="")
        l += 1

    n = i - 1
    while n != 0:
        print("0", end="")
        n -= 1
    i += 1
    print("")
