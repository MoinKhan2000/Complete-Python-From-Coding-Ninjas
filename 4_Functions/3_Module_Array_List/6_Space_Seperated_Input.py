"""def sum(l):
    sum = 0
    for e in l:
        sum += int(e)
    return sum


number = int(input("How many numbers are there to add\n"))
strInput = input("Enter your numbers. Ensure to have spaces between your numbers \n")
print(strInput)
numInputList = strInput.split(" ")
print("The sum is", sum(numInputList))


# How to convert string list to integer list - An Advance Way
intList = [int(x) for x in input().split()]
print(intList)

"""


# Array sum
def sum(l):
    sum = 0
    for e in l:
        sum += e
    return sum


number = int(input())
if number > 0:
    intList = [int(x) for x in input().split(" ")]
    print(sum(intList))
