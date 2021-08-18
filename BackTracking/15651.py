n, m = map(int, input().split())
MAX = 100
visited = [False for x in range(MAX)]       # 방문여부를 확인하기 위한 배열
array = [0 for x in range(MAX)]             # 탐색값 저장을 위한 배열

def backTracking(cnt):
    if cnt == m: 
        for a in range(m):
            print(array[a], end=' ')
        print()
    else:
        for i in range(1, n+1):    
            array[cnt] = i
            backTracking(cnt+1)

backTracking(0)