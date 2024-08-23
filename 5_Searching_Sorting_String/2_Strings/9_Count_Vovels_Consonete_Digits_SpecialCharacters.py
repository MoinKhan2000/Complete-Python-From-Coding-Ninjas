def countVovelsConsonentsDigitsSpecialCharacters(str):
    nVovles = 0
    nDigits = 0
    nConsonent = 0
    nSpecialChar = 0

    for char in str:
        if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
            char = char.lower()
            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                nVovles += 1
            else:
                nConsonent += 1
        elif char >= "0" and char <= "9":
            nDigits += 1
        else:
            nSpecialChar += 1
    return nVovles, nConsonent, nDigits, nSpecialChar


str = "aeiouAEIOU123412348qwrhgdsddf!7!@#$%!@#%"
(
    nVovels,
    nConsonent,
    nDigits,
    nSpecialChar,
) = countVovelsConsonentsDigitsSpecialCharacters(str)
print("Voles", nVovels)
print("Consonets are", nConsonent)
print("Digits ", nDigits)
print("Special Char", nSpecialChar)
