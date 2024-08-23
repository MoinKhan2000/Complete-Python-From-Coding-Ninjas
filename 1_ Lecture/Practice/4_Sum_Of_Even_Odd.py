n = int(input(""))
sumEven = 0
sumOdd = 0
while n != 0:
    d = n % 10
    if d % 2 == 0:
        sumEven = sumEven + d
    else:
        sumOdd = sumOdd + d
    n = n // 10

print(sumEven , sumOdd)