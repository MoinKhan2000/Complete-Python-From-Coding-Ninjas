from functools import reduce
greater = lambda x,y:x if x>y else y
arr  = [1,2,3,4,5,6,7,8,9]
greatestOfArray = reduce(greater,arr)
print(greatestOfArray)
