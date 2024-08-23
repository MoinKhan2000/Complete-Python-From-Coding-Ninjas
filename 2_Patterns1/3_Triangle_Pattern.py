"""
n=int(input(""));
i=0;
while i<n:
    j=0;        # Stars in Square Shape
    # j=i;        # Decreasing Star
    j=n-i-1;    # Increasing Star   
    k=1;
    while j<n:
        print(k, end="");
        k+=1;
        j+=1; 
    print("");
    i+=1;

4
1
12
123
1234

"""


"""
n=int(input(""));
i=1;
while i<=n:
    j=n-i;    # Increasing Star   
    k=i;
    while j<n:
        print(k,end="")
        k+=1;
        j+=1;
    print("");
    i+=1;

4
1
23
345
4567

"""

"""
n=int(input(""));
i=1;
num=1;
while i<=n:
    j=1;   # Increasing Star   
    while j<=i:
        print(num,end=" ")
        num+=1;
        j+=1;
    print("");
    i+=1;
4
1 
2 3
4 5 6
7 8 9 10

"""

n=int(input())
x = ord('A');
i=0;
while i<n:
    j=0;
    while j<=i:
        print(chr(x+j) , end="");
        j+=1;
    print("")
    x=x+1;
    i+=1;

# number=int(input(""))
# start_alphabet=ord('A')
# # print(ord('A'))
# cur_alphabet=start_alphabet+number-1;
# print(chr(cur_alphabet));
# i=number;
# while i!=0:
#     print(chr(cur_alphabet))
#     cur_alphabet=cur_alphabet-1;
#     i-=1;
