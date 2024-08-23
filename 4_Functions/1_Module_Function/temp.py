"""
def func(a):
    a=a+10
    return a
a=5;
func(a)
print(a)

# 5
"""

"""
def square(a):
    ans=a*a
    return ans
a=4;
a=square(a);
print(a)
"""
"""
a=14;
def f():
    a=12
    
f();
print(a)
"""

"""
a=14
def f():
    global a
    a=12
    
f();
print(a)
"""

"""
a=14
def f():
    a=12
    return a
a=f();
print(a)

"""

"""
def function (a,b,c=1):
    return a+b-c
value=function(10,12)
print(value)
"""

"""
def function(a, b, c=1):
    return a + b - c
value = function(10, 12, 5)
print(value)
"""


def function(a, b, c=1, d=5):
    return a + b + c + d


value = function(1, 2, d=7)
print(value)
