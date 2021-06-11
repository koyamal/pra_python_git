w = input()

words = list(set(w))

for word in words:
    if w.count(word) % 2 != 0:
        print('No')
        exit()

print('Yes')