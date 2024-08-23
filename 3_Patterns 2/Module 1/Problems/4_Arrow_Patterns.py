"""
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*
"""
number = int(input(""))
upperTriangle = (number // 2) + 1
bottomTriangle = number - upperTriangle

i = 1
while i <= upperTriangle:
    j = 1
    s = 0
    while s < i - 1:
        print(" ", end="")
        s += 1

    while j <= i:
        print("* ", end="")
        j += 1

    i += 1
    print("")

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
