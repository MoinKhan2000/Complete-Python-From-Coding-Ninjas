l = [1, 2, 3, 4, "Moin Khan", True, False, 23.25, 532.342]


def printList(l):
    for item in l:
        print(item, end="   ")
    print()


# printList(l)
l[2] = "Mohsin Khan"  # List are mutable
# printList(l)
# l[99]="99 element"      IndexError: List assignment index out of range


# Slicing Of A List l[1:3:1]    -> Start from 1 index till 3-1=2 and the step is 1 (range())
"""
print(l[1:3])  # [2, 'Mohsin Khan']
print(l[:])  # [1, 2, 'Mohsin Khan', 4, 'Moin Khan', True, False, 23.25, 532.342]
print(l[1:10:2])  # [2, 4, True, 23.25]
print(l[:-1])  # [1, 2, 'Mohsin Khan', 4, 'Moin Khan', True, False, 23.25]
"""

# Insert And Append Element IN List
"""
# Insert 124 at index 2 if the index is provided > len(l) then at last the element will be inserted
l.insert(2, 124)
printList(l)

# Append the element at last only.
l.append("CSE")
printList(l)

# Appending the list into list
l.append([9, 10, 100])
printList(l)

# Same as previous
l.insert(2, [12, 43, 21, 42, 12])
printList(l)

# Extending a list - Adding list items as an element into the list (add multiple elements in the last only)
l.extend([2, 353, 2, "Extended"])
printList(l)

"""

printList(l)
# Removing Elements from list

# remove(2) will remove element whose value is 2 (only first) if 2 is not exists in the list then throw an error
l.remove(2)
printList(l)

# pop() will remove the last element from the list
l.pop()
printList(l)

# pop(2) will remove the second element from the list if that index is not available then throw an error
l.pop(4)
printList(l)


print(len(l))
