X = int(input())

add = 0
count = 0
for i in range(X):
    add = add + (i + 1)
    count = i
    if add >= X:
        break

Start = count
End = Start + 1

if End % 2 == 1:
    Start = End - (add - X)
    End = (add - X) + 1
elif End % 2 == 0:
    End = End - (add - X)
    Start = (add - X) + 1

print(f"{End}/{Start}")
