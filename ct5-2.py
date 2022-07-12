# 미로 탈출
# n X m 크기의 직사각형 형태의 미로에 갇혀있음. 위치는 1,1 이고 미로의 출구는 (n,m)에 위치하며 한번에 한칸씩 이동 가능
# 괴물이 있는부분은 0으로 없는부분은 1로 표현되어있음 이때 탈출하기위해 움직여야한느 최소칸의 개수는?
# 처음칸과 마지막칸 모두를 포함하여 셈

from collections import deque

n, m = map(int, input().split())
map = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs(map, q, w):
    cnt = 0
    queue = deque()
    queue.append([q, w, cnt])
    while queue:
        print(queue)
        a = queue.popleft()
        x = a[0]
        y = a[1]
        z = a[2]
        visited[x][y] = True
        z = z + 1
        if (0 <= x + 1 <= n - 1 and 0 <= y <= m - 1) and map[x + 1][y] == 1 and visited[x + 1][y] == False:
            queue.append([x + 1, y, z])
        if (0 <= x < n and m - 1 >= y + 1 >= 0) and map[x][y + 1] == 1 and visited[x][y + 1] == False:
            queue.append([x, y + 1, z])
        if (0 <= x - 1 <= n - 1 and 0 <= y <= m - 1) and map[x - 1][y] == 1 and not visited[x - 1][y]:
            queue.append([x - 1, y, z])
        if (n - 1 >= x >= 0 and m - 1 >= y - 1 >= 0) and map[x][y - 1] == 1 and visited[x][y - 1] == False:
            queue.append([x, y - 1, z])
        if x == n - 1 and y == m - 1:
            break
    return z

print(bfs(map, 0, 0))
