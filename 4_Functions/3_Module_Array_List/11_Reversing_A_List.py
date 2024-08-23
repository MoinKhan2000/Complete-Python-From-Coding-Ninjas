def reverseList(l):
    length = len(l)
    for i in range(0, (len(l) // 2)):
        # temp = l[i]
        # l[i] = l[length - i - 1]
        # l[length - i - 1] = temp
        l[i], l[length - i - 1] = l[length - i - 1], l[i]
    print(l)


def reverseList2(l):
    length = len(l)
    for i in range(0, (len(l) // 2)):
        # temp = l[i]
        # l[i] = l[length - i - 1]
        # l[length - i - 1] = temp
        l[i], l[-i - 1] = l[-i - 1], l[i]
    print(l)

def reverseList3(l):
    l

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(li)
# reverseList2(li)
# reverseList(li)
# print(li)
print(li)
print(li[::-1])
