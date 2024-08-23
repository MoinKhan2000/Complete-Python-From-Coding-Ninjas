def checkArmstrong(n):
    nLen = len(n)
    num = 0
    for i in n:
        num += pow(int(i), int(nLen))
    # print(num)
    if num == int(n):
        return True
    else:
        return False


numberStr = input()
# print(len(numberStr))
print(checkArmstrong(numberStr))
