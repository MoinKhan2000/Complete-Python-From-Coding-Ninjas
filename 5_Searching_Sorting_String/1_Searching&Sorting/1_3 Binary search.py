def binSearch(lst, elem):
    """
    The function `binSearch` implements the binary search algorithm to find the index of a target
    element in a sorted list.
    :param lst: The `lst` parameter is a list of integers. It represents the sorted list in which we
    want to search for the element
    :param elem: The `elem` parameter represents the element that we are searching for in the list
    :return: The `binSearch` function returns the index of the `target` element in the sorted list
    `lst`. If the `target` element is not found in the list, it returns -1.
    """
    lst.sort()
    listLength = len(lst)
    l = 0
    u = listLength - 1
    m = (u + l) // 2
    while l <= u:
        if lst[m] == elem:
            # Means we got the element we were looking for
            return m

        elif lst[m] > elem:
            # lower bound will not be change
            u = m - 1
            m = (u + l) // 2
        else:
            # Upper bound will not be change
            l = m + 1
            m = (u + l) // 2
    return -1


# The code is taking user input to perform a binary search on a sorted list.
number = int(input())
lst = [int(x) for x in input().split()]
target = int(input())
print(binSearch(lst, target))
