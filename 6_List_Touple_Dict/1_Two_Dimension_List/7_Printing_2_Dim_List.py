li = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1], [33, 4]]
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j], end=" ")
#     print()

# for row in li:
#     for col in row:
#         print(col, end=" ")
#     print()

# Printing Methods Using JOIN
# print("ab".join("12"))  # 1ab2
# print("ab".join("123"))  # 1ab2ab3
# print("ab".join("1234"))  # 1ab2ab3ab4
# print("abcd".join("12345"))  # 1abcd2abcd3abcd4abcd5


# print(" ".join(["1", "2", "3", "4"]))
for row in li:
    output = " ".join([str(ele) for ele in row])
    print(output)


# print([[item for item in el] for el in li])
