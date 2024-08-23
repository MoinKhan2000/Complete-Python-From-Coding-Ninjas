def checkMember(n):
    a=0;
    b=1;
    c=a+b;
    if(n==1 or n==0):
        return True
    else:
        while c<=n:
            a=b
            b=c
            c=a+b
            if(c==n):
                return True
        return False
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")