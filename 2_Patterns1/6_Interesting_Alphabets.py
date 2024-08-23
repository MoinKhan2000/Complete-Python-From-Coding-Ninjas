N = int(input(""))
start_alphabet = ord("A")
our_alphabet = start_alphabet + N - 1
i = 1
while i <= N:
    j = N - i
    k = i
    while j < N:
        print(chr(our_alphabet - k + 1), end="")
        k -= 1
        j += 1
    print("")
    i += 1
