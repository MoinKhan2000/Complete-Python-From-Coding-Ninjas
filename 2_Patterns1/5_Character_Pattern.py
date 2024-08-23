number=int(input(""))
cur_alphabet=ord('A')
i=0
while i<number:
    j=0
    while j<=i:
        print_character=chr(cur_alphabet+j+i)
        print(print_character, end="")
        j+=1
    print("")
    i+=1