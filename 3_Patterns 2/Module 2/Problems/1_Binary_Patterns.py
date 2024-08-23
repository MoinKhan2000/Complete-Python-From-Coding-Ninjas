"""
11111
0000
111
00
1
"""
number = int(input())
for i in range(1, number + 1, 1):
    flag = True
    for j in range(number, i - 1, -1):
        if i % 2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    print()
