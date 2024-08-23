"""
# Sum of n numbers 

n=int(input(""));
a=1;
sum=0
while a <= n:
    sum = a + sum;
    a=a+1;
print("sum is ", sum)

"""
# sum of even numbers
n=int(input("Enter your number "));
a=1;
sum=0
while a<=n:
    if(a%2==0):
        sum=sum+a;
    a=a+1
print(sum)