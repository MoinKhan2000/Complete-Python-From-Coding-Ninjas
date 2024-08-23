"""
i=1;
while i<10:
    if i==5:
        break
    print(i, end=" ");
    i=i+1;
    
"""

"""
num=int(input())
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break 
if(prime):
    print("This number is prime");
else:
    print("This number is not prime")
    
"""

num=int(input())
k=2;
while k<=num:
    d=2
    flag=False
    while d<k:
        if k%d==0:
            flag=True
            break
        d+=1;
    if(flag==False):
        print(k)
    k+=1