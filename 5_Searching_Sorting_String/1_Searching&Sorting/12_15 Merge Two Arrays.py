"""import math
import sys


def merge2SortedLists(l1, l2):
    l4 = []
    i = 0
    j = 0
    k = 0
    while i < len(l1) and j < len(l2):
        if l1[i] >= l2[j]:
            l4.append(l2[j])
            k += 1
            j += 1
        elif l1[i] < l2[j]:
            l4.append(l1[i])
            k += 1
            i += 1
    while i < len(l1):
        l4.append(l1[i])
        i += 1

    while j < len(l2):
        l4.append(l2[j])
        j += 1

    for el in l4:
        print(el, end=" ")


def getData(number):
    for i in range(number):
        num1 = int(input())
        if num1 > 0:
            lst1 = [int(x) for x in input().split()]
        else:
            lst1 = []
        num2 = int(input())
        if num2 > 0:
            lst2 = [int(x) for x in input().split()]
        else:
            lst2 = []
        if num1 > 0 or num2 > 0:
            merge2SortedLists(lst1, lst2)


number = int(input())
for i in range(1,number+1):
    getData(i)
sys.exit()
"""

"""
import sys
import math


def merge2SortedLists(l1, l2):
    l4 = []
    i = 0
    j = 0
    k = 0
    while i < len(l1) and j < len(l2):
        if l1[i] >= l2[j]:
            l4.append(l2[j])
            k += 1
            j += 1
        elif l1[i] < l2[j]:
            l4.append(l1[i])
            k += 1
            i += 1
    while i < len(l1):
        l4.append(l1[i])
        i += 1

    while j < len(l2):
        l4.append(l2[j])
        j += 1

    for el in l4:
        print(el, end=" ")


def getData(number):
    for i in range(number):
        try:
            num1 = int(input(""))
            if num1 > 0:
                lst1 = [int(x) for x in input().split()]
                lst1 = lst1[:num1:]
            else:
                lst1 = []
            num2 = int(input(""))
            if num2>0:
                lst2 = [int(x) for x in input().split()]
                lst2 = lst2[:num2:]
            else:
                lst2=[]

            merge2SortedLists(lst1, lst2)
        except EOFError:
            break


number = int(input())
for i in range(0, number + 1):
    getData(i)

sys.exit()
"""


"""

from sys import stdin

def merge(arr1, n, arr2, m) : 
    #Your code goes here
    ans = (n + m) * [0]
    i = 0 
    j = 0 
    k = 0
    while i < n and j < m :
        if arr1[i] < arr2[j] :
            ans[k] = arr1[i]
            k += 1 
            i += 1 
        else : 
            ans[k] = arr2[j] 
            k += 1 
            j += 1 
    while i < n :
        ans[k] = arr1[i]
        k += 1
        i += 1
    while j < m :
        ans[k] = arr2[j]
        k += 1
        j += 1
    return ans 


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1
    
"""


import sys
import math


def merge2SortedLists(l1, l2):
    l4 = []
    i = 0
    j = 0
    k = 0
    while i < len(l1) and j < len(l2):
        if l1[i] >= l2[j]:
            l4.append(l2[j])
            k += 1
            j += 1
        elif l1[i] < l2[j]:
            l4.append(l1[i])
            k += 1
            i += 1
    while i < len(l1):
        l4.append(l1[i])
        i += 1

    while j < len(l2):
        l4.append(l2[j])
        j += 1

    for el in l4:
        print(el, end=" ")


def getData(number):
    for i in range(number):
        try:
            num1 = int(input(""))
            if num1 > 0:
                lst1 = [int(x) for x in input().split()]
                lst1 = lst1[:num1:]
            else:
                lst1 = []
            num2 = int(input(""))
            if num2 > 0:
                lst2 = [int(x) for x in input().split()]
                lst2 = lst2[:num2:]
            else:
                lst2 = []

            merge2SortedLists(lst1, lst2)
        except EOFError:
            break


number = int(input())
for i in range(0, number + 1):
    getData(i)
