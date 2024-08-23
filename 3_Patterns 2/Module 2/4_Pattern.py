"""
number = int(input())
for i in range(1, number + 1):
    # For Spaces
    for s in range(i, number):
        print(" ", end="")
    print(i, end="")

    # For Increasing Number
    k = i + 1
    for n in range(1, i):
        print(k, end="")
        k += 1

    # For Decreasing Number
    x=k-1;
    for m in range(x, i,-1):
        x=x-1;
        print(x, end="")
        
    print()


    1
   232
  34543
 4567654
567898765

"""
# Another Way - Basically A Good Way

# n = int(input())
# for i in range(1, n + 1):
#     # For spaces
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(i, 2 * i, 1):
#         print(j, end="")
#     for m in range(2 * i - 2, i - 1, -1):
#         print(m, end="")
#     print()


number = int(input())
for i in range(1, number + 1):
    # For Spaces
    for s in range(i, number):
        print(" ", end="")
    print(i, end="")

    # For Increasing Number
    k = i + 1
    for n in range(1, i):
        print(k, end="")
        k += 1

    # For Decreasing Number
    x=k-1;
    for m in range(x, i,-1):
        x=x-1;
        print(x, end="")
        
    print()
