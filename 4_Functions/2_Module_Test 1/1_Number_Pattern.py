"""
Number Star pattern 1
Send Feedback
Print the following pattern for given number of rows.
Input format :
Integer N (Total number of rows)
Output Format :
Pattern in N lines
Sample Input :
   5
Sample Output :
 5432*
 543*1
 54*21
 5*321
 *4321
"""

num=int(input(""))
num2=num
for i in range(1, num+1):
    for j in range(1, num+1):
        if (num2==j):
            print("*", end="");
            num2-=1
        else:
            print(num-j+1, end="");
        
    print()