number = int(input())
i = 1
while i <= number:
    # Printing Spaces
    spaces = 1
    while spaces <= number - i:
        print(" ", end="")
        spaces += 1
    num = 1
    # Increasing Sequence
    while num <= i:
        incNum = num
        # decNum = num
        print(incNum, end="")
        incNum += 1
        num += 1
    # Decreasing Sequence
    decNum=i-1;
    # while decNum != 1:
    while decNum>=1:
        # decNum -= 1
        print(decNum, end="")
        decNum -= 1
    print("")
    i += 1
