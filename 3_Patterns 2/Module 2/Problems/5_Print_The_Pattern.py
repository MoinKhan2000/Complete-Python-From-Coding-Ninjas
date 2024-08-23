"""import math
number=int(input(""))
if (number==1):
    print(1, end=" ");
elif number<=0:
    pass
else:
    pattern1 = math.ceil(number / 2)
    pattern2 = number - pattern1
    # print(pattern1, pattern2)
    # print("")
    for i in range(0, pattern1, 1):
        num = 1
        num += number * i * 2
        for j in range(1, number + 1):
            print(num, end=" ")
            num += 1
        print()

    if number%2==0:
        num2 = num
    else:
        num2=num-number*2
    for l in range(0, pattern2):
        num3 = num2
        for k in range(1, number + 1):
            print(num3, end=" ")
            num3 += 1
        print()
        num2 -= number * 2
"""

# n=int(input())
n=4;
startValue=1;
for i in range(1, n+1):
    for j in range(startValue, startValue+n):
        print(j, end=" ");
    print()
    if (i==((n+1)//2)):
        if(n%2)!=0:
            startValue=n*(n-2)+1
        else:
            startValue=n*(n-1)+1
    elif((i>((n+1)//2))):
        startValue=startValue-2*n
    else:
        startValue=startValue+2*n
        