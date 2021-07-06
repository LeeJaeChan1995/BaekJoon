score = int(input())
if not 0 > score and not 100 < score:
    if 90 <= score and 100 >= score:
        print("A")
    elif 80 <= score and 89 >= score:
        print("B")
    elif 70 <= score and 79 >= score:
        print("C")
    elif 60 <= score and 69 >= score:
        print("D")
    else:
        print("F")