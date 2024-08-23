n=int(input(""));
i=1;
dig=0;
while i<=n:
    j=1;
    while j<=i:
        if(i==1 and j==1):
            print(1 , end="")
        elif(j==1):
            print(dig, end="");
        elif(i==j):
            print(dig , end="");
        else:
            print("0",end="")
        j+=1;
    print("");
    dig+=1;
    i+=1;