N = int(input())
SugarCount = 0

while N >= 0:
    if N % 5 == 0:
        SugarCount += N // 5
        N %= 5
        print(SugarCount)
        break
    N -= 3
    SugarCount += 1

if N != 0 or N < 0:
    print(-1)

# sugar = int(input())

# DONE = False

# if sugar % 5 == 0:
#     # 5로 나눠떨어지는 경우, 이 값이 최소
#     # print("case 1")
#     print(sugar//5)
# else:
#     # 5로 나눠 떨어지지 않는 경우
#     tmp = sugar//5
#     for i in range(tmp, -1, -1):
#         if (sugar - i*5) % 3 == 0:
#             # print(f"case 2, 5kg {i}개 + 3kg {(sugar - i*5)//3}개")
#             print(i + (sugar - i*5)//3)
#             DONE = True
#             break
    
#     # 3, 5로 구성할 수 없는 경우
#     if not DONE:
#         # print("case 3")
#         print(-1)