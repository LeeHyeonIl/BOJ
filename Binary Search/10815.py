import sys
n = int(input())
p1 = [int(x) for x in sys.stdin.readline().split()]

p1.sort()

m = int(input())
p2 = [int(x) for x in sys.stdin.readline().split()]

def binarySearch(v,start,end):

    while start <= end:
        mid = (start + end) // 2

        if p1[mid] == v:
            return True # 함수를 끝내버린다.
        elif p1[mid] < v:
            start = mid + 1
        else:
            end = mid -1
    return False



for i in range(len(p2)):
    if binarySearch(p2[i], 0, len(p1)-1):
        p2[i] = 1
    else:
        p2[i] = 0

for p in p2:
    print(p, end= ' ')