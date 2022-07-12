# P.180 성적이 낮은 순서로 학생 출력하기
# 첫번째 줄에 학생의 수 n이 입력
# 두번째 줄부터 n+1 번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력
# a와 학생의 성적은 100이하 자연수, 모든학생의 이름을 성적이 낮은순으로 출력(동점시 학생순서는 상관없음)

n = int(input())
list = []
for i in range(n):
    a, b = input().split(' ')
    list.append([a, int(b)])

list.sort(key=lambda x:x[1])
for j in range(n):
    print(list[j][0], end = ' ')