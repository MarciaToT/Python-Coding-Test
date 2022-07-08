#상하좌우
#N*N 크기의 판에서 상하좌우로 이동하는 프로그램

N = int(input())
array = list(input().split())
#for i in range(len(array)):
    #print(array[i], end=' ')
x, y = 1, 1
for i in range(len(array)):
    if array[i] == 'L':
        if y - 1 != 0:
            y -= 1
    if array[i] == 'R':
        if y + 1 != N + 1:
            y += 1
    if array[i] == 'U':
        if x - 1 != 0:
            x -= 1
    if array[i] == 'D':
        if x + 1 != N + 1:
            x += 1
print(x, y)

