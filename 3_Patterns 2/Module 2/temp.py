"""
i=1;
while i<5:
    if i==3:
        break
    print(i, end="")
    i+=1
    
output=1 2

"""
"""
i=1;
while i<3:
    j=1;
    while j<5:
        if j==3:
            break
        print(j, end="")
        j+=1
    i+=1
    
# output= 1 2 1 2 
"""

"""
i=1;
while i<5:
    if i==6:
        break;
    print(i, end="")
    i=i+1
else:
    print("Else is also printed")
    
# 1234Else is also printed

"""

"""
i = 1
while i < 5:
    if i == 3:
        break
    print(i, end="")
    i += 1
else:
    print("Else is also printed")

# 1 2

"""

"""
i=1
while i<5:
    if i==3:
        print(i)
        continue
    print(i, end="")
    i+=1;
"""

i=1;
while i<3:
    j=0
    while j<5:
        j+=1;
        if j==3:
            continue
        print(j, end=" ")            
    i+=1
