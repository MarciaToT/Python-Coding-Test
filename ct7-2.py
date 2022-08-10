# P.201 떡볶이 떡 만들기
# 절단기에 높이h를 지정하면 줄지어진 떡을 절단
# 높이가 h보다 긴 떡은 h 윗부분이 잘리고, 낮은떡은 잘리지 않음
# 예를들어 높이가 19, 14, 10, 17인 떡이 나란히 있고 절단기 높이를 15로 설정 후 자른다면
# 15, 14, 10, 15가 되고 잘리고 난 떡의 길이는 4, 0, 0, 2이고 손님은 도합 6만큼을 가져감
# 손님이 요청한 총 길이가 m일때 적어도 m만큼의 떡을 얻기위해 절단기에 설정할 수 있는 높이의 최댓값은?
# 첫재줄에 떡의개수 n과 요청한 떡의 길이 m이 주어짐
# 둘째줄에 떡의 개별 높이가 주어짐. 떡 높이의 총 합은 m이상이므로 손님은 필요한 만큼 떡을 사갈 수 있음.
# 높이는 0 이상 10억이하

n, m = map(int, input().split())
Hlist = list(map(int, input().split()))

Hlist.sort()


def binsearch(list, m, start, end):
    result = 0
    while start < end:
        mid = (start + end)//2
        sum = 0
        for i in range(n):
            if Hlist[i] - mid >=0:
                sum = sum + Hlist[i] - mid
        if sum >= m:
            start = mid + 1
            result = mid
        elif sum < m:
            end = end - 1
    return result

print(binsearch(Hlist, m, 0, Hlist[n-1]))