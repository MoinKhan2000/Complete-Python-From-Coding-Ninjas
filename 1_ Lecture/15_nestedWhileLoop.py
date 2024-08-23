#  All prime numbers from 2 to n
n = int(input("Enter your number\n"))
a = 2

while a <= n:
    flag = True
    b = 2
    while b < a:
        if a % b == 0:
            flag = False;
        b = b + 1

    if(flag):
        print(a)
    a = a + 1
