# 시각
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하시오

n = int(input())
cnt = 0
for H in range(0, n + 1):
    for M in range(0, 60):
        for S in range(0, 60):
            time = str(H) + str(M) + str(S)
            if '3' in time:
                cnt += 1
print(cnt)
