num=int(input())
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        
if(prime):
    print("This number is prime");
else:
    print("This number is not prime")