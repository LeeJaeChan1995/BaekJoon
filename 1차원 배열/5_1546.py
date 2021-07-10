n = int(input())
t_list = list(map(int, input().split()))
max_s = max(t_list)

mylist = []
for score in t_list :
    mylist.append(score/max_s * 100)
t_avg = sum(mylist)/n
print(t_avg)