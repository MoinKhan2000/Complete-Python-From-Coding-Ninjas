""" 
Remove Consecutive Duplicates
Send Feedback
For a given string(str), remove all the consecutive duplicate characters.
Example:
Input String: "aaaa"
Expected Output: "a"

Input String: "aabbbcc"
Expected Output: "abc"
 Input Format:
The first and only line of input contains a string without any leading and trailing spaces. All the characters in the string would be in lower case.
Output Format:
The only line of output prints the updated string.
Note:
You are not required to print anything. It has already been taken care of.
Constraints:
0 <= N <= 10^6
Where N is the length of the input string.

Time Limit: 1 second
Sample Input 1:
aabccbaa
Sample Output 1:
abcba
Sample Input 2:
xxyyzxx
Sample Output 2:
xyzx
"""

from sys import stdin


def removeConsecutiveDuplicates(string):
    # Your code goes here
    newStr="";
    ls2 = list(map(str, string))
    i=0
    while i<len(string):
        key=string[i];
        newStr+=key;
        count=0;
        j=0;
        j=i+1
        print(j)
        while (string[j]==key) and j<len(string)-1:
            i+=1
            j+=1
        i+=1
    
    print(ls2)
    print(string)


# main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
