N = int(input())

for i in range(N):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]

    count = 0
    for i in score[1:]:
        if i > avg:
            count += 1
    
    result = (count / score[0]) * 100
    print(f'{result:.3f}%')
