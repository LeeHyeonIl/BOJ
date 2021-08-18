n = int(input())
visited = [False for x in range(n+1)]
array = [0 for x in range(n+1)]

def bfs(cnt):
    if cnt == n+1:
        for i in range(1, n+1):
            print(array[i], end=' ')
        print()

    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                array[cnt] = i
                bfs(cnt+1)
                visited[i] = False
bfs(1)