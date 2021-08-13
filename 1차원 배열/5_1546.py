import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))

max_score = max(score)
average = 0

for i in score:
    average = average + (i / max_score) * 100

print(average / N)
    


