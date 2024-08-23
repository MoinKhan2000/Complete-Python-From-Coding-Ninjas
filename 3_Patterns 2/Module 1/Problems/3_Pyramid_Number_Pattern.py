number = int(input())
i = 1
while i <= number:
    # Printing Spaces
    spaces = 1
    while spaces <= number - i:
        print(" ", end="")
        spaces += 1

    # Printing Increased Number
    num = 1
    num2 = i
    num3 = i
    while num <= i:
        k = num
        print(num3, end="")
        k += 1
        num += 1
        num2 += 1
        num3 -= 1
    num2 -= 1

    # Printing Decreased Number
    incNum = 1
    while incNum != i:
        incNum += 1
        print(incNum, end="")
    print("")
    i += 1
