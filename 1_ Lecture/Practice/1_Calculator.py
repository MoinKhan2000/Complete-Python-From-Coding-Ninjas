while(True):
    case=int(input(""));
    if case==1:
        num1=int(input(""))
        num2=int(input(""))
        print(num1+num2)
    elif case==2:
        num1=int(input(""))
        num2=int(input(""))
        print(num1-num2)
    elif case==3:
        num1=int(input(""))
        num2=int(input(""))
        print(num1*num2)
    elif case==4:
        num1=int(input(""))
        num2=int(input(""))
        print(num1//num2)
    elif case==5:
        num1=int(input(""))
        num2=int(input(""))
        print(int(num1%num2))
    elif case==6:
        break
    else:
        print("Invalid Operation")

