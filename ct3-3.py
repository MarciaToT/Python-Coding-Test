#숫자 카드 게임
#첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.
#둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000이하의 자연수이다.
#가장 작은 값이 가장 큰 행의 가장 작은 값을 출력
n, m = map(int, input().split())
aaa = []
for i in range(n):
    num = list(map(int, input().split()))
    aaa.append(min(num))
print(max(aaa))
