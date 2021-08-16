A, B = map(list, input().split())
A = ''.join(reversed(A))
B = ''.join(reversed(B))

print(max(A, B))