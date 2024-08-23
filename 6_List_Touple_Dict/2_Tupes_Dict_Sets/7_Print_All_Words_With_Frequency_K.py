s = "this is a word string having many many word"
words = s.split()
# print(words)

d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
# print(d)
# {'this': 1, 'is': 1, 'a': 1, 'word': 2, 'string': 1, 'having': 1, 'many': 2}

d2 = {}
for w in words:
    d[w] = d.get(w, 0) + 1

k = 2
for w in d2:
    # if d2[w]==k:
    # print(d2[w])
    pass
    #     print(w)


def printKFreqWords(s, k):
    words = s.split()
    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1
    print(d)
    for w in d:
        if d[w] == k:
            print(w)

printKFreqWords(s, 2)
