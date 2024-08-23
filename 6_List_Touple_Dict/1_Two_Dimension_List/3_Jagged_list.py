# Jagged list are the 2d Lists where column size doesn't nedd to be same
"""  
Ex : Jagged List
00 01 02 03
00 01
00 01 02
00 01 02 03
"""
li = [[1, 2, 3], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
for el in li:
    for li in el:
        print(li, end=" ")
    print()
