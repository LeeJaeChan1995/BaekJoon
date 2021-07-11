n = int(input())

for i in range(n):
    OX = input()
    arr = list(OX)
    count = 0
    count_sum = 0
    for j in range(len(arr)):
        if arr[j] == "O":
            count += 1
            count_sum = count_sum + count
        else:
            count = 0
    print(count_sum)
