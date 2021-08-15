S = input().upper()

Alphabet = list(set(S))

Alphabet_count = []
for i in Alphabet:
    count = S.count(i)
    Alphabet_count.append(count)

if Alphabet_count.count(max(Alphabet_count)) > 1:
    print("?")
else:
    maxCount = Alphabet_count.index(max(Alphabet_count))
    print(Alphabet[maxCount])
