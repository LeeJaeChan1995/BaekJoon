A = int(input())
B = int(input())
C = int(input())
sum = list(str(A * B * C))

for i in range(10):
    print(sum.count(str(i)))
