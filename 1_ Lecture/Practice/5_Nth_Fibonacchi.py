n = int(input(""))
a = 0
b = 1
c = b
digit = 0
if n == 0:
    print("0")
    exit();
elif n == 1:
    print("1")
i = 3
while i <= n:
    a = b
    b = c
    c = a + b
    digit = c
    i += 1

print(digit)

