number = int(input(""))
cur_alphabet = ord("A")
i = 0
while i < number:
    j = 0
    while j <= i:
        print_character = chr(cur_alphabet)
        print(print_character, end="")
        j += 1
    print("")
    cur_alphabet += 1
    i += 1
