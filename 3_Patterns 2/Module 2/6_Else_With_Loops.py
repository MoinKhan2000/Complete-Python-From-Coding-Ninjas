# If Break Statment is Met during the execution of the loop then else condition will never execute

"""
i=1;
while i<10:
    print(i, end="")
    i+=1
else:
    print("\nHii")
    
"""    
"""
for i in range(10):
    print(i, end="")
else:
    print("\nhii")
"""
"""
for i in range(10):
    print(i, end="")
    if i==5:
        break
else:
    print("\nhii")
    
"""

n=int(input())
for d in range(2, n, 1):
    if n%d==0:
        break;
else:
    print(n ,"Is Prime Number")