import math
import sys
input = sys.stdin.readline

climb, fall, height = map(int, input().split())

day = (height - fall) / (climb - fall)
print(math.ceil(day))
