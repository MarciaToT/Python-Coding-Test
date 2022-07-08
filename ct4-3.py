# 왕실의 나이트
# 체스판은 8X8 좌표평면이고 특정한 한 칸에 나이트 한개가 서있다.
# 나이트는 수평 혹은 수직으로 2칸 이동후 수직 혹은 수평으로 1칸 이동할 수 있다.
# 이 때 8 X 8 죄표평면상에서 나이트의 위치가 주어졌을때 나이트가 이동할 수 있는 경우의 수를 출력하시오
# 행 위치는 1~8로, 열 위치는 a부터 h로 표현
n = input()
cnt = 0

if (ord(n[0]) - 96) + 2 < 9 and int(n[1]) + 1 < 9:
    cnt += 1
if (ord(n[0]) - 96) + 2 < 9 and int(n[1]) - 1 > 0:
    cnt += 1
if (ord(n[0]) - 96) - 2 > 0 and int(n[1]) + 1 < 9:
    cnt += 1
if (ord(n[0]) - 96) - 2 > 0 and int(n[1]) - 1 > 0:
    cnt += 1
if (ord(n[0]) - 96) + 1 < 9 and int(n[1]) + 2 < 9:
    cnt += 1
if (ord(n[0]) - 96) + 1 < 9 and int(n[1]) - 2 > 0:
    cnt += 1
if (ord(n[0]) - 96) - 1 > 0 and int(n[1]) + 2 < 9:
    cnt += 1
if (ord(n[0]) - 96) - 1 > 0 and int(n[1]) - 2 > 0:
    cnt += 1

# if or(ord(n[0])-96) - 2 > 0:

# if int(n[1]) + 2 < 9 or int(n[1]) - 2 > 0:
#     if (ord(n[0])-96) + 1 < 9 or (ord(n[0])-96) - 1 > 0:
#         if int(n[1]) + 2 < 9 and int(n[1]) - 2 > 0 == 1:
#             cnt += 2
#         cnt += 1

print(cnt)
