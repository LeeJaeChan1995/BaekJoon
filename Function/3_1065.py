def find_hansu(N):
    if N > 99:
        hansu = 99
        for i in range(100, N + 1):
            N_list = list(map(int, str(i)))

            if N_list[2] - N_list[1] == N_list[1] - N_list[0]:
                hansu += 1
    else:
        hansu = N

    return hansu

N = int(input())
print(find_hansu(N))
