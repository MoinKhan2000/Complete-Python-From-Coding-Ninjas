# Find the max sum column with index

"""                 Mine Solution                   """


# def largestColumnSum(l1):
#     maxIndex = -1
#     maxSum = -1
#     for i in range(len(l1[0])):
#         sum = 0
#         for j in range(len(l1)):
#             sum += l1[j][i]
#             if sum > maxSum:
#                 maxSum = sum
#                 maxIndex = i
#     return maxIndex, maxSum


# l1 = [[1, 2, 3, 4], [5, 6, 7, 8], [19, 10, 11, 12]]
# print(largestColumnSum(l1))

"""                 Mentor Solution                   """


def largestColumnSum(l1):
    maxIndex = -1
    maxSum = -1
    for i in range(len(l1[0])):
        sum = 0
        for el in l1:
            sum += el[i]
            if sum > maxSum:
                maxSum = sum
                maxIndex = i
    return maxIndex, maxSum


l1 = [[1, 2, 3, 4], [5, 6, 7, 8], [19, 10, 11, 12]]
print(largestColumnSum(l1))
