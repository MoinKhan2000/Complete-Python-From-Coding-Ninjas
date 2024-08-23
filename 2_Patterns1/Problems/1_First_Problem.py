n=int(input(""));
i=0;
while i<n:
    j=0;        # Stars in Square Shape
    # j=i;        # Decreasing Star
    j=n-i-1;    # Increasing Star   
    k=1;
    while j<n:
        print(1, end="");
        k+=1;
        j+=1; 
    print("");
    i+=1;