N = int(input())

for _ in range(N):
    S = input()
    for i in range(1, len(S)):
        if S.find(S[i-1]) > S.find(S[i]):
            print(S.find(S[i-1]), S.find(S[i]))
            N -= 1
            break

print(N)