# P.217 1로 만들기
# 정수x가 주어질때 사용가능한 연산은 4가지이다.
# 1. x가 5로 나누어떨어지면 5로 나눈다
# 2. x가 3으로 나누어떨어지면 3으로 나눈다
# 3. x가 2로 나누어떨어지면 2로 나눈다
# 4. x에서 1을 뺀다
# 정수 x가 주어졌을때 연산4개를 적절히 사용해서 1을 만들때 연산을 사용하는 최소값을 출력

x = int(input())

d = [0] * 30000
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
print(d[x])




# 2 x 소수로 이루어진 값을 계산못함
# def makeOne(x):
#     cnt = 0
#     while(x != 1):
#         if (x//2) % 2 != 0:
#             if x - 1 % 5 ==0:
#                 x = x - 1
#             elif x % 3 == 0:
#                 x = x//3
#             elif x % 2 == 0:
#                 x = x//2
#             else: x = x - 1
#             cnt = cnt + 1
#         elif x % 5 == 0:
#             x = x//5
#             cnt = cnt + 1
#         elif x % 3 == 0:
#             x = x//3
#             cnt = cnt + 1
#         else: 
#             x = x - 1
#             cnt = cnt + 1
#     return cnt
# print(makeOne(x))