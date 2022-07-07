N, M, K = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
big1 = num[N-1]
big2 = num[N-2]
temp = 0
for i in range(int(M/(K+1))):
    temp += big1*K + big2
temp += M % (K+1)*big1
print(temp)