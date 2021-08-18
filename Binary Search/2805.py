N, M = map(int, input().split())
heights = [int(x) for x in input().split()]
result = 0
start, end = 0, max(heights)

while start <= end:
    if start == 0 and end == 0:
        break
    mid = (start + end)//2
    total = 0
    for h in heights:
        if total >= M:
            break
        if h > mid:
            total += h % mid

    if total < M:
        end = mid-1
    else:
        result = mid
        start = mid + 1
    # print(f'start = {start} end = {end}')
    # print(f'total = {total} result = {result}')

print(result)
