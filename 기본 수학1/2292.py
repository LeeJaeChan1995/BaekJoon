N = int(input())
count = 0
length = 1

for i in range(N):
    length += 6 * i
    count += 1
    if N <= length:
        break

print(count)