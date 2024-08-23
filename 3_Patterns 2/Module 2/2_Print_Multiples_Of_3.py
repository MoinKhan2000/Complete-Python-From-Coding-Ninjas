# number1=int(input())
# number2=int(input())
number1=1;
number2=100;

# First way - Correct but larger calculations
for i in range(number1,number2+1,1):
    if(i%3==0):
        # print(i);
        pass
        
# Second Way - Less calculation     (Everytime we have to start from multiple of 3)
for i in range(number1, number2+1, 1):
    if(i%3==0):
        # print(i, end="")
        pass
print("")
        
    
# Third Way - An Efficient Way
if number1%3==0:
    s=number1;
elif number1%3==1:
    s=number1+2;
else:
    s=number1+1;
for i in range(number1,number2+1,3):
    if(i%3==0):
        # print(i, end="");
        pass
       
for i in range(-100, 1):
    print(i, end=" ")