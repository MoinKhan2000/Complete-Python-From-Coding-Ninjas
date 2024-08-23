number = int(input())
i = 1
halfStar = number // 2
while i <= halfStar:
    spaces = 1
    while spaces <= halfStar - i + 1:
        spaces += 1
        print(" ", end="")

    # Increasing Sequence
    num = 1
    while num <= i:
        incNum = num
        print("*", end="")
        incNum += 1
        num += 1
    decNum = i - 1
    while decNum >= 1:
        print("*", end="")
        decNum -= 1
    print("")
    i += 1
fullStar = number - halfStar
i = fullStar
while i >= 1:
    spaces = 1
    while spaces <= fullStar - i:
        print(" ", end="")
        spaces += 1
    num = 1
    # Increasing Sequence
    while num <= i:
        incNum = num
        print("*", end="")
        incNum += 1
        num += 1
    decNum = i - 1
    while decNum >= 1:
        print("*", end="")
        decNum -= 1
    print("")
    i -= 1


print(halfStar, fullStar)
