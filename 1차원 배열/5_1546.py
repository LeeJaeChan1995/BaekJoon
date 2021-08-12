import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))

max_score = max(score)
average = 0

for i in score:
    if i == max_score:
        pass
    
    average = average + (i / max_score) * 100

print(average / N)
    