def selectionSort(l):
    for i in range(len(l)-1):
        min_index = i
        for j in range(min_index + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[min_index], l[i] = l[i], l[min_index]
    for el in l:
        print(el, end=" ") 


# number = int(input())
lst = [int(x) for x in input().split(" ")]
selectionSort(lst)s
