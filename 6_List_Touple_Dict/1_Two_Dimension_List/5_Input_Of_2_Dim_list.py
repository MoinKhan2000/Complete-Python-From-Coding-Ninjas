n=int(input())
m=int(input());
lst=[[int(j) for j in input().split()] for i in range(n)];

for ele in lst:
    # print(ele, end=" ")
    for li in ele:
        print(li, end=" ")
    print()
print(lst)