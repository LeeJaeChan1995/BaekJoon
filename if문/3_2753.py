year = int(input())

if 1 <= year and 4000 >= year:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("1")
    else:
        print("0")
