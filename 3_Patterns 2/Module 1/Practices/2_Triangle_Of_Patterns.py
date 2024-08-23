number = int(input())
i = 1

while i <= number:
    spaces = 1
    while spaces <= number - i:
        print(" ", end="")
        spaces += 1
    num = 1
    num2 = i
    while num <= i:
        k = num
        print(num2, end="")
        k += 1
        num += 1
        num2 += 1
    num2 -= 1
    decNum = num2
    while decNum != i:
        decNum -= 1
        print(decNum, end="")

    print("")
    i += 1
