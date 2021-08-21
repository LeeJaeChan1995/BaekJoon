X = int(input())

add = 0
count = 0
for i in range(X):
    add = add + (i + 1)
    count = i
    if add >= X:
        break

Column = count
Row = Column + 1

if Row % 2 == 1:
    Column = Row - (add - X)
    Row = (add - X) + 1
elif Row % 2 == 0:
    Row = Row - (add - X)
    Column = (add - X) + 1

print(f"{Row}/{Column}")
