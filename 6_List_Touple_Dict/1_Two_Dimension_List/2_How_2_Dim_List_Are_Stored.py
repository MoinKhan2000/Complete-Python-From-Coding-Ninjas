li = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for el in range(len(li)):
    for i in range(len(li[el])):
        if el == i:
            li[el][i] = 1
    # print(type(el))
for el in li:
    for li in el:
        print(li, end=" ")
    print()
