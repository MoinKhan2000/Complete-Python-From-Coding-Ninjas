number = int(input())
i=1;

while i<=number:
    spaces=1;
   
    while spaces<=number-i:
        print(" ", end="");
        spaces+=1;
    stars=1;
    while stars<=i:
        k=stars
        print(k, end="");
        k+=1;
        stars+=1;
    print("")
    i+=1
    