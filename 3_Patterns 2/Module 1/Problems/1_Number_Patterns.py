number = int(input())
i = 1
k=1;
while i <= number:
    k=1;
    while k<=i:
        print(k , end="");
        k+=1;
    s=1;
    while s<= number*2-2*i:
        print(" ", end="");
        s+=1;
    rn=i
    while rn>0:
        print(rn , end="")
        rn-=1
        
    print("")
    i += 1

"""
spaces = 1
    while spaces <= number - i:
        print(" ", end="")
        spaces += 1
    stars = 1
    while stars <= i:
        k = stars
        print(k, end="")
        k += 1
        stars += 1
"""
