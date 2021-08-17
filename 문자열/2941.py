S = input()
S_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in S_list:
    S = S.replace(i, 'a')
    
print(len(S))