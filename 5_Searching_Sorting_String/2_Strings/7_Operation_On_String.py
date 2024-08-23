########################################## Split ##########################################
"""
str = "My Name Is Moin Khan"
li = str.split()
print(li)  # ['My', 'Name', 'Is', 'Moin', 'Khan']

str = "My ,Name ,Is ,Moin ,Khan"
li = str.split(",")
print(li)  # ['My ', 'Name ', 'Is ', 'Moin ', 'Khan']

str = "My ,Name ,Is ,Moin ,Khan"
li = str.split(
    ",", 1
)  # Explicitily telling how much should be the part of list 1- (0,1)
print(li)  # ['My ', 'Name ,Is ,Moin ,Khan']
"""

########################################## Replace ##########################################
"""
# replace function returns the replaced string
str = "My Name Is Khan"
str = str.replace("Khan", "Moin")  # My Name Is Moin
# print(str)

# If the key by which you are going to replace is not present then replace function does not do anything
str = "My Name Is Khan"
str = str.replace("asdf", "Moin")  # My Name Is Moin
print(str)

# If there are more than one occurence of replacing string then bydefault it replaces each word
str = "My Name Is Khan Khan Khan"
str = str.replace("Khan", "Moin")  # My Name Is Moin Moin Moin
print(str)

str = "My Name Is Khan Khan Khan"
str = str.replace("Khan", "Moin", 1)  # Explicitily telling the replace function to replace only first occurance of the word
print(str)  # My Name Is Moin Khan Khan
"""


########################################## Find ##########################################
"""
# Returns the index where it found the substring if not present it returns -1
str = "Moin Khan"
index = str.find("Moin")
print(index)


# Explicitily telling the find function to start finding process from index 15 only till last (second arg is also available)
str = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
index = str.find("abcd", 15, 9999)
print(index)

"""


########################################## LOWER/UPPER ##########################################

str = "Moin Khan"
str = str.lower()
print(str)
str = str.upper()
print(str)


########################################## StartsWith ##########################################

str = "My Name Is Khan"
ans = str.startswith("My")  # True
print(ans)

str = "My Name Is Khan"
ans = str.startswith("y")  # False
print(ans)

# Explicitily telling the function to look up into specific part
str = "My Name Is Khan"
ans = str.startswith("Is", len("My Name "), 100)
print(ans)  # True
