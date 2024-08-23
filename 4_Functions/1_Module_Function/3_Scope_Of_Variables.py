"""
a1 = 10  # Global Variable
def f1():
    b1 = 12  # Local Variable
    print(a1)  # Here you can use Global variable This will not throw an error
print(a1)
# print(b1)   This will throw an error
print(a1)
"""


# Intresting Part - You can access any global variable defined before the function call
"""
def f3():
    # print(a3)  # 5
    # a3 += 5 # UnboundedLocalError
    global a3
    a3 = 12
    print("inside function a3 ", id(a3), a3)


a3 = 5  # Global Variable
# print(a3)  # 5
print("outside function a3 ", id(a3), a3)
f3()
"""
a = 34


def func():
    global a
    a += 34
    global b
    b += 12
    print(a, id(a))


print(a, id(a))
b = 1
func()
print(a, id(a))
print(b, id(b))
