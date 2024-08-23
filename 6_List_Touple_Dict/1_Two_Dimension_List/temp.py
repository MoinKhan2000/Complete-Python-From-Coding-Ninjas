"""
l=[[1,2,3],[4,5,6],[7,8,9]]
print(l[2][1]);
"""
"""
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l[1][3])
"""

"""
l = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
print(l[2])
"""
"""
l=[[1,2,3,4],[5,6],[7,8,9]]
print(l[1][3])
"""
"""
li=[ele**2 for ele in range(5)];
print(li)

li=[[i*j for j in range(4)] for i in range(3)];
print(li)

li = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12]
    ]
"""
"""

li = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for j in range(4):
    for ele in li:
        print(ele[j], end=" ")
        
        10 2
        10  6
        20  20 
"""

"""
def largestRowSum(l1, nRows, mCols):
    maxIndex = -1
    maxSum = -1
    for i in range(nRows):
        sum = 0
        for el in l1:
            print(el[i], end=" ")
            sum += el[i]
            if sum > maxSum:
                maxSum = sum
                maxIndex = i
    print()
    return maxIndex


l1 = [[10, 2], [0, 6], [0, 0]]
print(largestRowSum(l1, len(l1[0]), len(l1)))

"""
"""    

b = mat
    n, m = nRows, mCols
    # arr = [[int(b[i * m + j]) for j in range(m)] for i in range(n)]
    arr = [[int(b[i * m + j]) for j in range(m)] for i in range(n)]
    print(arr)
"""


"""
import math
def wavePrint(mat, nRows, mCols):
# i = 0
# while i < nRows:
#     if i % 2 == 0:
#         j = 0
#         while j < mCols:
#             print(mat[i][j], end=" ")
#             j += 1
#     else:
#         j = mCols - 1
#         while j >= 0:
#             print(mat[i][j], end=" ")
#             j -= 1
#     i += 1
# print()

# print(lst)

for i in range(mCols):
        for j in range(nRows):
            # print(mat[j][i])
            if i % 2 == 0:
                print(mat[j][i], end=" ")
            else:
                print(mat[nRows-j-1][i], end=" ")

li = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
wavePrint(li, len(li), len(li[0]))
"""

"""
def spiralPrint(mat, nRows, mCols):
    # Your code goes here
    elem = nRows * mCols
    main = 0
    rowStart = 0
    colStart = 0
    rowEnd = nRows - 1
    colEnd = mCols - 1
    while main != elem:
        # print(rowStart, rowEnd, colStart, colEnd)

        for i in range(colStart, colEnd):
            print(mat[rowStart][i], end=" ")
            main += 1

        for i in range(rowStart, rowEnd + 1):
            print(mat[i][colEnd], end=" ")
            main += 1
        
        if main < elem:
            for i in range(colEnd - 1, colStart - 1, -1):
                print(mat[rowEnd][i], end=" ")
                main += 1
        if main < elem:
            for i in range(rowEnd - 1, rowStart, -1):
                print(mat[i][colStart], end=" ")
                main += 1

        colStart += 1
        colEnd -= 1
        rowStart += 1
        rowEnd -= 1
        print(main, elem)


li = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
spiralPrint(li, len(li), len(li[0]))
"""


li = [ele**2 for ele in range(10) if ele % 3 == 0]
print(li)
