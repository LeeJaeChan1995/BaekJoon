T = int(input())

for i in range(T):
    floor, room, guest = map(int, input().split())
    roomNum = guest // floor + 1   # 호수 중 방을 의미
    floorNum = guest % floor       # 호수 중 층을 의미

    if guest % floor == 0:
        roomNum = guest // floor  # 방을 의미
        floorNum = floor
    print(f'{floorNum * 100 + roomNum}')