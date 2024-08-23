# Print Kth Alphabet
# k=int(input())
# print(ord('A'))     #65
# print(ord('B'))     #65
# print(chr(65))      #A
# print(chr(66))      #B
"""
x=ord('A');
i=0;
while i<k:
    j=0
    while j<k:
        print(chr(x+j) , end="");
        j+=1;
    print("")
    i+=1;
4
ABCD
ABCD
ABCD
ABCD

"""


"""
x=ord('A');
i=0;
while i<k:
    j=0
    while j<k:
        print(chr(x+j) , end="");
        j+=1;
    print("")
    x=x+1;
    i+=1;

4
ABCD
BCDE
CDEF
DEFG

"""



N = int(input(""))
start_alphabet = ord('A')
our_alphabet = start_alphabet + N - 1
i = 1
while i <= N:
    j = N - i
    k = i
    while j < N:
        print(chr(our_alphabet - k + 1), end="")
        k -= 1
        j += 1
    print("")
    i += 1


