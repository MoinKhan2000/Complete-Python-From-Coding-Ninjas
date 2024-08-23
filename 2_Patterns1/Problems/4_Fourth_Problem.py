n=int(input(""));
i=0;
while i<n:
    j=i;        # Decreasing Star
    k=1;
    while j<n:
        print(k, end="");
        k+=1;
        j+=1; 
    print("");
    i+=1;
