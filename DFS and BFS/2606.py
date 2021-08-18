from collections import deque

n = int(input())
m = int(input())
networks = [[] for y in range(n+1)]
cnt = 0 

for i in range(m):
    r1,r2 = map(int, input().split())
    networks[r1].append(r2)
    networks[r2].append(r1)

visited = [False] *(n+1)

def bfs(graph, v):
    global cnt
    visited[v] = True
    queue = deque([v])
    while queue:
        j = queue.popleft()
        for i in graph[j]:
            if not visited[i]:
                cnt+=1
                visited[i] = True             
                queue.append(i)   

bfs(networks, 1)
print(cnt)