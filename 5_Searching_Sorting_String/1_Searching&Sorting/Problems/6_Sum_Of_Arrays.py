# """
# Sum of Two Arrays
# Send Feedback
# Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively. Both the arrays/lists contain numbers from 0 to 9(i.e. single digit integer is present at every index). The idea here is to represent each array/list as an integer in itself of digits N and M.
# You need to find the sum of both the input arrays/list treating them as two integers and put the result in another array/list i.e. output array/list will also contain only single digit at every index.
# Note:
# The sizes N and M can be different.

# Output array/list(of all 0s) has been provided as a function argument. Its size will always be one more than the size of the bigger array/list. Place 0 at the 0th index if there is no carry.

# No need to print the elements of the output array/list.
# Using the function "sumOfTwoArrays", write the solution to the problem and store the answer inside this output array/list. The main code will handle the printing of the output on its own.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the first array/list.

# Second line contains 'N' single space separated integers representing the elements of the first array/list.

# Third line contains an integer 'M' representing the size of the second array/list.

# Fourth line contains 'M' single space separated integers representing the elements of the second array/list.
# Output Format :
# For each test case, print the required sum of the arrays/list in a row, separated by a single space.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# 0 <= M <= 10^5
# Time Limit: 1 sec
# Sample Input 1:
# 1
# 3
# 6 2 4
# 3
# 7 5 6
# Sample Output 1:
# 1 3 8 0
# Sample Input 2:
# 2
# 3
# 8 5 2
# 2
# 1 3
# 4
# 9 7 6 1
# 3
# 4 5 9
# Sample Output 2:
# 0 8 6 5
# 1 0 2 2 0
# """


# from sys import stdin


# def sumOfTwoArrays(arr1, n, arr2, m, output):
#     # if n == m:
#     #     for i in range(n):
#     #         arr1[i] = arr1[i] + arr2[i]
#     num1=0;
#     for i in range(n):
#         num1+=arr1[i];
#     printList(arr1, n)


# # Taking Input Using Fast I/O
# def takeInput():
#     n = int(stdin.readline().rstrip())
#     if n == 0:
#         return list(), 0

#     arr = list(map(int, stdin.readline().rstrip().split(" ")))
#     return arr, n


# # to print the array/list
# def printList(arr, n):
#     for i in range(n):
#         print(arr[i], end=" ")

#     print()


# # main
# t = int(stdin.readline().rstrip())

# while t > 0:
#     arr1, n = takeInput()
#     arr2, m = takeInput()

#     outputSize = 1 + max(n, m)
#     output = outputSize * [0]

#     sumOfTwoArrays(arr1, n, arr2, m, output)
#     # printList(output, outputSize)

#     t -= 1


"""
from sys import stdin


def sumOfTwoArrays(arr1, n, arr2, m, output):
    pass


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    outputSize = 1 + max(n, m)
    output = outputSize * [0]

    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)

    t -= 1
"""
from sys import stdin


def sumOfTwoArrays(arr1, n, arr2, m, output):
    k = max(n, m)
    result = []
    for i in range(k+1):
        result.append(0)

    i = n - 1
    j = m - 1
    carry = 0
    while k >= 0:
        d = carry
        if i >= 0:
            d += arr1[i]
        if j >= 0:
            d += arr2[j]

        carry = d // 10
        d = d % 10

        result[k] = d  # Fix the index here
        i -= 1
        j -= 1
        k -= 1

    if carry > 0:
        print(carry, end=" ")
    printList(result, len(result))


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    outputSize = 1 + max(n, m)
    output = outputSize * [0]

    sumOfTwoArrays(arr1, n, arr2, m, output)

    t -= 1
