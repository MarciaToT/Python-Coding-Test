# P.178 위에서 아래로
# 첫째줄에 수열에 속해 있는 수의 개수 N이 주어진다
# 둘째줄 부터 n+1번째 줄까지 n개의 수가 입력된다. 1<= n <=100000
# 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. (동일한 수의 순서는 자유롭게 출력 가능)

n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
list.sort(reverse=True)
for i in range(n):
     print(list[i], end=' ')