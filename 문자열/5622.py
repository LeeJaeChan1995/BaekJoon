S = input()

dial_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0

for i in S:
    for j in dial_list:
        if i in j:
            time += dial_list.index(j) + 3
            break

print(time)
         