"""
123456
  23456
    3456
      456
        56
          6
        56
      456
    3456
  23456
123456

"""

# number = int(input(""))
# upperTriangle = (number // 2) + 1
# bottomTriangle = number - upperTriangle

# i = 1
# while i <= upperTriangle:
#     j = 1
#     s = 0
#     while s < i - 1:
#         print(" ", end="")
#         s += 1

#     while j <= i:
#         print("* ", end="")
#         j += 1

#     i += 1
#     print("")

# x = bottomTriangle
# while x != 0:
#     j = 1
#     s = 0
#     while s < x - 1:
#         print(" ", end="")
#         s += 1

#     while j <= x:
#         print("* ", end="")
#         j += 1

#     x -= 1
#     print("")


number = int(input())
for i in range(1, number + 1, 1):
    for s in range(1, i):
        print(" ", end="")

    for n in range(i, number + 1, 1):
        print(n, end="")
    print()
i=1;
for i in range(1, number, 1):
    for s in range(i, number-1,1):
        print(" ", end="")

    for n in range(number-i, number + 1, 1):
        print(n, end="")
    print()
