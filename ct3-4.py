#1이 될 때까지
#어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행한다.
#1. N에서 1을 뺀다. 2. N을 K로 나눈다.

n, k = map(int, input().split())
cnt = 0
while 1 != n:
    if int(n % k) == 0:
        n = int(n/k)
    else:
        n -= 1
    cnt += 1
print(cnt)
