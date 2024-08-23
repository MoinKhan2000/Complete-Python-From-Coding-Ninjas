def insertionSort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while l[j] > key and j >= 0:
            l[j + 1] = l[j]
            j -= 1

        l[j + 1] = key

    print(l)


# number = int(input())
# lst = [int(x) for x in input().split()]
# insertionSort(lst)

l = [12, 54, 65, 7, 23, 9]
insertionSort(l)
