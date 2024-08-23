number = int(input(""))
upperTriangle = (number // 2) + 1
bottomTriangle = number - upperTriangle

x = bottomTriangle
while x != 0:
    j = 1
    s = 0
    while s < x - 1:
        print(" ", end="")
        s += 1

    while j <= x:
        print("* ", end="")
        j += 1

    x -= 1
    print("")

