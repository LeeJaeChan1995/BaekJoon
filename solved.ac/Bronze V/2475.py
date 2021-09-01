inspectNum = list(map(int, input().split()))

square = []
for i in range(len(inspectNum)):
    i = inspectNum[i]
    square.append(i * i)

print(sum(square) % 10)
