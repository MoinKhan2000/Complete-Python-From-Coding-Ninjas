"""             [output for_expression condition]           """

l = [1, 2, 3, 4]
l_new = []
for ele in l:
    # print(ele)
    l_new.append(ele**2)
# print(l_new)


################### Using List Comprehension ###################

li_new_2 = [ele**2 for ele in l_new]
print(li_new_2)

li_even_square = [ele**2 for ele in l_new if ele % 2 == 0]
print(li_even_square)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li_mul_2_mul_3 = [ele for ele in li if (ele % 2 == 0) and (ele % 3 == 0)]
print(li_mul_2_mul_3)

################### Get the intersection list btw 2 lists
l1 = [1, 2, 3, 4, 5]
l2 = [2, 5, 7, 8]
lInterSection = []

# for el in l1:
#     for el2 in l2:
#         if el == el2:
#             lInterSection.append(el)
# print(lInterSection)

# Better way to do this
lInterSection = [el for el in l1 for el2 in l2 if (el == el2)]
print(lInterSection)


####################
# Q - If the element is multiple of two then the element **2 else element
l1 = [1, 2, 3, 4, 5]
l_mul_2_ele_2 = [ele**2 if ele % 2 == 0 else ele for ele in l1]
print(l_mul_2_ele_2)


###################
s = "moin khan"
l_name = [ele for ele in s]
# print(l_name)


################### Create a 2d list
students = ["Moin", "Rohan", "Parikh", "Ankush"]
listStudents = [[chr for chr in el] for el in students]
# print(listStudents)
for ele in listStudents:
    print(ele)
