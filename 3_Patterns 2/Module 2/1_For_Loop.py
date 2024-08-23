"""
for i in "MOIN KHAN":
    print(i, end="");       #MOIN KHAN
print()
for i in range (3,9):
    print(i , end="");      #345678

"""
"""
n=int(input("Enter your number"))
for i in range(0,n):        # n is excluded         range(start, stop, step)
    print(i, end=", ");     # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,  input=10
                            # BY DEFAULT start=0, step=1
"""   

# Experiments 
for i in range(0,10,2):
    # print(i, end=",")       # 0,2,4,6,8,
    pass
print()

        
for i in range(10):
    # print(i, end="_")       # 0_1_2_3_4_5_6_7_8_9_
    pass
print()

# Decreasing numbers
for i in range (10, 1, -1):
    print(i, end=" ")       # 10 9 8 7 6 5 4 3 2           it will not print till 1 
print()

for i in range (10, 0, -1):
    print(i, end=" ")       # 10 9 8 7 6 5 4 3 2 1      it will not print till 1 
print()

for i in range(5):
    print(i, end="")