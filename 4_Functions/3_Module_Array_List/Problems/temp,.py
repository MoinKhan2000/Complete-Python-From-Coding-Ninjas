def findUnique(l):
    l2 = []
    for i in range(len(l)):
        count = 1
        for j in range(len(l)):
            if i == j:
                break
            if l[i] == l[j]:
                l2.append(l[i])
    for i in range(len(l2)):
        l.remove(l2[i])
        l.remove(l2[i])
    l2.remove(1)
    return l[0]


l = [1, 2, 3, 4, 2, 3, 1]
print(findUnique(l))
