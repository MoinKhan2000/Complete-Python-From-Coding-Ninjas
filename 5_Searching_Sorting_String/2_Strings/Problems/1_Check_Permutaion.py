from sys import stdin


def isPermutation(string1, string2):
    # Create lists to hold characters of string1 and string2
    ls1 = list(map(str, string1))
    ls2 = list(map(str, string2))

    # Initialize a frequency array to track character occurrences
    frequencyArr = []

    # Initialize the frequency array with zeros for each ASCII character (0-255)
    for i in range(256):
        frequencyArr.append(0)

    # Check if lengths of the two strings are equal
    if len(ls1) == len(ls2):
        # Count character frequencies in string1
        for el in ls1:
            ordEl = ord(el)  # Get ASCII value of the character
            frequencyArr[ordEl] += 1

        # Decrease character frequencies in string2
        for el in ls2:
            ordEl = ord(el)  # Get ASCII value of the character
            frequencyArr[ordEl] -= 1

        # Check if all character frequencies are zero, indicating a permutation
        isTrue = all(v == 0 for v in frequencyArr)
        if isTrue:
            return True  # Strings are permutations of each other
    else:
        return False  # Different lengths, not permutations


# Main section
string1 = stdin.readline().strip()  # Read the first string
string2 = stdin.readline().strip()  # Read the second string

ans = isPermutation(string1, string2)  # Check if strings are permutations

# Print the result
if ans:
    print("true")  # Strings are permutations
else:
    print("false")  # Strings are not permutations


""" 
For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.
Permutations of each other
Two strings are said to be a permutation of each other when either of the string's characters can be rearranged so that it becomes identical to the other one.

Example: 
str1= "sinrtg" 
str2 = "string"

The character of the first string(str1) can be rearranged to form str2 and hence we can say that the given strings are a permutation of each other.
Input Format:
The first line of input contains a string without any leading and trailing spaces, representing the first string 'str1'.

The second line of input contains a string without any leading and trailing spaces, representing the second string 'str2'.
Note:
All the characters in the input strings would be in lower case.
Output Format:
The only line of output prints either 'true' or 'false', denoting whether the two strings are a permutation of each other or not.

You are not required to print anything. It has already been taken care of. Just implement the function. 
Constraints:
0 <= N <= 10^6
Where N is the length of the input string.

Time Limit: 1 second
Sample Input 1:
abcde
baedc
Sample Output 1:
true
Sample Input 2:
abc
cbd
Sample Output 2:
false
"""
