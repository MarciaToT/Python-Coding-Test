# P.118 게임개발

# 캐릭터가 있는 장소는 1 X 1 크기의 정사각형으로 이뤄진 N X M크기의 직사각형으로 각각의 칸은 육지 또는 바다
# 캐릭터는 동서남북중 한곳을 바라본다.
# 맵의 각 칸은 (A,B)로 나타낼 수 있고 A는 북쪽으로 부터 떨어진 칸의 개수, B는 서쪽으로 부터 떨어진 칸의 개수
# 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어있는 공간에는 갈 수 없음
# 캐릭터의 움직임을 설정하기위한 메뉴얼은 하단과 같음

# 1. 현재위치에서 현재방향을 기준으로 왼쪽방향부터 (반시계방향으로 90도회전한방향) 차례대로 갈곳을 정함
# 2. 캐릭터의 바로 왼쪽방향에 가보지 않은 칸이 존재한다면 왼쪽방향으로 회전한 다음 한칸전진, 존재하지않는다면 왼쪽방향으로 회전만하고 1번으로 돌아감
# 3. 만약 4방향 모두 이미 가본칸이거나 바다인 경우 바라보는 방향을 유지하고 뒤로 한칸가고 1번으로 돌아감. 이때 뒤쪽 방향이 바다라 뒤로 갈 수 없는 경우에는 움직임을 멈춤

# 첫째줄 입력은 맵의 크기 N과 M을 공백으로 구분하여 입력
# 둘째줄에는 게임캐릭터가 있는 칸의 좌표(A,B)와 바라보는 방향 d가 전부 공백으로 구분하여 입력 (0:북, 1:동, 2:남, 3:서)
# 셋째줄부터 맵이 육지인지 바다인지에 대한 정보가 주어짐
# N개의 줄에 맵의 상태가 북쪽부터 남쪽순서대로, 각줄의 데이터는 서쪽부터 동쪽 순서대로 주어짐, 맵의 외곽은 항상 바다(0:육지, 1:바다)

n, m = map(int, input().split())
chdir = list(map(int, input().split()))
map = [list(map(int, input().split())) for _ in range(n)]
x = chdir[0]
y = chdir[1]
cnt = 0
map[x][y] = 2

while 1:
    if chdir[2] == 0:
        if map[x][y - 1] == 0:
            chdir[2] = 1
            map[x][y - 1] = 2
            y = y - 1
            print("동쪽 진행")
        elif map[x][y - 1] == 1 or map[x][y - 1] == 2:
            chdir[2] = 1
            print("동쪽 방향 전환")
    elif chdir[2] == 1:
        if map[x + 1][y] == 0:
            chdir[2] = 2
            map[x + 1][y] = 2
            x = x + 1
            print("남쪽 진행")
        elif map[x + 1][y] == 1 or map[x + 1][y] == 2:
            chdir[2] = 2
            print("남쪽 방향 전환")
    elif chdir[2] == 2:
        if map[x][y + 1] == 0:
            chdir[2] = 3
            map[x][y + 1] = 2
            y = y + 1
            print("서쪽 진행")
        elif map[x][y + 1] == 1 or map[x][y + 1] == 2:
            chdir[2] = 3
            print("서쪽 방향 전환")
    elif chdir[2] == 3:
        if map[x - 1][y] == 0:
            chdir[2] = 0
            map[x - 1][y] = 2
            x = x - 1
            print("북쪽 진행")
        elif map[x - 1][y] == 1 or map[x - 1][y] == 2:
            chdir[2] = 0
            print("북쪽 방향 전환")
            #print(chdir[2])
    if ((map[x - 1][y] == 2 or map[x - 1][y] == 1) and (map[x + 1][y] == 2 or map[x + 1][y] == 1)\
            and (map[x][y - 1] == 2 or map[x][y - 1] == 1) and (map[x][y + 1] == 2 or map[x][y + 1] == 1)):
        if chdir[2] == 0:
            if map[x + 1][y] == 1:
                print("정지1")
                break
            else:
                x = x + 1
        elif chdir[2] == 1:
            if map[x][y + 1] == 1:
                print("정지2")
                break
            else:
                y = y + 1
        elif chdir[2] == 2:
            if map[x][y - 1] == 1:
                print("정지3")
                break
            else:
                y = y - 1
        elif chdir[2] == 3:
            if map[x - 1][y] == 1:
                print("정지4")
                break
            else:
                x = x - 1
for i in range(n - 1):
    for j in range(m - 1):
        if map[i][j] == 2:
            cnt = cnt + 1
print(cnt)
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1