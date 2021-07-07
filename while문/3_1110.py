N = num = int(input())
length = 0

while True:
    ten = N // 10
    one = N % 10
    sum = ten + one
    N = int(str(N % 10)+str(sum % 10))
    length += 1
    
    if N == num:
        break

print(length)