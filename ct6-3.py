# P.182 두 배열의 원소 교체
# 두개의 배열 a,b는 n개의 원소로 이루어져 있으며 모든 원소는 자연수
# 최대 k번의 바꿔치기 연산을 수행할 수 있는데 이는 a에 있는 원소를 b에 있는 원소와 바꾸는 것을 말함
# 최종목표는 a의 모든원소의 합이 최대가 되도록 하는것

n, k = map(int, input().split(' '))

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
print(sum(a))
