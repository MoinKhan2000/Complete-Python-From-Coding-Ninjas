"""
Find Unique
Send Feedback
You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
You need to find and return that number which is unique in the array/list.
 Note:
Unique element is always present in the array/list according to the given condition.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.
Output Format :
For each test case, print the unique element present in the array.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
Time Limit: 1 sec
Sample Input 1:
1
7
2 3 1 6 3 6 2
Sample Output 1:
1
Sample Input 2:
2
5
2 4 7 2 7
9
1 3 1 3 6 6 7 10 7
Sample Output 2:
4
10
"""


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
    return l[0]

def getList(n):
    num=int(input())
    l = [int(x) for x in input().split()]
    el = findUnique(l)
    print(el)

number = int(input())
for i in range(number):
    # print(i, end=" ")
    getList(i)

