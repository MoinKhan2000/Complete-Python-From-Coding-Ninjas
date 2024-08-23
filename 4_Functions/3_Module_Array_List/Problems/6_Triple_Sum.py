"""
    Triplet Sum
Send Feedback
You have been given a random integer array/list(ARR) and a number X. Find and return the number of triplets in the array/list which sum to X.
Note :
Given array/list can contain duplicate elements.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'X'.
Output format :
For each test case, print the total number of triplets present in the array/list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 50
0 <= N <= 10^2
0 <= X <= 10^9
Time Limit: 1 sec
Sample Input 1:
1
7
1 2 3 4 5 6 7 
12
Sample Output 1:
5
Sample Input 2:
2
7
1 2 3 4 5 6 7 
19
9
2 -5 8 -6 0 5 10 11 -3
10
Sample Output 2:
0
5


 Explanation for Input 2:
Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.

For the second query, we have 5 triplets in total that sum up to 10. They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) and (-6, 5, 11)
    
"""
def tripletSum(l, sum):
    # print(l)
    l2 = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if sum == (l[i] + l[j] + l[k]):    
                    # print(l[i], l[j], l[k])
                    if l[i] >= l[j] and l[i] >= l[k]:
                        if l[j] >= l[k]:
                            pair = [l[k], l[j], l[i]]
                        else:
                            pair = [l[j], l[k], l[i]]
                    elif l[j] >= l[i] and l[j] >= l[k]:
                        if l[i] >= l[k]:
                            pair = [l[k], l[i], l[j]]
                        else:
                            pair = [l[k], l[i], l[j]]
                    elif l[k] >= l[i] and l[k] >= l[j]:
                        if l[i] >= l[k]:
                            pair = [l[k], l[i], l[k]]
                        else:
                            pair = [l[i], l[k], l[k]]

                    # print(pair)
                    # isPresent = l2.count(pair)
                    # if isPresent == 0:
                    l2.append(pair)
    # print(l2)
    return len(l2)


# l = [2, 5, 2, 2, 5, 2, 5]
# l = [1, 3, 6, 2, 5, 4, 3, 2, 4]
# l = [2, 8, 10, 5, -2, 5]
# l = [2, -5, 8, -6, 0, 5, 10, 11, -3]
# l = [1, 2, 3, 4,5,6,7]
# l = [9, 3, 3, 5, 6, 7, 3, -1, 1]
# print(tripletSum(l, 12))
# l = [5, 5, 4, 4, 5, 4]
# print(tripletSum(l, 13))

def getList(n):
    num = int(input())
    if num > 0:
        l = [int(x) for x in input().split()]
        sum = int(input())
        print(tripletSum(l, sum))
    else:
        print(0)


number = int(input())
for i in range(number):
    # print(i, end=" ")
    getList(i)
