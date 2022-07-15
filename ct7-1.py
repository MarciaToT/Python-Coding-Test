# P.197 부품 찾기
# n개의 부품은 정수형태의 고유번호가 부여됨, 손님이 m개 종류의 부품을 대량구매할때 가게안에 부품이 모두 있는지 확인하는 견적서 프로그램
# 첫째줄에 정수 n이 주어지고, 둘째줄에 공백으로 구분하여 n개의 정수가 주어짐
# 셋째줄에 정수 m이 주어지고, 넷쨰줄에 공백으로 구분하여 m개의 정수가 주어짐

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

#이진탐색
def bin(i, start, end):
    while start <= end:
        middle = (start + end) // 2
        if nlist[middle] == i:
            print("yes", i, end=' ')
            break
        elif nlist[middle] < i:
            start = start + 1
            if start > end:
                print("no", i, end=' ')
        else:
            end = end - 1
            if start > end:
                print("no", i, end=' ')
nlist.sort()
start = 0
end = n - 1
for i in range(m):
    bin(mlist[i], start, end)

#in list를 사용
# for i in range(m):
#     if mlist[i] in nlist:
#         print("yes", end = ' ')
#     else:
#         print("no", end = ' ')

# 5
# 8 3 7 9 2
# 3
# 5 7 9