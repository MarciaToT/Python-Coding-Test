# P.149 음료수 얼려 먹기
# 구멍이 뚫려있는 부분은 0으로, 칸막이가 존재하는 부분은 1로 표시
# 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어있는 경우 서로 연결되어있는것으로 간주
# 얼음 틀의 모양이 주어졌을때 생성되는 총 아이스크림의 개수를 구하시오
# 첫번째 줄에 얼음틀의 세로길이 N과 가로길이 M (1<=n,m <=1000)
# 두번째 줄 부터 n+1줄까지 얼음틀의 형태가 주어짐
#재귀함수는 반복문을 바깥으로 빼자

n, m = map(int, input().split())
map = [list(map(int, input())) for _ in range(n)]
dfscnt = 0

def dfs(graph, x, y):
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return False
    if map[x][y] == 0:
        map[x][y] = 1
        dfs(map, x, y + 1)
        dfs(map, x, y - 1)
        dfs(map, x + 1, y)
        dfs(map, x - 1, y)
        return True

for x in range(m):
    for y in range(n):
        if dfs(map, x, y):
           dfscnt = dfscnt + 1

print(dfscnt)
