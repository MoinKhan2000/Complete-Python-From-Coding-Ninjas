"""import time
def sort_0_1(l):
    time.time();
    l2=[]
    for i in range(len(l)):
        if(l[i]==0):
            l2.insert(0,0)
        else:
            l2.append(1);
    for el in l2:
        print(el , end=" ")
    print()


# def getList(n):
#     num=int(input())
#     if(num>0):
#         l = [int(x) for x in input().split()]
#         li=sort_0_1(l)

# number = int(input())
# for i in range(number):
#     getList(i)


l=[1,0,1,0,0,1,0,1]
sort_0_1(l)"""


def sort_0_1(l):
    left, right = 0, len(l) - 1
    while left < right:
        while l[left] == 0 and left < right:
            left += 1
        while l[right] == 1 and left < right:
            right -= 1

        if left < right:
            l[left] = 0
            l[right] = 1
            left += 1
            right -= 1

    return l


def getList():
    num = int(input())
    if num > 0:
        l = [int(x) for x in input().split()]
        li = sort_0_1(l)
        for el in li:
            print(el, end=" ")
        print()


number = int(input())
for i in range(1, number + 1):
    getList()
