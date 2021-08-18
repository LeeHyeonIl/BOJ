n, m, b = map(int, input().split())

trees = [[int(x) for x in input().split()] for y in range(n)]
minValue, maxValue = 257, -1
INF = 987654321
time = INF
# b가 0이면 블록을 빼야함
# 배열을 순회하면서 알고리즘 수행

def mineCraft(value, b):
    second = 0
    for y in range(n):
        for x in range(m):
            target = trees[y][x]
            addBlock = target - value
            if target == value:     # 같으면
                continue
            elif target > value:    # 크면
                second += addBlock * 2  # 블록의 차이만큼 초*2를 더하고
                b += addBlock           # 남은블록에 추가
            else:                   # 작으면
                b -= value - target     # 블록의 차이만큼 가지고 있는 개수에서 빼고
                if b < 0:               # 가지고 있는 블록이 없다면 중지
                    break
                second += value - target    # 초를 더함
        if b < 0:
            return INF, INF
    return second, value

for i in range(n):
    minValue = min(minValue, min(trees[i]))
    maxValue = max(maxValue, max(trees[i]))


for value in range(minValue, maxValue+1):
    rtime, rheight = mineCraft(value, b)
    if time > rtime:
        time = rtime
        s1 = rtime
        s2 = rheight

print(s1, s2)
        


