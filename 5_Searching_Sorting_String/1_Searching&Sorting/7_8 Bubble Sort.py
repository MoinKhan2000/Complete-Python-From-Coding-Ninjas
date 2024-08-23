"""
def bubbleSort(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                l[j], l[i] = l[i], l[j]

    for el in l:
        print(el, end=" ")


number = int(input())
lst = [int(x) for x in input().split()]
bubbleSort(lst)
"""


# Optimized Solution by Instructor
def bubbleSort(l):
    isSorte = True
    for i in range(len(l) - 1):
        isSorte = True
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                isSorte = False
        # Assume the array is sorted - If sorted then dont need to continue the function to waste time
        print(f"After {i} pass", l)   
        if isSorte:
            break
        # print(i, l)

    for el in l:
        print(el, end=" ")


# # According to the instructer
# def bubbleSort(l):
#     lenght = len(l)
#     for i in range(lenght):
#         for j in range(lenght - 1):
#             if l[j] >= l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#         print(f"After {i} pass", print(l))
#     print(l)


# l = [3, 43, 34, 64, 23, 532, 623, 324, 23, 236, 2213, 652, 3256, 234, 623, 4]
# l = [6, 0, 3, 5]
# l = [9, 5, 7, 3, 1, 4]
l = [10, 8, 1, 3, 3, 4, 5, 6]
bubbleSort(l)
