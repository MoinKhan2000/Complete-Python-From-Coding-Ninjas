"""  
Count And Say
Send Feedback
Write as you speak is a special sequence of strings that starts with string “1” and after one iteration you rewrite the sequence as whatever you speak.
Example :
The first few iterations of the sequence are :
First iteration: “1”
    As we are starting with one.

Second iteration: “11”
    We speak “1” as   “one 1” then we write it as “11”

Third iteration: “21”
    We speak “11” as “Two 1” then we write it as “21”

Fourth iteration: “1211”
    We speak “21” as “one 2, one 1”  then we write it as “1211”

Fifth iteration: “111221”
    We speak “1211” as “one 1, one 2, two 1” then we write it as “111221”

Sixth iteration: “312211”
    We speak “111221” as “three 1, two 2, one 1” then we write it as “312211”
You will be given a single positive integer N, Your task is to write the sequence after N iterations.
Input Format:
The first line of the input contains a single positive integer T, denoting the number of test cases.

The first line of each test case contains a single integer N, denoting the number of iterations.
Output Format:
For each query print the string that represents the sequence after the nth iteration.
Note:
You don't have to print anything, it has already been taken care of. Just Implement the given function.
Constraints:
1 <= T <= 10
1 <= N <= 30

Time Limit: 1 sec
Sample Input 1 :
2
1
2
Sample Output 1:
1
11
Explanation For Sample Input 2:
First iteration: “1”
    As we are starting with one.

Second iteration: “11”
    We speak “1” as   “one 1” then we write it as “11”
Sample Input 2 :
2
3
4
Sample Output 2:
21
1211

"""

import sys


def writeAndSay(n):
    sequence = "1"

    for j in range(n - 1):
        new_sequence = ""
        count = 1
        current_char = sequence[0]
        for i in range(1, len(sequence)):
            print(sequence)
            if sequence[i] == current_char:
                count += 1
            else:
                new_sequence += str(count) + current_char
                count = 1
                current_char = sequence[i]

        new_sequence += str(count) + current_char
        sequence = new_sequence

    return sequence


# Read the number of test cases
t = int(input())
for j in range(t):
    n = int(input())
    result = writeAndSay(n)
    print(result)

sys.exit()
