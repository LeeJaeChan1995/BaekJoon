import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    OX = input()
    count = 0
    sum = 0

    for j in range(len(OX)):
        if OX[j] == "O":
            count += 1
            sum = sum + count
        elif OX[j] == "X":
            count = 0

    print(sum)
