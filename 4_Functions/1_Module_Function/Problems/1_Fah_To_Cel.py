def fahToCel(n):
    cel=0;
    cel = ( n - 32) * 5 / 9
    return int(cel)


def printTable(start, end, step):
    # Implement Your Code Here
    # (32°F − 32) × 5/9 = 0°C
    for i in range(start, end + 1, step):
        print(i, fahToCel(i))

s = int(input())
e = int(input())
step = int(input())
printTable(s, e, step)
