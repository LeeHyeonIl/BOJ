n, lan = map(int, input().split())
lans = []
result = 0
for i in range(n):
    lans.append(int(input()))

def binarySearch(start, end):
    global result
    if start > end:
        return
    mid = (start + end) // 2
    total = 0
    for l in lans:
        total += l // mid
    
    if total < lan:
        binarySearch(start,mid-1)
    else:
        if mid > result:
            result = mid
        binarySearch(mid+1, end)

binarySearch(1, max(lans))
print(result)
