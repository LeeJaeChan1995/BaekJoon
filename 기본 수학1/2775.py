T = int(input())

for i in range(T):
    floor = int(input())
    num = int(input())
    people = []
    for peopleNum in range(1, num + 1):
        people.append(peopleNum)
    for floorNum in range(floor):
        for homeNum in range(1, num):
            people[homeNum] += people[homeNum - 1]
    print(people[-1])
