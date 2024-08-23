# n = int(input())


def checkPalindrom(n):
    temp = n
    reverse = 0
    while temp > 0:
        reminder = temp % 10
        reverse = (reverse * 10) + reminder
        # print(reminder)
        temp = temp // 10
    if n == reverse:
        return True
    else:
        return True


print(checkPalindrom(121))
