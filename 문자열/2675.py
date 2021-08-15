N = int(input())

for i in range(N):
    R, S = input().split()
    iteration = ""
    for j in S:
        iteration += j * int(R)
    print(iteration)
