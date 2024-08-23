def replaceCharacter(str, char1, char2):
    newStr = str.replace(char1, char2)
    return newStr


str = input("")
char1 = input("Which  Character Is To Be Replaced\n")
char2 = input("Enter the first Character\n")
str2 = replaceCharacter(str, char1, char2)
print(str2)
