# It is used to skip a special iteration if the condition is met then skip that iteration
# Whether the continue statement execute but still else condition will execute.
"""
for i in range(10):
    if(i==5):
        continue
    print(i, end="");
# 012346789
"""

"""
for i in range(10):
    if(i==5):
        continue
    print(i, end="");
else:
    print("Hii")
    
"""
# Question - Print the even numbers from 2 to n and avoid to print if the number is multiple of 7

n = int(input())
for i in range(2, n + 1, 2):
    if i % 7 == 0:
        continue
    print(i, end=" ")
    # 2 4 6 8 10 12 16 18 20 22 24 26 30 32 34 36 38 40 44 46 48 50 52 54 58 60 62 64 66 68 72 74 76 78 80 82 86 88 90 92 94 96 100
