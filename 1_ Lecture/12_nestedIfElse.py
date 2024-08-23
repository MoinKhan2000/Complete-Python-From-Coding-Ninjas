# n=int(input("Enter your number\n"))
# if n%2==0:
#     print("n is even");
#     if n==0:
#         print("n is zero");
#     else:
#         print("n is non zero")
# else:
#     print("n is odd")


"""
if (10 < 0) and (0 < -10):
    print("A")
elif (10>0) or False:
    print("B")
else :
    print("C")
"""

if True or True:
    if False and True or False:
        print("A")
    elif False or False or True and True:
        print("B")  #correct
    else:
        print("C");
else:
    print("D")
