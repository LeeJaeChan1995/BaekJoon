list = []
for i in range(9):
    list.append(int(input()))
    
print(max(list))
print(list.index(max(list))+1)

# max() 함수 : 해당 리스트의 최대 값을 반환
# index() 함수 : 해당 리스트의 특정 값이 위치한 인덱스 값을 반환